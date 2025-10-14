from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message', 'cc_email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 5}),
            'cc_email': forms.EmailInput(attrs={'placeholder': 'CC email (optional)'}),
        }
