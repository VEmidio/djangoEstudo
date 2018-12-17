from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano informado é: ' + str(year))

def lerDoBanco(name):
    list_name = [
        {'name': 'Ana', 'ega': 22},
        {'name': 'Joao', 'ega': 26},
        {'name': 'Joaquim', 'ega': 27}
    ]

    for pessoa in list_name:
        if pessoa['name'] == name:
            return pessoa
    else:
        return {'name': 'The person was is not found ', 'ega': 0}



def fname(request, name):
    result = lerDoBanco(name)
    if result['ega'] > 0:
        return HttpResponse('The person was found, his ega is:  ' + str(result['ega']) + ' years')
    else:
        return HttpResponse('The person was is not found ')

def fname2(request, name):
    ega = lerDoBanco(name)['ega']
    return render(request, 'pessoa.html', {'v_idade': ega})