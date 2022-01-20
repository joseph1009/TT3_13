
from .models import Message
from django.forms import ModelForm


class messageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
    
