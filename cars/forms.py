from django import forms

from .models import Feedback, RequestCar


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'сar_showroom': forms.Select(attrs={'class': 'form-control'}),

        }


class RequestCarForm(forms.ModelForm):
    class Meta:
        model = RequestCar
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'сar_showroom': forms.Select(attrs={'class': 'form-control'}),
            'car': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.Select(attrs={'class': 'form-control'}),

        }
