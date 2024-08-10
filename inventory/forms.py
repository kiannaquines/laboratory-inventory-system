from django import forms
from inventory.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DefaultUser


class FilterReportForm(forms.Form):

    chemical_category = forms.ModelChoiceField(
        queryset=ChemicalCategory.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Chemical Category",
        error_messages={
            "required": "Chemical category field is required."
        },
    )

    chemical_units = forms.ChoiceField(
        choices=Chemicals.chemical_units_category,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        error_messages={
            "required": "Chemical unit field is required."
        },
    )

    available_chemical = forms.BooleanField(
        required=True,
        label="Only Available Chemical",
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}),
        error_messages={
            "required": "Chemical availability field is required."
        },
    )
    
    date_from = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"}),
        error_messages={
            'invalid': 'Enter a valid start date.',
        }
    )

    date_to = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"type": "date", "class": "form-control"}),
        error_messages={
            'invalid': 'Enter a valid start date.',
        }
    )


    class Meta:
        fields = [
            "chemical_category",
            "chemical_units",
            "available_chemical",
            "date_from",
            "date_to",
        ]


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Username"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "First Name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Last Name"}
        )

    class Meta:
        model = DefaultUser
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if (
                field_name == "is_staff"
                or field_name == "is_superuser"
                or field_name == "is_active"
            ):
                field.widget.attrs.update(
                    {
                        "class": "custom-control-input",
                    }
                )
            else:
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                        "placeholder": field.label,
                        "spellcheck": "false",
                        "required": field.required,
                    }
                )

    class Meta:
        model = DefaultUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if (
                field_name == "is_staff"
                or field_name == "is_superuser"
                or field_name == "is_active"
            ):
                field.widget.attrs.update(
                    {
                        "class": "custom-control-input",
                    }
                )
            else:
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                        "placeholder": field.label,
                        "spellcheck": "false",
                        "required": field.required,
                    }
                )

    class Meta:
        model = DefaultUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
        ]
        exclude = [
            "password1",
            "password2",
        ]


class ChemicalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChemicalForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == "availability":
                field.widget.attrs.update(
                    {
                        "class": "custom-control-input",
                    }
                )
            else:
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                        "placeholder": field.label,
                        "spellcheck": "false",
                        "required": field.required,
                    }
                )

    class Meta:
        model = Chemicals
        fields = "__all__"
        widgets = {
            "expiration_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }


class ChemicalCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChemicalCategoryForm, self).__init__(*args, **kwargs)
        self.fields["category_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Category Name",
                "spellcheck": "false",
            }
        )

    class Meta:
        model = ChemicalCategory
        fields = "__all__"


class EquipmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": field.label,
                    "spellcheck": "false",
                    "required": field.required,
                }
            )

    class Meta:
        model = Equipment
        fields = "__all__"
        widgets = {
            "equipment_purchase_date": forms.DateInput(
                {
                    "type": "date",
                }
            )
        }


class EquipmentCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": field.label,
                    "spellcheck": "false",
                    "required": field.required,
                }
            )

    class Meta:
        model = EquipmentCategory
        fields = "__all__"
