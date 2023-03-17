from django.db import models
from django.db.models import CASCADE

ONE_CHOICES = (
  ('interior', 'Interior'),
  ('capital', 'Capital')

)

COORD_CHOICES = (
      ('cd01', 'Coordenação 1'),
      ('cd02', 'Coordenação 2')
)

ESC_CHOICES = (
    ('escola1', 'escola 1'),
    ('escola2', 'escola 2')
)

TURNO_CHOICES = (
    ('Matutino', 'Matutino'),
    ('Vespertino', 'Vespertino'),
    ('Noturno', 'Noturno'),
    ('Integral','Integral')
)

SERIE_CHOICES = (
    ('2º Ano EF', '2º Ano EF'),
    ('4º Ano EF', '4º Ano EF'),
    ('8º Ano EF', '8º Ano EF'),
    ('2º Ano EM', '2º Ano EM'),
)

MAT_CHOICES = (
    ('Biologia', 'Biologia'),
    ('Matemática', 'Matemática'),
    ('Portugês', 'Portugês'),
)

TURMA_CHOICES = (
    ('Turma 1', 'Turma 1'),
    ('Turma 2', 'Turma 2'),
    ('Turma 3', 'Turma 3'),
)

CONT_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)


class Pessoa(models.Model):

    região = models.CharField(max_length=10, choices=ONE_CHOICES)
    coordenação = models.CharField(max_length=10, choices=COORD_CHOICES)
    escola = models.CharField(max_length=10, choices=ESC_CHOICES)
    professor = models.EmailField(blank=True, null=True)

class Escola(models.Model):
    cadastro = models.ForeignKey(Pessoa, on_delete=CASCADE, related_name='adicionais')    
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    série = models.CharField(max_length=10, choices=SERIE_CHOICES)
    matéria = models.CharField(max_length=10, choices=MAT_CHOICES)
   #alterar para checklist
    turma = models.CharField(max_length=10, choices=TURMA_CHOICES)


# construir formulário para a matéria class Matemática(models.Model)
class Matematica(models.Model):

    coleta = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi possível realizar a coleta?")
    ausencia = models.CharField(max_length=50, verbose_name="Se não foi possível, indique o motivo:")
    numero = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi utilizada a temática Números? ")
    algebra = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi utilizada a temática Algebra? ")
    geometria = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi utilizada a temática Geometria? ")
    probabilidade = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi utilizada a temática Probabilidade e Estatística? ")
    grandezas = models.CharField(max_length=10, choices=CONT_CHOICES, verbose_name="Foi utilizada a temática Grandezas e Medidas? ")
