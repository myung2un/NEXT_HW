from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':

        print(request.POST, '확인') #POST 요청으로 온 데이터 확인하기 위해 출력

        new.article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],            
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()

    hobbies = Article.objects.filter(category='hobby')
    hobbies_num = hobbies.count()

    foods = Article.objects.filter(category='food')
    foods_num = foods.count()

    programmings = Article.objects.filter(category='programming')
    programmings_num = programmings.count()

    return render(request, 'list.html', {'articles':articles, 'hobbies_num': hobbies_num, 'foods_num': foods_num, 'programmings_num': programmings_num})

def detail(request, article_id):
    detail = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'detail': detail,})

def category(request, category):
    category_articles =Article.objects.filter(category=category)
    return render(request, 'category.html', {'category_name':category,'category_articles': category_articles})
