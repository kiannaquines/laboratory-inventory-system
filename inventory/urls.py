from django.urls import path
from inventory.views import *

urlpatterns = [
    # Dashboard View
    path('',DashboardPage.as_view(),name="dashboard"),
    
    # List Views
    path('equipments/',EquipmentList.as_view(),name="equipments"),
    path('equipments/category',EquipmentCategory.as_view(),name="equipment_category"),
    path('equipments/report',EquipmentReport.as_view(),name="equipment_report"),
    path('users/',UserList.as_view(),name="users"),
    path('chemicals/',ChemicalList.as_view(),name="chemicals"),
    path('chemicals/category',ChemicalList.as_view(),name="chemical_category"),
    path('chemicals/report',ChemicalList.as_view(),name="chemical_report"),
    

    # Create Views

    # Update Views

    # Delete Views
]