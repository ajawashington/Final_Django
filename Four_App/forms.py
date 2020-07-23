from django import forms
from django.core import validators
from django.contrib.auth.models import User
# from Four_App.models import UserProfileInfo










#MODEL FORM EXAMPLES
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta:
#         model = UserProfileInfo
#         fields = ('portfolio_site', 'profile_pic')















#BASIC MODEL FORMS

# from Four_App.models import User
#
# #Creating a model form
# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#
# #example of individual validator
# # def check_for_z(value):
# #      if value[0].lower() != 'z':
# #         raise forms.ValidationError('Name needs to start with Z')
#
# class Form_Name(forms.Form):
#     # name = forms.CharField(validators=[check_for_z]) <use this for individual validation
#
#     name = forms.CharField()
#     description = forms.CharField()
#     verify_desc = forms.CharField(label='Enter Description Again')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                 widget=forms.HiddenInput,
#                                 validators=[validators.MaxLengthValidator(0)])
#
#                                 #botcatcher example...import validators replace this method
#                                 # def clean_botcatcher(self):
#                                 #     botcatcher = self.cleaned_data['botcatcher']
#                                 #
#                                 #     if len(botcatcher) > 0:
#                                 #         raise  forms.ValidationError('GOTCHA BOT!')
#                                 #     return botcatcher
#
# #this validator works for the full form and not one individual field
# def clean(self):
#     all_clean_data = super().clean()
#     desc = all_clean_data['description']
#     vdesc = all_clean_data['verify_desc']
#
#     if desc != vdesc:
#         raise forms.ValidationError('description should match')
