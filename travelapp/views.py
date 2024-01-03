from django.shortcuts import render,HttpResponse
from . models import Place,Team

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request,"index.html",{'result': obj,'members': team})



def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x+y
    prod = x*y
    diff = x - y
    div = x/y
    return render(request,"result.html",{
                                            'result': res,
                                            'difference':diff,
                                            'product':prod,
                                            'division':div,
                                         
                                         })

