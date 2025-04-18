# assignment stuffs
from django import forms
from .models import Make

class MakeForm(forms.ModelForm):
    class Meta:
        model = Make
        fields = ['name']
        # You can also use fields = '__all__' if you want every field in the model.