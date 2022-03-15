from django.urls import path
from news.views import *

app_name = "news"

urlpatterns = [
    path('news-image', NewsImageListCreateView.as_view()),
    path('news-image/all', NewsImageListView.as_view()),
    path('news-image/<pk>', NewsImageDetailView.as_view()),
    path('news-event', NewsEventListCreateView.as_view()),
    path('news-event/all', NewsEventListView.as_view()),
    path('news-event/<pk>', NewsEventDetailView.as_view()),
    path('comment', CommentListCreateView.as_view()),
    path('comment/all', CommentListView.as_view()),
    path('comment/<pk>', CommentDetailView.as_view()),
    path('reaction', ReactionListCreateView.as_view()),
    path('reaction/all', ReactionListView.as_view()),
    path('reaction/<pk>', ReactionDetailView.as_view()),
    path('share', ShareOnListCreateView.as_view()),
    path('share/all', ShareOnListView.as_view()),
    path('share/<pk>', ShareOnDetailView.as_view()),

]