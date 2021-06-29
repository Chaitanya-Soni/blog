from django.http import JsonResponse
from .models import BlogArticle
from .serializers import BlogArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

""" class ArticleViewSet(viewsets.ViewSet):

    def list(self, request):
        articles = BlogArticle.objects.all()
        serializer = BlogArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = BlogArticle.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = BlogArticleSerializer(article)
        return Response(serializer.data)


    def update(self, request, pk):
        article = BlogArticle.objects.get(pk=pk)

        serializer = BlogArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        article = BlogArticle.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """""" class Articlelist(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class ArticleDetail(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin ,):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer
    lookup_field= "id"
    def get(self,request,id):
        return self.retrieve(request,id=id)
    def post(self,request,id):
        return self.create(request,id=id)
    def update(self, request,id):
        return self.update(request,id=id)
    def delete(self, request,id):
        return self.destroy(request,id=id)
 """
""" class Articlelist(APIView):
    def get(self,request):
        articles = BlogArticle.objects.all()
        serializer = BlogArticleSerializer(articles,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data= request.data
        serializer = BlogArticleSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
 """
""" class ArticleDetail(APIView):
    def get_object(self,id):
        try :
            articles = BlogArticle.objects.get(id=id)
            return articles
        except :
            return "NOT FOUND"

    def get(self,request,id):
        articles=self.get_object(id)
        if(articles!="NOT FOUND"):
            serializer = BlogArticleSerializer(articles)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    def post(self,request,id):
        articles=self.get_object(id)
        serializer = BlogArticleSerializer(articles ,data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        articles=self.get_object(id)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  """
# Create your views here.
""" @api_view(['GET','POST'])
def posts(request):
    if(request.method=='GET'):
        articles = BlogArticle.objects.all()
        serializer = BlogArticleSerializer(articles,many=True)
        return Response(serializer.data)
    if(request.method=='POST'):
        data= request.data
        serializer = BlogArticleSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def postsDetail(request,pk):
    if(request.method=='GET'):
        try :
            articles = BlogArticle.objects.get(pk=pk)

        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogArticleSerializer(articles)
        return Response(serializer.data)
    if(request.method=='PUT'):
        try :
            articles = BlogArticle.objects.get(pk=pk)

        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogArticleSerializer(articles ,data= request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    if(request.method=='DELETE'):
        try :
            articles = BlogArticle.objects.get(pk=pk)

        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """