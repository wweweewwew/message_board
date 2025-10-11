from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Posts
from .forms import PostForm

class HomepageView(ListView):
	model = Posts
	template_name = "home.html"

class PostCreateView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home')