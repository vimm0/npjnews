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
from django.conf import settings

from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.news.models import Category, Reporter, Publication, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    reporter = ReporterSerializer(many=False)
    publications = PublicationSerializer(many=True)
    date_url = serializers.SerializerMethodField('date_man')

    def date_man(self, obj):
        return str(obj.created.year) + '-' + str(obj.created.month) + '-' + str(obj.created.day)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'reporter', 'publications', 'category', 'created', 'modified', 'date_url')


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    lookup_field = 'slug'


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    lookup_field = 'slug'


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['get'], detail=False)
    def breaking_news(self, request):
        try:
            queryset = Article.objects.filter(category__title='Breaking News')
            data = ArticleSerializer(queryset, many=True, context={'request': request}).data
            return Response(data)
        except:
            return Response(None)

    @action(methods=['get'], detail=False)
    def international_news(self, request):
        try:
            queryset = Article.objects.filter(category__title='International News')
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

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns = [
#                       url(r'^__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
