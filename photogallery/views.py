from django.shortcuts import render
from .models import Photo,Item
# Create your views here.
def index(request):
    items=Item.objects.all()
    c={}
    c['items']=items
    return render(request,'index.html',c)