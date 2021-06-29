from django.contrib import admin
from django.urls import path ,include
from .views import ArticleViewSet ,UserViewSet
from rest_framework.routers import DefaultRouter

#from .views import posts ,postsDetail
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)
urlpatterns = [
    path('api/',include(router.urls))
    #path('posts/', Articlelist.as_view()),
    #path('posts/<int:id>/', ArticleDetail.as_view()),
]
