from django.shortcuts import render, get_object_or_404
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db.models import Count, Sum, F
from django.db.models.functions import ExtractYear
import django_tables2 as tables
import json
import sys
import os
import pandas as pd

from rest_framework import viewsets
from rest_framework_gis import filters
from django_tables2 import RequestConfig
from django_tables2.paginators import LazyPaginator

import folium
from folium import plugins, Popup

from .models import Accident, Vehicle, Person
from .tables import *

def get_fill_color(fatals):
    if fatals > 5:
        return 'red'
    elif fatals > 3:
        return 'orange'
    elif fatals > 2:
        return 'yellow'
    elif fatals > 1:
        return 'cadetblue'
    else:
        return 'cyan'

from .serializers import (
    AccidentSerializer,
)

class AccidentViewSet(
    viewsets.ReadOnlyModelViewSet,
):
    bbox_filter_field = "location"
    filter_backends = [filters.InBBoxFilter]
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer


def accident_detail(request, year, st_case):
    accident = get_object_or_404(Accident, datetime__year=year, st_case=st_case)
    vehicles = Vehicle.objects.filter(st_case=accident)
    persons = Person.objects.filter(st_case=accident)
    map1 = folium.Map(location=[accident.location.y, accident.location.x],
        tiles=None,  # Start with no base tiles
        zoom_start=12,
        control_scale=False)
    folium.TileLayer('CartoDB Dark_Matter', name='Dark Matter').add_to(map1)
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(map1)
    folium.CircleMarker(
        location=[accident.location.y, accident.location.x],
        radius=6,
        color='blue',
        fill=True,
        fill_color=get_fill_color(accident.fatals),
        fill_opacity=0.7,
    ).add_to(map1)
    folium.LayerControl(collapsed=False).add_to(map1)
    map1 = map1._repr_html_()
    return render(request, 'accident_detail.html', {'accident': accident, 'vehicles': vehicles, 'persons': persons, 'map1': map1})

def accident_year_index(request, year):
    table = AccidentTable(Accident.objects.filter(datetime__year=year).order_by('-fatals'))
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(table)
    # this is faster than Accident.objects.count()
    length = Accident.objects.all().order_by('-id')[0].id
    fatals = Accident.objects.aggregate(Sum('fatals'))['fatals__sum']
    persons = Accident.objects.aggregate(Sum('persons'))['persons__sum']
    vehicles = Accident.objects.aggregate(Sum('ve_total'))['ve_total__sum']
    aggregate_state_data = (
    Accident.objects.values('state').annotate(
            total_fatalities=Sum('fatals'),
            total_accidents=Count('id')
        )
    )
    for item in aggregate_state_data:
        choices = dict(Accident.state.field.choices)
        item['state'] = choices.get(str(item['state']), "unk")
    aggregate_state_data = sorted(aggregate_state_data, key=lambda x: x['state'])
    aggregate_state_data = (
        pd.DataFrame(aggregate_state_data)
        .melt(id_vars=["state"], value_vars=["total_fatalities", "total_accidents"], var_name="metric", value_name="value")
        .pivot(index="metric", columns="state", values="value")
        .reset_index()
        .to_dict(orient="records")
    )
    columns = []
    for state in Accident.state.field.choices:
        # Add a column for each state dynamically
        state = state[1]
        columns.append((state, tables.Column()))
    aggregate_state_table = AccidentAggregateTable(aggregate_state_data, extra_columns = columns)

    aggregate_make_data = (
    Vehicle.objects.values('make').annotate(
            total_fatalities=Sum('st_case__fatals'),
            total_vehicles=Count('id')
        )
    )
    for item in aggregate_make_data:
        choices = dict(Vehicle.make.field.choices)
        item['make'] = choices.get(str(item['make']), "unk")
    aggregate_make_data = sorted(aggregate_make_data, key=lambda x: x['make'])
    aggregate_make_data = (
        pd.DataFrame(aggregate_make_data)
        .melt(id_vars=["make"], value_vars=["total_vehicles", "total_fatalities"], var_name="metric", value_name="value")
        .pivot(index="metric", columns="make", values="value")
        .reset_index()
        .to_dict(orient="records")
    )
    columns = []
    for make in Vehicle.make.field.choices:
        # Add a column for each state dynamically
        make = make[1]
        columns.append((make, tables.Column()))
    aggregate_make_table = AccidentAggregateTable(aggregate_make_data, extra_columns = columns)

    aggregate_harm_ev_data = (
    Accident.objects.values('harm_ev').annotate(
            total_fatalities=Sum('fatals'),
            total_accidents=Count('id')
        )
    )
    for item in aggregate_harm_ev_data:
        choices = dict(Accident.harm_ev.field.choices)
        item['harm_ev'] = choices.get(str(item['harm_ev']), "unk")
    aggregate_harm_ev_data = sorted(aggregate_harm_ev_data, key=lambda x: x['harm_ev'])
    aggregate_harm_ev_data = (
        pd.DataFrame(aggregate_harm_ev_data)
        .melt(id_vars=["harm_ev"], value_vars=["total_fatalities", "total_accidents"], var_name="metric", value_name="value")
        .pivot(index="metric", columns="harm_ev", values="value")
        .reset_index()
        .to_dict(orient="records")
    )
    columns = []
    for harm_ev in Accident.harm_ev.field.choices:
        # Add a column for each state dynamically
        harm_ev = harm_ev[1]
        columns.append((harm_ev, tables.Column()))
    aggregate_harm_ev_table = AccidentAggregateTable(aggregate_harm_ev_data, extra_columns = columns)

    aggregate_body_typ_data = (
    Vehicle.objects.values('body_typ').annotate(
            total_fatalities=Sum('st_case__fatals'),
            total_vehicles=Count('id')
        )
    )
    for item in aggregate_body_typ_data:
        choices = dict(Vehicle.body_typ.field.choices)
        item['body_typ'] = choices.get(str(item['body_typ']), "unk")
    aggregate_body_typ_data = sorted(aggregate_body_typ_data, key=lambda x: x['body_typ'])
    aggregate_body_typ_data = (
        pd.DataFrame(aggregate_body_typ_data)
        .melt(id_vars=["body_typ"], value_vars=["total_vehicles", "total_fatalities"], var_name="metric", value_name="value")
        .pivot(index="metric", columns="body_typ", values="value")
        .reset_index()
        .to_dict(orient="records")
    )
    columns = []
    for body_typ in Vehicle.body_typ.field.choices:
        # Add a column for each state dynamically
        body_typ = body_typ[1]
        columns.append((body_typ, tables.Column()))
    aggregate_body_typ_table = AccidentAggregateTable(aggregate_body_typ_data, extra_columns = columns)

    context = {'table': table, 'aggregate_state_table': aggregate_state_table, 'aggregate_make_table': aggregate_make_table, 'aggregate_harm_ev_table': aggregate_harm_ev_table, 'aggregate_body_typ_table': aggregate_body_typ_table,
               'length': length, 'year': year, 'fatals': fatals, 'persons': persons, 'vehicles': vehicles}
    return render(request, 'accident_year_index.html', context)

