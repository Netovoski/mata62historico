from django.shortcuts import render, redirect, get_object_or_404
import json
# Create your views here.
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from projpad.models import *
from django.db.models import Sum
from appprincipal.forms import *
from .forms import *
from projpad.models import *
#from chartit import DataPool, Chart, PivotDataPool, PivotChart

def index(request):
    return render(request, 'index.html')


def Hist_2015_1(request):
    item = Hist_voo2015.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2015 Janeiro',
    }
    return render(request, 'hist2015.html', context)


def Hist_2015_2(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Fevereiro',
    }
    return render(Hist_2015_1, 'hist2015.html', context)


def Hist_2015_3(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Março',
    }
    return render(Hist_2015_1, 'hist2015.html', context)

def Hist_2015_4(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Abril',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_5(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Maio',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_6(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 junho',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_7(Hist_2015_1):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Julho',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

def Hist_2015_8(request):
    pass
    context = {
        'item': item,
        'header': 'Historico 2015 Agosto',
    }
    return render(Hist_2015_1, 'hist2015.html', context) 

# def Hist_2015_9(request):
#     item = Hist_voo2015_9.objects.all()
#     context = {
#         'item': item,
#         'header': 'Historico 2015 Setembro',
#     }
#     return render(request, 'hist2015.html', context) 

# def Hist_2015_10(request):
#     item = Hist_voo2015_10.objects.all()
#     context = {
#         'item': item,
#         'header': 'Historico 2015 Outubro',
#     }
#     return render(request, 'hist2015.html', context) 

# def Hist_2015_11(request):
#     item = Hist_voo2015_11.objects.all()
#     context = {
#         'item': item,
#         'header': 'Historico 2015 Novembro',
#     }
#     return render(request, 'hist2015.html', context) 

# def Hist_2015_12(request):
#     item = Hist_voo2015_12.objects.all()    
#     context = {
#         'item': item,
#         'header': 'Historico 2015 Dezembro',
#     }
#     return render(request, 'hist2015.html', context) 

# def historico(request):
#     queryset = Hist_voo2015.objects.all()
#     sigla = [obj.sigla for obj in queryset]
#     situacao = [obj.situacao for obj in queryset]

#     context = {
#         'sigla': json.dumps(sigla),
#         'situacao': json.dumps(situacao),
#     }
#     return render(request, 'historico.html', context)
    

def Hist_2016_1(request):
    item = Hist_voo2016.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2016 Janeiro',
    }
    return render(request, 'hist2016.html', context)


def Hist_2016_2(Hist_2016_1):
    pass
    context = {
        'header': 'Historico 2016 Fervereiro',
    }
    return render(Hist_2016_1, 'hist2016.html', context)

def Hist_2016_3(Hist_2016_1):
    pass
    context = {
        'header': 'Historico 2016 Março',
    }
    return render(Hist_2016_1, 'hist2016.html', context)

def Hist_2017_1(request):
    item = Hist_voo2017.objects.all()
    context = {
        'item': item,
        'header': 'Historico 2017 Janeiro',
    }
    return render(request, 'hist2017.html', context)

