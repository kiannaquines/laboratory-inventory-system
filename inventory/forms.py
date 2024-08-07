from typing import Any
from django import forms
from inventory.models import *

class ChemicalForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ChemicalForm,self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'spellcheck': 'false',
                'required': field.required
            })

    class Meta:
        model = Chemicals
        fields = '__all__'
        widgets = {
            'expiration_date': forms.DateInput(attrs={
                'type': 'date',
            }),
        }

class ChemicalCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChemicalCategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Category Name','spellcheck': 'false',})

    class Meta:
        model = ChemicalCategory
        fields = '__all__'

class EquipmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'spellcheck': 'false',
                'required': field.required
            })

    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'spellcheck': 'false',
                'required': field.required,
            })
            
    class Meta:
        model = EquipmentCategory
        fields = '__all__'