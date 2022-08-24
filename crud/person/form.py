from django.forms import ModelForm, EmailInput
from person.models import Person

class FormPerson(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }