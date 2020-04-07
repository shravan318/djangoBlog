from django.shortcuts import render


posts = [
    {
        "author" : "Corey",
        "title" : "blog post 1",
        "content": "adhdh kjshdkjas djhs dasjdhas ddhkjsd sdajd hd",
        "posted_on": "Aug 15, 2018"
    },
       {
        "author" : "jane",
        "title" : "blog post 2",
        "content": "adhdh kjshdkjas djhs dasjdhas ddhkjsd sdajd hd",
        "posted_on": "Jan 15, 2019"
    },
]

# Create your views here.

def home(request):
    context ={
        "posts": posts
    }
    return render(request,"blog/home.html", context )



def about(request):
    return render(request, "blog/about.html", {"title" : "about the blog"})