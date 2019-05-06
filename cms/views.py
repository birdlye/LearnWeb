from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from cms.models import Story,Category
from django.views import generic

# Create your views here.
def category(request,slug):
    category=get_object_or_404(Category,slug=slug)
    story_list=Story.objects.filter(category=category)
    heading='Category:%s' % category.label
    return render(request,'cms/story_list.html',locals())

def search(request):
    print('search')
    if 'q' in request.GET:
        term=request.GET['q']
        story_list=Story.objects.filter(Q(title__contains=term)|Q
                                        (markdown_content__contains=term))
        heading='Search results'
    return render(request,'cms/story_list.html',locals())


def story_detail(request,slug):
    print('abcd')
    story=get_object_or_404(Story,slug=slug)
    heading='Story:%s' % slug
    return render(request,'cms/story_detail.html',locals())

def story_list(request):
    story_list=Story.objects.all()
    return render(request,'cms/story_list.html',locals())