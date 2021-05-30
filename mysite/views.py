from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post

def index(request):
	posts = Post.objects.all()
	myname = "高雄市交通資料庫"
	
	return render(request, 'index.html', locals())

def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())


