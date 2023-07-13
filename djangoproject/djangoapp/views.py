from django.shortcuts import render
from django.http import HttpResponse
from.models import flower

def demo(request):
    obj=flower.objects.all()
    return render(request,"index.html",{'result':obj})


#def operation(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
  #  sum=x+y
   # division=x/y
    #mul=x*y
    #sub=x-y

 #   return render(request,"result.html",{'add':sum,'div':division,'mult':mul,'subt':sub})
# Create your views here.
