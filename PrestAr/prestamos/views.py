from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .filters import SimulacionFilter
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm


# def register(resquest):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {'form': form}
#     return render(request, 'registration/register.html', context)


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
            if request.user.is_authenticated:
                simulacion.author = request.user
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

    return render(request, 'sobre_conami.html', {'filter': simulaciones})


def sobre_creditos(request):
    simulaciones = SimulacionFilter(
        request.GET, queryset=Simulacion.objects.all())

    return render(request, 'sobre_creditos.html', {'filter': simulaciones})


# SOLICITUDES

def solicitud_new(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            if request.user.is_authenticated:
                solicitud.author = request.user
            solicitud.save()
            return redirect('solicitud_detail', pk=solicitud.pk)
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/solicitud_edit.html', {'form': form})


def solicitud_edit(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == "POST":
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.save()
            return redirect('solicitud_detail', pk=solicitud.pk)
    else:
        form = SolicitudForm(instance=solicitud)
    return render(request, 'solicitudes/solicitud_edit.html', {'form': form})
