from django import forms
from django.core.validators import RegexValidator
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'name', 'institute', 'whatsapp_no', 'dob', 'gender',
            'fathers_name', 'mothers_name', 'course', 'semester', 'address', 'dp', 'surname',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'institute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Your Institute'}),
            'whatsapp_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your father\'s name'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your mother\'s name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of course you\'re enrolled in'}),
            'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your current semester'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'rows': 3}),
        }

class ConsultationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_number = mobile_number = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit mobile number.')]
    )
    date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'])
    institute = forms.CharField(max_length=100)
    custom_msg = forms.CharField(widget=forms.Textarea)
