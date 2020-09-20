from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def post_list(request):
	posts=Post.objects.all()
	category=Categorcy.objects.all()
	context={'posts':posts, 'category':category}
	return render(request, 'Blog/post_list.html', context)

def post_detail(request, id):
	post_detail=Post.objects.get(id=id)
	category=Category.objects.all()
	context={'post_detail':post_detail,
			'category':category,
	}
	return render(request, 'Blog/post_detail.html', context)