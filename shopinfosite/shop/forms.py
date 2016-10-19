from django import forms
from .models import ContactMessage
from django import template
register = template.Library()
from django.utils.translation import ugettext_lazy as _
from django.core import validators

from django.contrib import admin

from django.core.exceptions import ValidationError

from django.forms import TextInput, Textarea

class ContactForm(forms.ModelForm):
    # contact_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    # content = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea
    # )



    full_name = forms.CharField(

        widget=TextInput(attrs={
            'required':True,
            'class': 'form-control'
        })
    )

    email = forms.EmailField(

        widget=TextInput(attrs={
            'class': 'form-control'
        })
    )
    contact_no = forms.IntegerField(

        widget=TextInput(attrs={
            'class': 'form-control'
        })
    )
    title = forms.CharField(

        widget=TextInput(attrs={
            'class': 'form-control'
        })
    )
    message = forms.CharField(

        widget=Textarea(attrs={
            'class': 'form-control'
        })
    )


    class Meta:
        model = ContactMessage
        fields = ('full_name', 'email', 'contact_no', 'title', 'message',)





    def save(self, commit=True):
        """ This is override method of ModelForm.

        """
        model = super(ContactForm, self).save(commit=False)
        if commit:
            model.save()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("invalid email")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return email




