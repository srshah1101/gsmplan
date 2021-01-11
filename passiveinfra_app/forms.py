from django.forms import ModelForm
from passiveinfra_app.models import pi_correspondence



class PassiveInfraForm(ModelForm):

    original_letter = ModelForm.FileField()
    reply_letter = ModelForm.FileField()
    class Meta:
        model=pi_correspondence
        fields=['department','originlletter_desc','replyletter_desc']