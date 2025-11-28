from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer
from categories.models import Category 


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'category', 'category_id', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')