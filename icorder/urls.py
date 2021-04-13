import urllib
from django.urls import path
from . import views

app_name = 'icorder'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('panel_create/', views.add_panel, name="panel_create"),
    path('plate_create/', views.add_plate, name='plate_create'),
    path('gom_create/', views.add_gom, name='gom_create'),
    path('sheet_create/', views.add_sheet, name='sheet_create'),
    path('window_create/', views.add_window, name='window_create'),
    path('yuka_create/', views.add_yuka, name='yuka'),
    path('printlami_create/', views.add_printlami, name='printlami_create'),
    path('customer_list/', views.SearchResultView.as_view(), name='customer_list'),
]
