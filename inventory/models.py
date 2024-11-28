from django.db import models
from django.contrib.auth.models import User

class RequestChemical(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    chemical_requested = models.ForeignKey('Chemicals', on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.chemical_requested.quantity -= self.requested_quantity        
        self.chemical_requested.save()
        return self.chemical_requested.quantity

    def __str__(self) -> str:
        return self.requested_by.get_full_name()

    class Meta:
        db_table ='request_chemicals'
        verbose_name_plural = 'Request Chemicals'
        verbose_name = 'Request Chemical'
        ordering = ['-requested_by']


class ChemicalCategory(models.Model):
    category_name = models.CharField(max_length=100,help_text="Enter the chemical category name.")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chemical_categories'
        verbose_name_plural = 'Chemical Categories'

    def __str__(self) -> str:
        return self.category_name

class Chemicals(models.Model):
    chemical_composition = (
        ('solid', 'Solid'),
        ('liquid', 'Liquid'),
        ('gas', 'Gas'),
    )

    chemical_units_category = (
        ('g', 'Gram'),
        ('mg', 'Milligram'),
        ('μg', 'Microgram'),
        ('kg', 'Kilogram'),
        ('L', 'Liter'),
        ('mL', 'Milliliter'),
        ('μL', 'Microliter'),
        ('mol', 'Mole'),
        ('mmol', 'Millimole'),
        ('μmol', 'Micromole'),
        ('M', 'Molarity'),
        ('m', 'Molality'),
        ('X', 'Mole fraction'),
        ('ppm', 'Parts per million'),
        ('ppb', 'Parts per billion'),
        ('J', 'Joule'),
        ('kJ', 'Kilojoule'),
        ('eV', 'Electronvolt'),
        ('°C', 'Degrees Celsius'),
        ('°F', 'Degrees Fahrenheit'),
        ('K', 'Kelvin'),
        ('Pa', 'Pascal'),
        ('kPa', 'Kilopascal'),
        ('atm', 'Atmosphere'),
        ('mmHg', 'Millimeters of mercury')
    )

    name = models.CharField(max_length=200,help_text="Enter the chemical name.")
    composition = models.CharField(max_length=10, choices=chemical_composition,help_text="Select the chemical composition.")
    quantity = models.IntegerField(help_text="Enter the quantity of the chemical.")
    chemical_category = models.ForeignKey(ChemicalCategory, on_delete=models.CASCADE,help_text="Select the chemical category.")
    chemical_units = models.CharField(max_length=10, choices=chemical_units_category,null=True, blank=True, help_text="Select the chemical units.")
    expiration_date = models.DateField(auto_now_add=False,name="",help_text="Enter the expiration date of the chemical.")
    date_acquired = models.DateField(auto_now_add=False,name="",help_text="Enter date acquired of the chemical.")
    availability = models.BooleanField(default=True, help_text="Select if the chemical is available.")
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'chemicals'
        verbose_name_plural = 'Chemicals'

    def __str__(self) -> str:
        return self.name