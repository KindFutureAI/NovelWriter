from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_main.views import UserInfoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API平台",
        default_version="v1",
        description="接口文档",
        terms_of_service="",
        contact=openapi.Contact(email='2495128088@qq.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)


# 路由
router = DefaultRouter()
# 注册路由: userinfo 是路由的名字，UserInfoViewSet 是视图集，basename是路由的名字
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
    path("index/", views.index, name="index"),  # 一种方式
    path('', include(router.urls)),             # 第二种方式
    # 使用 swagger 生成api文档
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('chat/<int:group_num>/', views.room, name='room')
]
