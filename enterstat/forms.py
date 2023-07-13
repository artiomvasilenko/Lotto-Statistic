from django.forms import ModelForm
from datetime import date
from django.forms import ModelForm
from .models import Lottery, Name

class LotteryForm(ModelForm):
    class Meta:
        model = Lottery
        fields = ['date', 'name', 'price', 'result']
