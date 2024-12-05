from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "map/simple/",
        TemplateView.as_view(template_name="map_generated.html"),
    ),
    path('map/', views.index, name='map'),
    path('accidents/<int:year>/<int:st_case>/', views.accident_detail, name='accident_detail'),
    path('accidents/<int:year>/', views.accident_year_index, name='accident_year_index'),
    path('accidents/', views.accident_index, name='accident_index'),
]