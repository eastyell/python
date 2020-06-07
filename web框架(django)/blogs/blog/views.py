from django.shortcuts import render
import markdown
# Create your views here.
import blog.models as m

# 查询
# models.UserInfo.objects.all()
# models.UserInfo.objects.all().values('user')    #只取user列
# models.UserInfo.objects.all().values_list('id','user')    #取出id和user列，并生成一个列表
# models.UserInfo.objects.get(id=1)
# models.UserInfo.objects.get(user='yangmv')

# 增
# models.UserInfo.objects.create(user='yangmv',pwd='123456')
# 或者
# obj = models.UserInfo(user='yangmv',pwd='123456')
# obj.save()
# 或者
# dic = {'user':'yangmv','pwd':'123456'}
# models.UserInfo.objects.create(**dic)

# 删
# models.UserInfo.objects.filter(id=1).delete()

# 改
# models.UserInfo.objects.filter(user='yangmv').update(pwd='520')
# 或者
# obj = models.UserInfo.objects.get(user='yangmv')
# obj.pwd = '520'
# obj.save()
def index(request):
    i = request.GET.get('id')
    # postdata = request.POST['id']
    blog = m.Blog.objects.get(id=i)
    blog_content = markdown.markdown(blog.content)
    return render(request, "blog.html", {'blog': blog, 'blog_content': blog_content})

# render(request, template_name[, context]） 将指定页面渲染后返回给浏览器

def indexes(request):
    blogs = m.Blog.objects.all()
    return render(request, "blogs.html", {'blogs': blogs})

def hello(request):
    # blogs = m.Blog.objects.all()
    # return render(request, "blogs.html", {'blogs': blogs})
    return render(request, "hello.html", {'blogs': 'Leo'})

def query(request):
    blog_index = m.Blog.objects.all().order_by('-id')#从数据库中取出文章数据
    print(request.body)
    context = {
        'blog_index':blog_index,#将数据保存在blog_index
    }
    return render(request, 'hello.html',context)#通过render进行模板渲染