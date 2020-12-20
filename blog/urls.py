from django.urls import path
from . import views 
app_name='blog'

urlpatterns = [
    path('',  views.post_list, name='post_list'),
    path('<int:id>',  views.post_detail, name='post_detail'),
    path('about_us/',  views.about_us, name='about_us'),
    path('summernote/', include('django_summernote.urls')),
    


]
