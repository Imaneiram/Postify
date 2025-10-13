from django.shortcuts import render

posts=[
    { 
        'author':'iramdane imane ',
        'title':"post 1 ",
        'content':'keep trying',
        'date':' october 12 2025'
    },
    { 
        'author':'ename',
        'title':'post 2',
        'content':'enjoy the journey',
        'date':' october 12 2025' 
    },   
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'posts/home.html',context)

def about(request): 
    return render(request,'posts/about.html',{'title':'About'})