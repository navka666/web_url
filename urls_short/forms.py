from django import forms
from urls_short.models import URL


class UrlForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url_max', 'url_short']
        labels = { 'url_short': '', 'url_max': ''}
        widgets={'url_max': forms.TextInput(attrs={'placeholder': 'Your URL'}), 
                'url_short': forms.TextInput(attrs={'placeholder': 'Your short URL (optional)'}) }

