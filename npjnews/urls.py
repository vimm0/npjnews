"""npjnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path, include

from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.news.models import Category, Reporter, Publication, Article


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['get'], detail=False)
    def breaking_news(self, request):
        try:
            queryset = Article.objects.filter(category__pk=2)
            data = ArticleSerializer(queryset, many=True, context={'request': request}).data
            return Response(data)
        except:
            return Response(None)

    @action(methods=['get'], detail=False)
    def international_news(self, request):
        try:
            queryset = Article.objects.filter(category__pk=8)
            data = ArticleSerializer(queryset, many=True, context={'request': request}).data
            return Response(data)
        except:
            return Response(None)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('reporter', ReporterViewSet)
router.register('publication', PublicationViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url('froala_editor/', include('froala_editor.urls')),
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls'))
]
