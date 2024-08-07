from django.urls import path
from inventory.views import *

app_name = 'inventory'

urlpatterns = [

    # Auth Urls
    path('', LoginPage.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register"),
    
    # Dashboard Urls
    path('dashboard/',DashboardPage.as_view(),name="dashboard"),
    
    # List Urls
    path('users/',UserList.as_view(),name="users"),

    path('equipments/',EquipmentList.as_view(),name="equipments"),
    path('equipments/category',EquipmentCategory.as_view(),name="equipment_category"),
    path('equipments/report',EquipmentReport.as_view(),name="equipment_report"),

    path('chemicals/',ChemicalList.as_view(),name="chemicals"),
    path('chemicals/category',ChemicalCategory.as_view(),name="chemical_category"),
    path('chemicals/report',ChemicalReport.as_view(),name="chemical_report"),
    
    # Create Urls
    path('chemicals/add/', AddChemicalView.as_view(), name='add_chemical'),
    path('chemicals/category/add/', AddChemicalCategoryView.as_view(), name='add_chemical_category'),
    path('equipments/add/', AddEquipmentView.as_view(), name='add_equipment'),
    path('equipments/category/add', AddEquipmentCategoryView.as_view(), name='add_equipment_category'),
    # Update Urls

    # Delete Urls
]