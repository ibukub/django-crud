from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.list import ListView
from .models import Post

class PostListView(ListView):
    model = Post

from django.views.generic.edit import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'

success_url  =  reverse_lazy('blog:all')   

from django.views.generic.detail import DetailView
from .models import Post

class PostDetailView(DetailView):

    model = Post
    fields = '__all__'

success_url  =  reverse_lazy('blog:all')   

from django.views.generic.edit import UpdateView
from .models import Post

class PostUpdateView(UpdateView): 
    model = Post
    fields = '__all__'

success_url  =  reverse_lazy('blog:all') 

from django.views.generic.edit import DeleteView
from .models import Post

class PostDeleteView(DeleteView): 
    model = Post
    fields = '__all__'

success_url  =  reverse_lazy('blog:all') 
