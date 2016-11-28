# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:19:51 2016

@author: lindo
"""


from django import forms
from django.contrib.auth.models import User
from SpecManApp.models import UserProfile
from registration.forms import RegistrationForm

#class UserForm(forms.ModelForm):
class UserForm(RegistrationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    
    class Meta :
        model = User
        fields =('username','first_name','last_name','email', 'password')
        
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('FullNames','CityTown','PostalAddress','PostalCode','CellphoneNumber','TelNumber','YearSubmitted','CommunicationMethod','picture','Landline','Fax','StatusRelation','Other','AdvantageArea','AffectedParty','PhysicalAddress','PropertyFarm','DeedNumber','FarmName','Radio','Radio_Other','TVSignal','OtherTV','TVLicence','ElectronicComm','IcasaLicence','OtherElectronicComm','state','OtherInterest','AdditionalInfo','Certify')