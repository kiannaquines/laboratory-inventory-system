from django.db import models

class EquipmentCategory(models.Model):
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    equipment_model = models.CharField(max_length=100)
    equipment_model_number = models.CharField(max_length=100)
    equipment_purchase_date = models.DateField()
    equipment_model_cost = models.DecimalField(max_digits=10, decimal_places=2)
    equipment_model_quantity = models.IntegerField()
    equipment_category = models.ForeignKey(EquipmentCategory, on_delete=models.CASCADE)

class ChemicalCategory(models.Model):
    category_name = models.CharField(max_length=100)
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

    name = models.CharField(max_length=200)
    composition = models.CharField(max_length=10, choices=chemical_composition)
    quantity = models.IntegerField()
    chemical_category = models.ForeignKey(ChemicalCategory, on_delete=models.CASCADE)
    expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'chemicals'
        verbose_name_plural = 'Chemicals'