from django.forms import ModelForm
from .models import Entretenimento

class EntretenimentoForm(ModelForm):
    class Meta():
        model = Entretenimento
        fields = '__all__'