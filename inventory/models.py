from django.db import models

class EquipmentCategory(models.Model):
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100,help_text="Enter the equipment name.")
    equipment_model = models.CharField(max_length=100,help_text="Enter the equipment model.")
    equipment_model_number = models.CharField(max_length=100,help_text="Enter the equipment model number.")
    equipment_purchase_date = models.DateField(help_text="Enter the equipment purchase date.")
    equipment_model_cost = models.DecimalField(max_digits=10, decimal_places=2,help_text="Enter the equipment model cost.")
    equipment_model_quantity = models.IntegerField(help_text="Enter the equipment model quantity.")
    equipment_category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE,help_text="Select the equipment category.")
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'equipment'
        verbose_name_plural = 'Equipment'

class ChemicalCategory(models.Model):
    category_name = models.CharField(max_length=100,help_text="Enter the chemical category name.")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chemical_categories'
        verbose_name_plural = 'Chemical Categories'

class Chemicals(models.Model):
    chemical_composition = (
        ('solid', 'Solid'),
        ('liquid', 'Liquid'),
        ('gas', 'Gas'),
    )

    name = models.CharField(max_length=200,help_text="Enter the chemical name.")
    composition = models.CharField(max_length=10, choices=chemical_composition,help_text="Select the chemical composition.")
    quantity = models.IntegerField(help_text="Enter the quantity of the chemical.")
    chemical_category = models.ForeignKey(ChemicalCategory, on_delete=models.CASCADE,help_text="Select the chemical category.")
    expiration_date = models.DateField(auto_now_add=False,name="",help_text="Enter the expiration date of the chemical.")

    class Meta:
        db_table = 'chemicals'
        verbose_name_plural = 'Chemicals'