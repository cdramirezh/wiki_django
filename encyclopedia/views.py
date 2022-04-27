from django.shortcuts import render
from . import util
from markdown2 import Markdown

from django import forms

from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse


from . import util

class EntryForm(forms.Form):
    entry = forms.CharField()

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
            'name': entry
        })
    else:
        return render(request, "encyclopedia/not_found.html")
    
def test(request):
    if request.method == 'POST':
        entry = request.POST['q']
        clean_entry = ''.join(entry)
        return HttpResponseRedirect(reverse('entry_page', args = [entry] ))
    
    return HttpResponse('Not even a POST')
    