from django.shortcuts import render

# Create your views here.

def cotacoins(request):
    return render(request, 'cotacoins.html')

def cotacao(request):
    return render(request, 'cotacao.html')

def buscar_cotacao(request):
    return render(request, 'buscar_cotacao.html')

def infos_grafico(request):
    return render(request, 'infos_grafico.html')

def grafico(request):
    return render(request, 'grafico.html')
