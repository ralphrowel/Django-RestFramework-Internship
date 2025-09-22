from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "person_firstname",
            "person_middlename",
            "person_lastname",
            "person_age",
            "person_gender",
            "person_contact",
        ]
