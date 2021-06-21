from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render


def index(request, name=""):
	
<<<<<<< HEAD
	posts = Post.objects.all()

=======
>>>>>>> 2c6c20248e88aecd53c4077053a7463be25bec85
	myname = "高雄市交通資料庫"

	target = Post.objects.order_by("-K_time")

	if request.method == 'POST':
		#這是從表單來的請求
		district = request.POST["items"]

		target = Post.objects.filter(K_location__contains=district).order_by("-K_time")

	
	return render(request, 'index.html', locals())	


def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

<<<<<<< HEAD
def listing(request):
	target = Post.objects.all()

	p = Paginator(target, 20)
	page_num = request.GET.get('page', 1)
	page = p.page(page_num)

	context = {'target' : page}

	return render(request, 'list.html', context)	
=======
>>>>>>> 2c6c20248e88aecd53c4077053a7463be25bec85
