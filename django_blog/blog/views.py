from django.shortcuts import render

posts = [
    {
        "author": "Joe",
        "title": "blog post one",
        "content": "first post content",
        "date_posted": "28th January 2024"
    },
    {
        "author": "Joe 2",
        "title": "blog post two",
        "content": "Second post content",
        "date_posted": "29th January 2024"
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, "blog/home.html",  context)

def gallery(request):
    return render (request, "blog/gallery.html")