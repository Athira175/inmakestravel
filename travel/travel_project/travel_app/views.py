from django.shortcuts import render

from .models import dress, jewellery
from .models import electronic
# Create your views here.
def demo(request):
    obj=dress.objects.all()
    obj1=electronic.objects.all()
    obj2=jewellery.objects.all()
    return render(request,"index.html",{'result':obj,'r1':obj1,'r2':obj2})



