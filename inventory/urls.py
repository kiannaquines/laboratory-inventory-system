from django.urls import path
from inventory.views import DashboardPage, EquipmentList, UserList, ChemicalList

urlpatterns = [
    # Dashboard View
    path('',DashboardPage.as_view(),name="dashboard"),
    
    # List Views
    path('equipments/',EquipmentList.as_view(),name="equipments"),
    path('users/',UserList.as_view(),name="users"),
    path('chemicals/',ChemicalList.as_view(),name="chemicals"),

    # Create Views

    # Update Views

    # Delete Views
]