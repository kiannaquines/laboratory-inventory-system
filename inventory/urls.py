from django.urls import path
from inventory.views import *
from inventory.custom_view.auth_views import *
from inventory.custom_view.user_views import *
from inventory.custom_view.equipment_views import *
from inventory.custom_view.chemical_views import *

app_name = 'inventory'

urlpatterns = [

    # Auth Urls
    path('login/', LoginPage.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('logout/',logout_view, name='app_logout'),
    # Dashboard Urls
    path('',DashboardPage.as_view(),name="dashboard"),

    # Equipment Urls
    path('equipments/add/', AddEquipmentView.as_view(), name='add_equipment'),
    path('equipments/category/add', AddEquipmentCategoryView.as_view(), name='add_equipment_category'),
    path('equipments/',EquipmentListView.as_view(),name="equipments"),
    path('equipments/category',EquipmentCategoryView.as_view(),name="equipment_category"),
    path('equipments/report',EquipmentReportView.as_view(),name="equipment_report"),

    # Chemicals Urls
    path('chemicals/',ChemicalListView.as_view(),name="chemicals"),
    path('chemicals/report',ChemicalReportView.as_view(),name="chemical_report"),    
    path('chemicals/add/', AddChemicalView.as_view(), name='add_chemical'),
    path('chemicals/update/<int:chemical_id>', UpdateChemicalView.as_view(), name='update_chemical'),
    path('chemicals/delete/<int:chemical_id>', DeleteChemicalView.as_view(), name='delete_chemical'),

    path('chemicals/category',ChemicalCategoryView.as_view(),name="chemical_category"),
    path('chemicals/category/add/', AddChemicalCategoryView.as_view(), name='add_chemical_category'),
    path('chemicals/category/update/<int:chemical_category_id>', UpdateChemicalCategoryView.as_view(), name='update_chemical_category'),
    path('chemicals/category/delete/<int:chemical_category_id>', DeleteChemicalCategoryView.as_view(), name='delete_chemical_category'),

    # Users Urls
    path('users/',UserList.as_view(),name="users"),
    path('users/add/', AddUserView.as_view(), name="add_user"),
    path('users/update/<int:user_id>', UpdateUserView.as_view(), name="update_user"),
    path('users/delete/<int:user_id>', DeleteUserView.as_view(), name="delete_user"),

    # Generate Report Urls
    path('chemicals/report/generate_report/', generate_report, name="generate_report"),
]