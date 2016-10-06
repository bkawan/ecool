from django import forms
from .models import ContactMessage
from django import template
register = template.Library()



class ContactForm(forms.ModelForm):
    # contact_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    # content = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea
    # )

    class Meta:
        model = ContactMessage
        fields = ('full_name', 'email', 'contact_no', 'message',)

