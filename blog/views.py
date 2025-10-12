from django.shortcuts import render, get_object_or_404
from .models import BlogPost
import markdown
from django.utils.html import strip_tags

def blog_list(request):
    posts = BlogPost.objects.order_by('-created_at')
    for post in posts:
        # Convert Markdown to HTML
        html_content = markdown.markdown(post.content, extensions=['fenced_code', 'tables'])
        # Strip HTML tags to create a plain-text excerpt
        post.excerpt = strip_tags(html_content)[:200]  # first 200 chars
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.content_html = markdown.markdown(
        post.content,
        extensions=['fenced_code', 'codehilite', 'tables', 'toc']
    )
    return render(request, 'blog/blog_detail.html', {'post': post})
