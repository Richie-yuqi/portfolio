from django.shortcuts import render,get_object_or_404

from .models import Blog
# Create your views here.

def blog(request):
	blogs = Blog.objects
	return render(request,'blog.html',{'blog':blogs})

def blog_text(request, blogid):
	blogpage = get_object_or_404(Blog,pk=blogid)
	return render(request,'blog_text.html',{'blogpage':blogpage})
	