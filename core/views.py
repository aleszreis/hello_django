from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name, age):
    return HttpResponse(f'<h1>Hello {name} de {age} anos.<h1>')

def operacao(request, operacao, n1, n2):
    if operacao == 'soma':
        return HttpResponse(f'A soma de {n1} + {n2} é igual a {n1+n2}.')
    elif operacao == 'subtração':
        return HttpResponse(f'A subtração de {n1} - {n2} é igual a {n1-n2}.')
    elif operacao == 'multiplicação':
        return HttpResponse(f'A multiplicação de {n1} * {n2} é igual a {n1*n2}.')
    elif operacao == 'divisão':
        return HttpResponse(f'A divisão de {n1} / {n2} é igual a {n1/n2}.')
    else:
        return HttpResponse('Operação não compreendida. Por favor, digite a operação desejada corretamente, e no seguinte formato: divisão/número1/número2/')