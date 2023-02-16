from django.http import HttpResponse
from django.shortcuts import render

def ram(request):
    return render(request, "countwords.html")

def count(request):
    mass=request.GET['message']
    wl=mass.split()
    #print(wl)
    wlcounnt={}
    for word in wl:
        if word in wlcount:
            wlcount[word] += 1
        else:
            wlcounnt[word]=1
    sort1=sorted(wlcounnt.items(),key=operateor.itemgetter(1),reverse=True)


    return render(request, "count.html",{"msg":mass,"length":len(wl),"abc":wlcounnt, 'cba':sort1})

#def wel(request):
#    return HttpResponse("<h3>traning<h3>")