
from markdown2 import Markdown
from webbrowser import get
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from . import util
import random

def to_index(request):
    return HttpResponseRedirect(reverse('index'))
def index(request):
    if request.method == "POST":
        title= request.POST["pageName"]
        content = request.POST["info"]
        util.save_entry(title, content)
        return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

    if request.method == "GET" and 'q' in request.GET:
        return HttpResponseRedirect(reverse("page",args=(request.GET.get('q', None),)))
    else: 
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request, page):

    page_finder  = util.get_entry(page)
    if request.method == "POST" and "info" in request.POST:
        util.save_entry(page,request.POST['info'])
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
                "pageName" : "NOTFOUND",
                "not_found" : True
            }) 
def create_page_view(request):
    return render(request,"encyclopedia/create.html")

def edit_page_view(request, pageName):
    entry = util.get_entry(pageName)
    return render(request,"encyclopedia/edit.html", {"pageName":pageName,"page":entry})
def random_view(request):
    list_of_entires = util.list_entries()
    random_ent = random.randrange(len(list_of_entires))
    return HttpResponseRedirect(reverse("page",args=(list_of_entires[random_ent],)))
    


    

