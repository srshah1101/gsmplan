from django.forms import ModelForm
from passiveinfra_app.models import pi_correspondence
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from django.forms import DateInput





# class PassiveInfraForm(forms.ModelForm):
#
#     original_letter = ModelForm.FileField()
#     reply_letter = ModelForm.FileField()
#
#     class Meta:
#         model=pi_correspondence
#         fields=['department','originletter_date','originlletter_desc','replyletter_desc','replyletter_date']
#         widgets = {
#             'originletter_date': DateInput(attrs={'type': 'date'})
#         }