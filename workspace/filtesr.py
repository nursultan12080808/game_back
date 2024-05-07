import django_filters
from django import forms

from game_app.models import Game, Tag

class GameFilter(django_filters.FilterSet):
    tags_name = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), field_name='tag', widget=forms.CheckboxSelectMultiple(attrs={"class":"mb-10"}))
    date = django_filters.DateFromToRangeFilter()
    price = django_filters.RangeFilter()
    class Meta:
        model = Game
        fields = ['category', 'date','price']