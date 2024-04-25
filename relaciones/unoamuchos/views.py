from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm

def agregar_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('exito_libro')
    else:
        autor_form = AutorForm()
    return render(request, 'agregar_autor.html', {'autor_form': autor_form})

def agregar_libro(request):
    if request.method == 'POST':
        libro_form = LibroForm(request.POST)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('exito_libro')
    else:
        libro_form = LibroForm()
    return render(request, 'agregar_libro.html', {'libro_form': libro_form})

def exito_libro(request):
    return render(request, 'exito_libro.html')
