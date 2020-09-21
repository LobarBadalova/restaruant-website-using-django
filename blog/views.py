from django.shortcuts import render
from .models import Post, Category, Comments
from .forms import CommentForm

# Create your views here.
def post_list(request):
	posts=Post.objects.all()
	category=Category.objects.all()
	context={'posts':posts, 'category':category}
	return render(request, 'Blog/post_list.html', context)

def post_detail(request, id):
	post_detail=Post.objects.get(id=id)
	category=Category.objects.all()
	comments=Comments.objects.filter(post=post_detail)
	comment_form=CommentForm()

	if request.method=="POST":
		comment_form=CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment=comment_form.save(commit=False)
			new_comment.user=request.user
			new_comment.post=post_detail
			new_comment.save()

	else:
		comment_form=CommentForm()
	context={'post_detail':post_detail,
			'category':category,
			'comments':comments,
			'comment_form':comment_form
	}
	return render(request, 'Blog/post_detail.html', context)