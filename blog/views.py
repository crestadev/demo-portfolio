from django.shortcuts import render, get_object_or_404
from .models import BlogPost
import markdown

def blog_list(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.content_html = markdown.markdown(
        post.content,
        extensions=['fenced_code', 'codehilite', 'tables', 'toc']
    )
    return render(request, 'blog/blog_detail.html', {'post': post})
