from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse,Http404

# Create your views here.
def home(request):
    article_list=Article.objects.all()
    return render(request,'home.html',{'article_list':article_list})

def article_detail(request,title):
    try:
        article=Article.objects.get(title=str(title))
    except Article.DoesNotExist:
        raise Http404("Article Does not Exist !")
    return render(request,'article.html',{'article':article})

def article_category(request,category):
    try:
        article_list=Article.objects.filter(category=category)
        tag=category
    except Article.DoesNotExist:
        raise Http404("Article Does not Exist !")
    return render(request,'category.html',{'article_list':article_list,'tag':tag})

def article_search(request):
    if 's' in request.GET:
        s=request.GET['s']
        if s is None:
            return render(request,'home.html')
        else:
            article_list1=Article.objects.filter(title__icontains=s)
            search1="标题中包含该字段的文章"
            article_list2=Article.objects.filter(content__icontains=s)
            search2="内容中包含该字段的文章"
            return render(request,'search.html',{'article_list1':article_list1,'article_list2':article_list2,'search1':search1,'search2':search2})

def guidang(request):
    article_list=Article.objects.all()
    categories=[]
    article_lists=[]
    tags=[]
    for article in article_list:
        if article.category not in categories:
            categories.append(article.category)

    for category in categories:
        article_list=Article.objects.filter(category__iexact=category)
        tags.append(category)
        article_lists.append(article_list)
    return render(request,'guidang.html',{'article_lists':article_lists,'tags':tags})

def test(request):
    return HttpResponse("wwwwwwwww")



