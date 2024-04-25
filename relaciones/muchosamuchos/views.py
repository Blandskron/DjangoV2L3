from django.shortcuts import render, redirect
from .forms import ArticuloForm

def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('envio_exitoso')
    else:
        form = ArticuloForm()
    return render(request, 'agregar_articulo.html', {'form': form})

def envio_exitoso(request):
    return render(request, 'envio_exitoso.html')
