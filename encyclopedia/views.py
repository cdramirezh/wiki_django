from django.shortcuts import render
from django.http import HttpResponse #Delete this later when no longer needed
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def test(request):
    markdowner = Markdown()
    route = '/home/higi/dev/edx/wiki/entries/HTML.md'
    with open(route, 'r') as file:
        data = file.read()
    test = markdowner.convert(data)
    return HttpResponse(test)