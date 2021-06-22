from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def index(request, name=""):
    posts = Post.objects.all()
    p = Paginator(posts, 20)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    myname = "高雄市交通資料庫"
    if request.method == 'POST':
        # 這是從表單來的請求
        district = request.POST["items"]
        target = Post.objects.filter(K_location__contains=district)
    return render(request, 'index.html', locals())


def myindex(request, city=""):
    myname = "高雄市交通資料庫"
    citys = ['岡山區', '燕巢區', '楠梓區', '橋頭區', '左營區', '鼓山區', '三民區', '苓雅區', '新興區', '前金區', '鹽埕區', '前鎮區', '旗津區', '小港區', '鳳山區', '茂林區', '甲仙區',
             '六龜區', '杉林區', '內門區', '美濃區', '仁武區', '田寮區', '旗山區', '梓官區', '阿蓮區', '湖內區', '茄萣區', '路竹區', '鳥松區', '永安區', '燕巢區', '大樹區', '大社區', '彌陀區']
    try:
        posts = Post.objects.all()
        target = Post.objects.filter(K_location__contains=city)  # 篩選鄉鎮市

        paginator = Paginator(target, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        count = paginator.count
        num_pages = paginator.num_pages

        return render(request, "myindex.html", locals())
    except:
        return redirect("/")


def show(request, id):
    try:
        target = Post.objects.get(id=id)
    except:
        return redirect("/")
    return render(request, "showpost.html", locals())
