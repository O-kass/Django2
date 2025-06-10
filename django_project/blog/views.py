from django.shortcuts import render
from django.template.context_processors import request

posts = [
    {
        'author': 'OmarMK',
        'title': "BlogPost_1",
        'content': 'TEST1- If you can see this message the test blog is up and works',
        'date': "09/06/25",
    },
    {
        'author': 'OmarMK',
        'title': "BlogPost_2",
        'content': 'TEST2- If you can see this message multiple blogs can be seen at once',
        'date': "09/06/25",
    },

]



# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "ABOUT PAGE"})