from rest_framework import viewsets, permissions, filters, generics
#from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
#from .filters import CategoryFilter
#from .pagination import StandardResultsSetPagination
#from rest_framework.permissions import IsAdminUser
#from rest_framework.filters import OrderingFilter
#from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    #def get_permissions(self):
        #if self.action in ['create', 'update', 'partial_update', 'destroy']:
            #return [IsAdminUser()]
        #return [permissions.AllowAny()]

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]
