from django import forms
from .models import Telephone

class TelephoneForm(forms.ModelForm):

  class Meta:
    model = Telephone
    fields = ('name','profession','tel_num','mob_num')



