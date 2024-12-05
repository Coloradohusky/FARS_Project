from .models import *

import django_tables2 as tables


class YearTable(tables.Table):
    year = tables.LinkColumn(
        'accident_year_index',
        args=[tables.A('year')],
        verbose_name="Year",
        text=lambda record: record['year'],  # Display the year as text
    )
    total_accidents = tables.Column(verbose_name="Total Accidents")
    total_fatals = tables.Column(verbose_name="Total Fatalities")
    total_persons = tables.Column(verbose_name="Total Persons")
    total_vehicles = tables.Column(verbose_name="Total Vehicles")
    class Meta:
        model = Accident
        fields = (
            "year", "total_accidents", "total_fatals", "total_persons", "total_vehicles"
        )
        template_name = "django_tables2/semantic.html"


class AccidentTable(tables.Table):
    st_case = tables.Column(linkify=True)
    vehicles = tables.Column(empty_values=())

    def render_vehicles(self, record):
        vehicles = record.vehicle_set.all()
        return ", ".join(str(dict(Vehicle.make.field.choices).get(str(vehicle.make), vehicle.make)) for vehicle in vehicles) if vehicles else "No vehicles"

    def render_state(self, record):
        choices = dict(Accident.state.field.choices)
        return choices.get(str(record.state), record.state)

    def render_harm_ev(self, record):
        choices = dict(Accident.harm_ev.field.choices)
        return choices.get(str(record.harm_ev), record.harm_ev)

    def render_man_coll(self, record):
        choices = dict(Accident.man_coll.field.choices)
        return choices.get(str(record.man_coll), record.man_coll)

    class Meta:
        model = Accident
        fields = (
            "st_case", "datetime", "state", "fatals", "persons", "ve_total", "harm_ev", "man_coll", "vehicles"
        )
        template_name = "django_tables2/semantic.html"


class AccidentAggregateTable(tables.Table):
    # state = tables.Column(verbose_name="State")
    metric = tables.Column(verbose_name="metric")
    # Alabama = tables.Column(verbose_name="Alabama")
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for state in Accident.state.field.choices:
    #         # Add a column for each state dynamically
    #         state = state[1]
    #         self.base_columns[state] = tables.Column(verbose_name=state)
    # total_fatalities = tables.Column(verbose_name="Total Fatalities")
    # total_accidents = tables.Column(verbose_name="Total Accidents")

    class Meta:
        template_name = "django_tables2/semantic.html"
        attrs = {"class": "table"}
