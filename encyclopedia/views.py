from django.shortcuts import render
from django.http import HttpResponse #Delete this later when no longer needed
from . import util
from markdown2 import Markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry):
    markdowner = Markdown()
    raw_md = util.get_entry(entry)
    if raw_md:
        html_entry = markdowner.convert(raw_md)
        return HttpResponse(html_entry)
    else:
        return HttpResponse("Not found, bro")