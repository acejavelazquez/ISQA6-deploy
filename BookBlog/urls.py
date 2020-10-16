from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('post_detail', views.PostDetail.as_view(), name='post_detail'),
]
