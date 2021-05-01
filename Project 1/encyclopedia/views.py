from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib import messages
from django.db import models
from random import seed, randint
from . import util

class NewTaskForm(forms.Form):
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit(request, name):
    return render(request, "encyclopedia/edit.html", {
        "name" : name.capitalize(),
        "content" : util.get_entry(name)
    })

def new(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        # Verifica se o FORM é valido
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # Verificar se o título já não está sendo usado
            entries = util.list_entries()
            exist = False
            for entry in entries:
                if title == entry:
                    # Se sim retorna uma mensagem de erro
                    messages.info(request, 'This article already exist!')
                    exist = True
            # Se não, salva o artigo
            if exist == False:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('wiki:index'))
        else:
            return render(request, "encyclopedia/new.html", {
                "form" : form
            })

    return render(request, "encyclopedia/new.html", {
        "form" : NewTaskForm()
    })

def random(request):
    entries = util.list_entries()
    n = randint(0, len(entries))
    return greet(request, entries[n-1])

def greet(request, name):
    # Cria uma variável com a lista dos nomes existentes
    entries = util.list_entries()
    exist = False
    # Faz um laço que verifica se o nome está contido na lista de artigos
    for entry in entries:
        # Se sim retorna a página do artigo (retorna também o nome e o conteúdo do artigo)
        if name==entry:
            return render(request, "encyclopedia/entry.html", {
                "name" : name.capitalize(),
                "content" : util.get_entry(name)})
            exist = True
        # Se não retorna a página de erro
    if exist==False:
        return render(request, "encyclopedia/error.html", {
            "name" : name.capitalize().upper()
            })