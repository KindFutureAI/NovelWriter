from django_filters import FilterSet, filters
from app_main.models import UserInfo


class UserInfoFilter(FilterSet):
    """ 用户信息过滤器 """
    name = filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = UserInfo
        fields = ('username',)
