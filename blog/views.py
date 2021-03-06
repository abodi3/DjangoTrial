
from django.shortcuts import render
from .models import Post 
from django.views.generic import (ListView, 
	DetailView, 
	CreateView)

# Create your views here.


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

def meal(request):
	return render(request, 'blog/meal.html', {'title':'Meal'})



class PostListView(ListView):
	model = Post

	template_name = 'blog/home.html'

	context_object_name ='posts'

	ordering = ['-date_posted']



class PostDetailView(DetailView):
	model = Post

	
class PostCreateView(CreateView):
	model = Post

	fields = ['title', 'content']
