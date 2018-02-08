from django.urls import path
from QueAns import views

urlpatterns = [
    path('/upvote/', views.upvote, name="upvote"),
    path('/downvote/', views.downvote, name="downvote"),
    path('/satisfied/', views.satisfied, name="satisfied"),
    path('/disatisfied/', views.disatisfied, name="disatisfied"),
]
