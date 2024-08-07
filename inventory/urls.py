from django.urls import path
from inventory.views import *

urlpatterns = [

    # Auth Urls
    path('', LoginPage.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register"),
    
    # Dashboard Urls
    path('dashboard/',DashboardPage.as_view(),name="dashboard"),
    
    # List Urls
    path('equipments/',EquipmentList.as_view(),name="equipments"),
    path('equipments/category',EquipmentCategory.as_view(),name="equipment_category"),
    path('equipments/report',EquipmentReport.as_view(),name="equipment_report"),
    path('users/',UserList.as_view(),name="users"),
    path('chemicals/',ChemicalList.as_view(),name="chemicals"),
    path('chemicals/category',ChemicalList.as_view(),name="chemical_category"),
    path('chemicals/report',ChemicalList.as_view(),name="chemical_report"),
    

    # Create Urls

    # Update Urls

    # Delete Urls
]