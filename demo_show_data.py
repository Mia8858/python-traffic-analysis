import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mysite.models import Post
from django.core.paginator import Paginator
#=============================================================================#
# 添加一筆資料
# post = Post.objects.create(title="文章標題", slug="px", body='文章內容')
# post.save()

posts = Post.objects.all()

print(f'\nPost class 內資料: {posts}')


p = Paginator(posts, 20)

print(f'\n Paginator(posts, 20) {p}')

for i, post in enumerate(posts[:20]):
    #print(f'\n第 {i} 筆 Post 資料')
    print(f'{i} 事故時間: {post.K_time} 發生地點: {post.K_location} 死亡人數: {post.K_death} 受傷人數: {post.K_injure}')
#print('\n')

#    K_time = models.CharField(max_length=200)
#    K_location = models.CharField(max_length=200)
#    K_death = models.CharField(max_length=200)
#    K_injure = models.CharField(max_length=200)