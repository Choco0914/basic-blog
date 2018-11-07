from django.shortcuts import render
from . models import Article, Comment, HashTag

def index(request):
    """index page를 load한다"""
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtags = HashTag.objects.all()

    if not category and not hashtag:
        articles = Article.objects.all()
    elif category:
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.filter(hashtag__name=hashtag)


    # categories = set([])
    # for article in articles:
    #     categories.add(article.get_category_display())
        # print(categories)


    # categories = set([
    #     article.get_category_display()
    #     for article in articles
    # ])

    categories = set([
        (article.category, article.get_category_display())
        for article in articles
    ])

    context = {'articles':articles,
     'hashtags': hashtags,
     'categories':categories,
     }

    return render(request, "feed/index.html", context)


def detail(request, article_id):
    """글을 분리해서 보여준다"""
    article = Article.objects.get(id=article_id)
    hashtags = HashTag.objects.all()

    context = {
        'article':article,
        'hashtags':hashtags
    }
    return render(request, "feed/detail.html", context)
