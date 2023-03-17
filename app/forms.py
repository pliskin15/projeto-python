from django import forms
from app.models import Pessoa
from app.models import Escola
from app.models import Matematica
# Create your models here.

class PessoaForm(forms.ModelForm):
   class Meta:
      model = Pessoa
      fields = "__all__"

class EscolaForm(forms.ModelForm):
   class Meta:
      model = Escola
      fields = "__all__"  

class MatematicaForm(forms.ModelForm):
   class Meta:
      model = Matematica
      fields = "__all__"