def accident_index(request):
    accidents_by_year = (
        Accident.objects.annotate(year=ExtractYear('datetime'))
        .values('year')
        .annotate(
            total_accidents=Count('id'),
            total_fatals=Sum('fatals'),
            total_persons=Sum('persons'),
            total_vehicles=Sum('ve_total'),
        )
        .order_by('-year')
    )
    table = YearTable(accidents_by_year)
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    context = {'table': table}
    return render(request, 'accident_index.html', context)

def index(request):
    print("Start request", file=sys.stderr)
    cache_file = os.path.dirname(os.path.realpath(__file__)) + '/templates/map_generated.html'
    if not os.path.exists(cache_file) or (os.path.getmtime(cache_file) < os.path.getmtime(os.path.realpath(__file__))):
        data = Accident.objects.annotate(
            geojson=AsGeoJSON('location')
        ).values('geojson', 'st_case', 'fatals', 'datetime')

        data_list = [
            [
                json.loads(d['geojson'])['coordinates'][1],  # Latitude (y)
                json.loads(d['geojson'])['coordinates'][0],  # Longitude (x)
                d['fatals']
            ]
            for d in data
        ]

        # Create the base map
        map1 = folium.Map(location=[50, -110],
                          tiles=None,  # Start with no base tiles
                          zoom_start=3,
                          min_zoom=3,
                          control_scale=False)

        # Add multiple tile layers with custom display names
        folium.TileLayer('CartoDB Dark_Matter', name='Dark Matter').add_to(map1)
        folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(map1)
        # folium.TileLayer('Stamen Terrain', name='Terrain').add_to(map1)
        # folium.TileLayer('Stamen Toner', name='Toner').add_to(map1)

        # Create the heatmap layer
        heatmap_layer = folium.FeatureGroup(name="Heatmap")
        plugins.HeatMap(
            data_list,
            name="Heatmap",
            radius=15,
        ).add_to(heatmap_layer)

        for d, sublist in zip(data, data_list):
            sublist.append(d['st_case'])
            sublist.append(d['datetime'])

        marker_layer = folium.FeatureGroup(name="Markers")
        # add stuff to marker_layer
        marker_cluster = plugins.MarkerCluster(
            name="Marker Cluster",
            options={"disableClusteringAtZoom": 9}
        )

        print("Start adding coords", file=sys.stderr)
        for coords in data_list:
            folium.CircleMarker(
                location=[coords[0], coords[1]],
                radius=6,
                color='blue',
                fill=True,
                fill_color=get_fill_color(coords[2]),
                fill_opacity=0.7,
                popup=Popup(
                    f"""
                    <div style="width: 250px; font-size: 14px;">
                        <strong>Case Num:</strong>
                        <a href="/accidents/{coords[4].year}/{coords[3]}/" target="_blank" style="color: blue; text-decoration: underline;">
                            {coords[3]}
                        </a><br>
                        <strong>Fatalities:</strong> {coords[2]}
                    </div>
                    """,
                    max_width=300
                )
            ).add_to(marker_cluster)
        print("Done adding coords", file=sys.stderr)

        marker_cluster.add_to(marker_layer)

        heatmap_layer.add_to(map1)
        marker_layer.add_to(map1)

        # Add LayerControl and Fullscreen plugins
        folium.LayerControl(collapsed=False).add_to(map1)
        plugins.Fullscreen(position='topright').add_to(map1)

        # Render the map
        print("Rendering Map", file=sys.stderr)

        map1 = map1._repr_html_()
        with open(cache_file, "w") as f:
            f.write(map1)

    with open(cache_file, 'r') as f:
        map1_html = f.read()

    context = {'map1': map1_html}
    print("Done Rendering Map", file=sys.stderr)

    return render(request, 'index.html', context)

