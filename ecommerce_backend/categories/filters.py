import django_filters
from .models import Category


class CategoryFilter(django_filters.FilterSet):
    alphabetical = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    reverse_alphabetical = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    category = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Category
        fields = ['category', 'alphabetical', 'reverse_alphabetical']