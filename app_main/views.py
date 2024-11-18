from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from app_main.models import UserInfo
from app_main.serializer import UserInfoSerializer
from app_main.filter import UserInfoFilter

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Article
# from .serializer import ArticleSerializer


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)


# class ArticleListAPIView(APIView):
#     # rest api 示例
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 

def index(request):
    return render(request, 'index.html')


 
def room(request, group_num):
    """ 聊天室: 使用websocket 连接 """
    return render(request, 'socket_index.html', {
        "group_num": group_num
        })