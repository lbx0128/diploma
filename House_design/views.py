from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import User
from django.template import RequestContext


def index(request):
    limit = 10  # 每页显示的记录数
    user_list = User.objects.order_by("id")
    paginator = Paginator(user_list, limit)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    try:
        users = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        users = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        users = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render_to_response('index.html', {'users': users})


# 用户登录
def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        # 判断输入数据是否为空
        if name == '' or password == '':
            return render(request, "login.html", {"error": "用户名和密码不能为空"})
        else:
            user = User.objects.filter(name=name, password=password)
            if user:
                # 该函数用来重定向，登陆成功，跳转到index页面
                response = HttpResponseRedirect('../index')
                return response
            else:
                return render(request, "login.html", {"error": "用户名或密码错误"})
    else:
        return render_to_response('login.html')


def newuser(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST['role']

        if name == '' or password == '' or email == '':
            return render(request, "newuser.html", {"error": "请补全信息！"})
        else:
            user_list = User.objects.filter(name=name)
            if user_list:
                return render(request, "newuser.html", {"error": "用户已存在"})
            else:
                user = User()
                user.name = name
                user.password = password
                user.email = email
                user.role = role
                user.save()
                response = HttpResponseRedirect('../index')
                return response
    return render_to_response('newuser.html')
