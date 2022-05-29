from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from random import randint

class NewEntryForm(forms.Form):
    title = forms.CharField(label='New entrys title')
    new_entry_md = forms.CharField(widget=forms.Textarea, label='New entrys markdown')

class EditEntryForm(forms.Form):
    entry_md = forms.CharField(widget=forms.Textarea, label='Entrys markdown')

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry):
    markdowner = Markdown()
    raw_md = util.get_entry(entry)
    if raw_md:
        html_entry = markdowner.convert(raw_md)
        return render(request, "encyclopedia/entry.html",{
            'html_entry': html_entry,
            'name': entry,
            'edit_link_activated': 'true'
        })
    else:
        return render(request, "encyclopedia/not_found.html")
    
def search(request):
    if request.method == 'POST':
        entry = request.POST['q']
        if util.get_entry(entry):
            return HttpResponseRedirect(reverse('entry_page', args = [entry] ))
        else:
            entries = util.list_entries()
            some_entries = []

            for element in entries:
                if str(entry).lower() in element.lower():
                    some_entries += [element]

            if len(some_entries):
                #Cambiar el index para que diga algo mejor. Ponerle algo mejor a la ruta
                return render(request, "encyclopedia/index.html", {
                    "entries": some_entries
                })
            else:
                #Poner un mensaje descriptivo en Not Found
                return render(request, "encyclopedia/not_found.html")

    return HttpResponse('Not even a POST')

def new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            new_entry_md = form.cleaned_data['new_entry_md']

            if util.get_entry(title):
                #This error messaje should be sexier.
                return HttpResponse('Error. Duplicate entry')
            else:
                util.save_entry(title, new_entry_md)
                return HttpResponseRedirect(reverse("entry_page", args = [title] ))
        else:
            #This error message could be (Not neccessary) sexier
            return HttpResponse('Invalid form')

    return render(request, "encyclopedia/new_entry.html", {
        'form': NewEntryForm()
    })

def edit_page(request, entry):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            new_md = form.cleaned_data['entry_md']
            util.save_entry(entry, new_md)
        return HttpResponseRedirect(reverse("entry_page", args = [entry] ))
    if request.method == "GET":
        markdowner = Markdown()
        raw_md = util.get_entry(entry)
        data = {
            'entry_md': raw_md
        }
        form = EditEntryForm(initial=data)
        return render(request, "encyclopedia/edit_entry.html", {
            'form': form,
            'entry_name': entry
        })
    return HttpResponse('Sorry, couldnt find the page')

def random_page(request):
    entries = util.list_entries()
    total = len(entries)
    random = randint(0,total-1)
    return HttpResponseRedirect(reverse("entry_page", args = [entries[random]] ))