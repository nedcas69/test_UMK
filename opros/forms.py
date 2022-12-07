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
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'user_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('ФИО не должно начинаться с цифры')
        return title

# class UserResultForm(forms.ModelForm):
#     class Meta:
#         model = UserInput