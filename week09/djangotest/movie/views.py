from django.http import HttpResponse
from django.shortcuts import render
from .models import movieinfo
from django.db.models import Avg
#后台管理系统用到的包
from .form import LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

def movie_short(request):
    short = movieinfo.objects.all()

    #评论数量
    counter = short.count()
    # 提取评分三星以上的作为好评
    condtions = {'star__gte': 4.0}
    star_avg = f" {movieinfo.objects.aggregate(Avg('score'))['score__avg']:0.1f}"
    # 情感倾向
    sent_avg = f" {movieinfo.objects.aggregate(Avg('score'))['score__avg']:0.2f}"
    #正向评价星级标准 0.6
    queryset  = movieinfo.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.6}
    #过滤取值大于= 0.6
    plus = queryset.filter(**condtions).count()
    #负向评论
    condtions = {'sentiment__lt': 0.6}
    # 过滤
    minus = queryset.filter(**condtions).count()
    return render(request, 'result.html', locals())

def login2(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])
            if user:
                login(request,user)
                return render(request, 'result.html', locals())
            else:
                return HttpResponse('登录失败,请从新输入')


    if request.method == 'GET':
        loginform = LoginForm()
        return  render(request,'wetest.html',{'form':loginform})


