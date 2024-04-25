from django.shortcuts import render, redirect
from .forms import UsuarioPerfilForm, PerfilForm

def llenar_tablas(request):
    if request.method == 'POST':
        usuario_form = UsuarioPerfilForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario = usuario_form.save(commit=False)
            usuario.save()  # Guardamos el usuario primero para obtener su ID
            perfil = perfil_form.save(commit=False)
            perfil.usuario = usuario  # Asignamos el usuario al perfil
            perfil.save()  # Guardamos el perfil
            return redirect('exito')
    else:
        usuario_form = UsuarioPerfilForm()
        perfil_form = PerfilForm()
    return render(request, 'llenar_tablas.html', {'usuario_form': usuario_form, 'perfil_form': perfil_form})

def exito(request):
    return render(request, 'exito.html')
