from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .filters import SimulacionFilter
from .forms import *
from .models import *


def sim_index(request):
    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())

    return render(request, 'simulador/sim_index.html', {'filter': simulaciones})


def simulaciones_list(request):
    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())

    return render(request, 'simulador/simulaciones_list.html', {'filter': simulaciones})


def simulacion_detail(request, pk):
    simulacion = get_object_or_404(Simulacion, pk=pk)
    return render(request, 'simulador/simulacion_detail.html', {'simulacion': simulacion})


def simulacion_new(request):
    if request.method == "POST":
        form = SimulacionForm(request.POST)
        if form.is_valid():
            simulacion = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            simulacion.save()
            return redirect('simulacion_detail', pk=simulacion.pk)
    else:
        form = SimulacionForm()
    return render(request, 'simulador/simulacion_edit.html', {'form': form})


def simulacion_edit(request, pk):
    simulacion = get_object_or_404(Simulacion, pk=pk)
    if request.method == "POST":
        form = SimulacionForm(request.POST, instance=simulacion)
        if form.is_valid():
            simulacion = form.save(commit=False)
            simulacion.save()
            return redirect('simulacion_detail', pk=simulacion.pk)
    else:
        form = SimulacionForm(instance=simulacion)
    return render(request, 'simulador/simulacion_edit.html', {'form': form})


def simulacion_remove(request, pk):
    simulacion = get_object_or_404(Simulacion, pk=pk)
    simulacion.delete()

    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())
    return render(request, 'simulador/simulaciones_list.html', {'filter': simulaciones})


def sobre_conami(request):
    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())

    return render(request, 'simulador/sobre_conami.html', {'filter': simulaciones})


def sobre_creditos(request):
    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())

    return render(request, 'simulador/sobre_creditos.html', {'filter': simulaciones})
