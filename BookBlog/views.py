from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import FollowerForm


class SignUpView(generic.CreateView):
    form_class = FollowerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class PostList(generic.ListView):
   # queryset = Post.objects.filter(status=1).order_by('-created_on')
   # template_name = 'posts.html'



#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'
