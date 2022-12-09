from django import forms
from .models import UserInput
import re
from django.core.exceptions import ValidationError


class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        # fields = '__all__'
        fields = ['user_name', 'user_number' ]
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        user_name = self.cleaned_data['user_name']
        if re.match(r'\d', user_name):
            raise ValidationError('ФИО не должно начинаться с цифры')
        return user_name

# class UserResultForm(forms.ModelForm):
#     class Meta:
#         model = UserInput