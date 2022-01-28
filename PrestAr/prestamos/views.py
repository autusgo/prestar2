from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .filters import SimulacionFilter
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
            # Acá chequea que el monto de la simulación no super el SMVM, pero no tirar error de aviso
            if simulacion.importe_solicitado <= int(12*(simulacion.smvm.monto)):
                if request.user.is_authenticated:
                    simulacion.author = request.user
                simulacion.save()
                return redirect('simulacion_detail', pk=simulacion.pk)
            else:
                maximo = str(12*(simulacion.smvm.monto))
                messages.error(
                    request, f'El monto solicitado supera los 12 salarios mínimos. Ingresar un monto inferior a ${maximo}')
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

def solicitud_detail(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    return render(request, 'solicitudes/solicitud_detail.html', {'solicitud': solicitud})


# @login_required(login_url='accounts/login')
def solicitud_new(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        # print(form)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.emprendedor = request.user
            minimo = solicitud.minimo()
            if minimo == True:
                if solicitud.importe_solicitado <= int(12*(solicitud.smvm.monto)):
                    if request.user.is_authenticated:
                        solicitud.author = request.user
                    solicitud.save()
                    return redirect('solicitud_detail', pk=solicitud.pk)
                else:
                    maximo = str(12*(solicitud.smvm.importe_solicitado))
                    messages.error(
                        request, f'El monto solicitado supera los 12 salarios mínimos. Debe ser inferior a ${maximo}')
            else:
                messages.error(
                    request, 'El emprendimiento debe tener una antigüedad mayor a los 6 meses')
        else:
            messages.error(request, 'Algo no está bien')
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


# CONFIGURACIONES

def configuracion(request):

    return render(request, 'configuracion.html', {'filter': configuracion})


def smvm_new(request):
    if request.method == "POST":
        form = SMVMForm(request.POST)
        if form.is_valid():
            smvm = form.save(commit=False)
            if request.user.is_authenticated:
                smvm.author = request.user
            smvm.save()
            return redirect('smvm_edit', pk=smvm.pk)
    else:
        form = SMVMForm()
    return render(request, 'configuracion/smvm/smvm_edit.html', {'form': form})


def smvm_detail(request, pk):
    smvm = get_object_or_404(SMVM, pk=pk)
    return render(request, 'configuracion/smvm_detail.html', {'smvm': smvm})


def smvm_edit(request, pk):
    smvm = get_object_or_404(SMVM, pk=pk)
    if request.method == "POST":
        form = SMVMForm(request.POST, instance=smvm)
        if form.is_valid():
            smvm = form.save(commit=False)
            smvm.created_date = timezone.now()
            smvm.save()
            return redirect('smvm_detail', pk=smvm.pk)
    else:
        form = SMVMForm(instance=smvm)
    return render(request, 'configuracion/smvm_edit.html', {'form': form})


def tasa_new(request):
    if request.method == "POST":
        form = TasaInteresForm(request.POST)
        if form.is_valid():
            tasa = form.save(commit=False)
            if request.user.is_authenticated:
                tasa.author = request.user
            tasa.save()
            return redirect('tasa/tasa_edit', pk=tasa.pk)
    else:
        form = TasaInteresForm()
    return render(request, 'configuracion/tasa_edit.html', {'form': form})


def tasa_detail(request, pk):
    tasa = get_object_or_404(TasaInteres, pk=pk)
    return render(request, 'configuracion/tasa_detail.html', {'tasa': tasa})


def tasa_edit(request, pk):
    tasa = get_object_or_404(TasaInteres, pk=pk)
    if request.method == "POST":
        form = TasaInteresForm(request.POST, instance=tasa)
        if form.is_valid():
            tasa = form.save(commit=False)
            tasa.created_date = timezone.now()
            tasa.save()
            return redirect('tasa_detail', pk=tasa.pk)
    else:
        form = TasaInteresForm(instance=tasa)
    return render(request, 'configuracion/tasa_edit.html', {'form': form})
