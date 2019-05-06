from django.shortcuts import render
from blog.models import BlogPost

def blog(request):
    posts=BlogPost.objects.all()
    c={}
    c['posts']=posts
    return render(request,'blog.html',c)
