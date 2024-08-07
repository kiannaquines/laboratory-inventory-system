from typing import Any
from django import forms
from inventory.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DefaultUser

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if field_name == 'is_staff' or field_name == 'is_superuser' or field_name == 'is_active':
                field.widget.attrs.update({
                    'class': 'custom-control-input',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label,
                    'spellcheck': 'false',
                    'required': field.required
                })

    class Meta:
        model = DefaultUser
        fields = ['username','first_name','last_name','email','is_staff','is_superuser','is_active','password1', 'password2']


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
        widgets = {
            'equipment_purchase_date': forms.DateInput({
                'type': 'date',
            })
        }

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