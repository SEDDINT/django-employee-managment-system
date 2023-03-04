from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('show_employee', views.show_employee, name="show_employee"),
    path('add_employee', views.add_employee, name='add_employee'),
    path('update_employee/<employee_id>',
         views.update_employee, name='update_employee'),
    path('delete_employee/<employee_id>',
         views.delete_employee, name="delete_employee"),
    path('employee_info_table', views.employee_info_table,
         name='employee_info_table'),
    path('search', views.search, name='search'),
]
