from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu
from .forms import MenuForm

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'Menu/menu_list.html', {'menus': menus})

def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    
    # Fazendo a chamada à API do IBGE para obter a frequência do nome
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{menu.nome}"
    response = requests.get(url)
    
    # Verifique se a resposta é válida e filtre os dados para o período de 2000 a 2010
    frequencia_2000_2010 = None
    if response.status_code == 200:
        api_data = response.json()
        for entry in api_data:
            for res in entry['res']:
                if res['periodo'] == "[2000,2010[":
                    frequencia_2000_2010 = res['frequencia']
                    break
    else:
        frequencia_2000_2010 = 'Não foi possível obter os dados da API.'
    
    return render(request, 'Menu/menu_detail.html', {'menu': menu, 'frequencia_2000_2010': frequencia_2000_2010})


def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'Menu/menu_form.html', {'form': form})

def menu_update(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'Menu/menu_form.html', {'form': form})

def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'Menu/menu_confirm_delete.html', {'menu': menu})
