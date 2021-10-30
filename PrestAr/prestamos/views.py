from django.shortcuts import render


def simulaciones_list(request):
    return render(request, 'simulador/simulaciones_list.html', {})
