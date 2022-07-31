from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogModel
from .forms import BlogForm

def bloglist(request):
    # bilgiler = [{'title': 'Blog Listesi', 'content': 'Blog Listesi'},{'title': 'Blog Listesi 2', 'content': 'Blog Listesi 2'}]
    bilgiler = BlogModel.objects.all()
    return render(request, 'blog/bloglist.html',{"bloglar":bilgiler})

def blogdetail(request,pk):
    blog = get_object_or_404(BlogModel,pk=pk) # getting from database with pk => primary key
    return render(request, 'blog/blogdetail.html',{"blog":blog})


def blogadd(request):
    # form = BlogForm()
    # return render(request, 'blog/blogadd.html',{"form":form})
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloglist')
    else:
        form = BlogForm()
    return render(request, 'blog/blogadd.html',{"form":form})

def blogedit(request,pk):
    blog = get_object_or_404(BlogModel,pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('bloglist')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blogadd.html',{"form":form})