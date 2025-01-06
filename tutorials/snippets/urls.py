from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets.views import api_root, SnippetViewSet, UserViewset

    # url patterns while using function based views.
    
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    
    # url patterns while using class based views.

snippet_list = SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })
snippet_detail = SnippetViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
snippet_highlight = SnippetViewSet.as_view(
        {
        'get': 'highlight'
        },
        renderer_classes=[renderers.StaticHTMLRenderer])
    
user_list = UserViewset.as_view({
        'get': 'list'
    })
user_detail = UserViewset.as_view({
        'get': 'retrieve'
    })


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
])