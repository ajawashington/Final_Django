from django import forms
from django.core import validators


#example of individual validator
# def check_for_z(value):
#      if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with Z')

class Form_Name(forms.Form):
    # name = forms.CharField(validators=[check_for_z])

    name = forms.CharField()
    description = forms.CharField()
    verify_desc = forms.CharField(label='Enter Description Again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

def clean(self):
    all_clean_data = super().clean()
    desc = all_clean_data['description']
    vdesc = all_clean_data['verify_desc']

    if desc != vdesc:
        raise forms.ValidationError('description should match')

    #botcatcher example...import validators replace this method
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len(botcatcher) > 0:
    #         raise  forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher
