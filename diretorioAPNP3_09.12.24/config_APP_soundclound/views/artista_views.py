from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from forms import ArtistaForm
from models.artista import Artista

def listar_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'artista/listar.html', {'artistas': artistas})

def criar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas')
    else:
        form = ArtistaForm()
    return render(request, 'artista/criar.html', {'form': form})

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artista/editar.html', {'form': form})

def deletar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('listar_artistas')
    return render(request, 'artista/deletar.html', {'artista': artista})

def ver_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'artista/ver.html', {'artista': artista})
