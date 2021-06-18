from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post

def index(request, name=""):
	posts = Post.objects.all()
	myname = "高雄市交通資料庫"
	if request.method == 'POST':
		#這是從表單來的請求
#		items = int(request.POST["items"])

		district = request.POST["district"]
		target = Post.objects.filter(K_location__contains=district)

#		if target != None:
#			if items == 0:
#				cities = City.objects.filter(country=target).order_by("population")
#			else:	
#				cities = City.objects.filter(country=target).order_by("population")[:items]
#		else:
#			if items == 0:
#				cities = City.objects.all().order_by("-population")
#			else:
#				cities = City.objects.all().order_by("-population")[:items]

	return render(request, 'index.html', locals())	


def show(request, id):
	try:
		target = Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())


