from django.urls import path

from blog1.feeds import AllPostsRssFeed
from . import views

app_name = 'blog1'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('posts/<int:pk>', views.detail, name='detail'),
#     path('archives/<int:year>/<int:month>/', views.archive, name='archive'),  # 归档，视图在inclusions->_archive
#     path('categories/<int:pk>/', views.category, name='category'),
#     path('tags/<int:pk>/', views.tag, name='tag'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archives'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    # 记得在顶部引入 AllPostsRssFeed
    path('all/rss/', AllPostsRssFeed(), name='rss'),
    path('search/', views.search, name='search'),
]