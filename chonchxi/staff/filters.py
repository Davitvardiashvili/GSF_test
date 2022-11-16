import django_filters

from .models import *


class Orderfilter(django_filters.FilterSet):
    class Meta:
        model = Competitor
        fields = ['year', 'gender', 'school']


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = '__all__'


class ShakeFilter(django_filters.FilterSet):
    class Meta:
        model = Shake
        fields = '__all__'
