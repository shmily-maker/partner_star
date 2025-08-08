from django.shortcuts import render, redirect  # 包含 redirect 用于重定向
from django.contrib.auth import authenticate, login  # 用于用户认证和登录
from django.contrib import messages  # 用于显示错误消息
from django.contrib.auth.forms import AuthenticationForm  # 正确导入登录表单类
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User  # 添加User模型导入
from .forms import RegisterForm  # 导入注册表
def home(request):
    """首页视图"""
    # 可以传递数据到模板
    context = {
        'title': '欢迎来到我的网站',
        'message': '这是一个基于Django的Web页面示例',
        'features': ['简单易用', '高效稳定', '安全可靠']
    }
    return render(request, 'home.html', context)

def about(request):
    """关于页面视图"""
    context = {
        'title': '关于我们',
        'content': '我们致力于提供高质量的Web开发服务',
        'team': [
            {'name': '张三', 'position': '开发者'},
            {'name': '李四', 'position': '设计师'},
            {'name': '王五', 'position': '产品经理'}
        ]
    }
    return render(request, 'about.html', context)
def user_login(request):
    # 打印用户状态和用户名
    print("用户是否已登录:", request.user.is_authenticated)
    print("当前用户名:", request.user.username)  # 匿名用户会显示 "AnonymousUser"
    # 如果用户已登录，直接重定向到首页
    if request.user.is_authenticated:
        return redirect('home')

    # 实例化表单（GET请求显示空表单，POST请求验证数据）
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                next_page = request.GET.get('next')
                return redirect(next_page or 'home')
            else:
                messages.error(request, '用户名或密码不正确')
    else:
        form = AuthenticationForm()  # GET请求：实例化空表单

    # 关键：将form变量传递给模板
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)  # 清除用户会话
    return redirect('home')  # 退出后重定向到首页


def register(request):
    """用户注册视图"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # 创建用户（这里需要用到User模型）
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # 注册后自动登录
            login(request, user)
            messages.success(request, f'注册成功！欢迎 {username}')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})