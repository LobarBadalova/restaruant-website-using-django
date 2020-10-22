from django.shortcuts import render
from meals.models import Category, Meals
from blog.models import Post
# Create your views here.
def home(request):
	meal_list=Meals.objects.all()
	category=Category.objects.all()
	posts=Post.objects.all()
	context={"meal_list":meal_list,
	"category":category,
	'posts':posts}

	return render(request, 'home/index.html', context)