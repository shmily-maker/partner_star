from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

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