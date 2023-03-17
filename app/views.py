from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from app.models import Pessoa
from app.forms import PessoaForm
from app.models import Escola
from app.forms import EscolaForm
from django.forms import inlineformset_factory
from app.forms import MatematicaForm
from app.models import Matematica
from django.urls import reverse

class IndexView(TemplateView):
    template_name = "index.html"

class ModeloView(TemplateView):
    template_name = "model.html"    

class SobreView(TemplateView):
    template_name = "sobre.html"

def login(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user =authenticate(username=username, password=senha)

        if user:
            return render(request, 'login.html')
        else:
            return render(request, 'negado.html')  

@login_required        
def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return render('negado.html')
    
def lista(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        context = {
            'lista': pessoas,
        }
        return render(request, "resultados.html", context)


def index(request):
    if request.method == "GET":
        form = PessoaForm()
        form_escola_factory = inlineformset_factory(Pessoa, Escola, form=EscolaForm, extra=1)
        form_escola = form_escola_factory()
        context = {
            'form': form,
            'form_escola': form_escola,
    }
        return render(request, "form.html", context = context)
    
    elif request.method == "POST":
        form = PessoaForm(request.POST)
        form_escola_factory = inlineformset_factory(Pessoa, Escola, form=EscolaForm)
        form_escola = form_escola_factory(request.POST)
        if form.is_valid() and form_escola.is_valid():
            resultado = form.save()
            form_escola.instance = resultado
            form_escola.save()
            return redirect(reverse('questoes'))

        else:
            context = {
                'form': form,
                "form_escola": form_escola,
            }    

            return render(request, "form.html", context)

#pesquisar switch case

def mat(request):
    if request.method == "GET":
        form_matematica = MatematicaForm()
        context = {
            'form': form_matematica
    }
    return render(request, "questoes.html", context = context)
