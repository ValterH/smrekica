from django.shortcuts import render
#from django.http import HttpResponse

# izpiši spletno stran home/home.html (v mapi templates)

def index(request):
    #return HttpResponse("<h2>Hello World!<h2>")
    return render(request, 'home/home.html') 
