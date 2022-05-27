
from markdown2 import Markdown

from webbrowser import get
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from . import util


def index(request):
    if request.method == "GET" and 'q' in request.GET:
        return HttpResponseRedirect(reverse("page",args=(request.GET.get('q', None),)))
    else: 
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request, page):
    page_finder  = util.get_entry(page)
    if request.method == "GET" and 'q' in request.GET:
        q = request.GET.get('q', None)
        if q is not None:
            print(request.GET['q'])
            return HttpResponseRedirect(reverse("page",args=(request.GET['q'],)))

    elif(page_finder):
        markdowner = Markdown()
        
        return render(request,"encyclopedia/page.html", {
                "page":markdowner.convert(page_finder),
                "pageName":page
            }) 
    else:
        return render(request,"encyclopedia/page.html", {
                "page": "Page wasn't found",
                "pageName" : "NOTFOUND"
            }) 
    

