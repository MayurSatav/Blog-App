from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author':'Mayur',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'March 1, 2020'

    },
    {'author':'Mayur',
        'title':'Blog Post 1',
        'content':'second Post Content',
        'date_posted':'March 2 , 2020'
    }
]
# Create your views here.
def home(request):
    context ={
        'posts':posts
    }
    #return HttpResponse('<h1>hello this is home page</h1>')
    return render(request,'blog/home.html',context)
    
def about(request):
    #return HttpResponse('<h1>hello this is about page</h1>')
    return render(request,'blog/about.html',{'title':'About'})