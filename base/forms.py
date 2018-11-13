

from django import forms

class ContactForm(forms.Form):
    Votre_email = forms.EmailField(required=True)
    Sujet = forms.CharField(required=True)
    Votre_message = forms.CharField(widget=forms.Textarea, required=True)