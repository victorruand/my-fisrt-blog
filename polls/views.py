''' AQUI NAS VIEWS PODEMOS: LER DB, GERAR PDF, SAÍDA DE UM XML, CRIAR UM ZIP SOB DEMANDA, USAR QUAQUER LIB DO PYTHON'''
#Tudo que o Django espera é que a view devolva um HttpResponse. Ou uma exceção.
#from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse


from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context ={
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    

def results(request,question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(resquest, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
