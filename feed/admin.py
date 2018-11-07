from django.contrib import admin
from . models import Article, Comment, HashTag

@admin.register(Article, Comment, HashTag)
class FeedAdmin(admin.ModelAdmin):
    """admin site에 모델을 등록해준다."""
    pass
