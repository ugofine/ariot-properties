from django.shortcuts import render
from .models import Blog, Comment
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog(request):
    blogs =Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})

def blog_detail(request, id):
    blog =Blog.objects.get(id=id)
    #adding comment below

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                blog=blog
            )
            comment.save()
            comment= CommentForm()
            messages.success(request, 'Comment is successfully added')

        else: 
            form = CommentForm()
    else:
        form = CommentForm()

    comments = Comment.objects.filter(blog=blog)
    context = {
        "blog": blog,
        "comments": comments,
        "form": form,

    }   
    #if you as passing several things you can wrap them up in the function and pass the function itself 

    return render(request, 'blog/blog_detail.html', context)

def search(request):
    bloglist = blog.objects.all

    #for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            bloglist = bloglist.filter(description__icontains=keywords)

    return render(request,'blog/search.html' , {'bloglist' : bloglist})
