# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from .models import *
from django.shortcuts import render

# Create your views here.
def main(request):
    # 从页面读取用户输入的用户名和密码
    p_userName = request.POST.get('userNum')
    p_userPw = request.POST.get('userPw')

    stuList = User.objects.filter(userName=p_userName, userPw=p_userPw)
    if stuList:
        return render(request,'main.html')
    else:
        return render(request,'login.html')
    # # 从页面读取用户输入的用户名和密码
    # p_userName = request.POST.get('userNum')
    # p_userPw = request.POST.get('userPw')
    # print('asf')
    # # 从数据库读取用户名和密码（准备与页面输入输入的进行匹配）
    # user = User.objects.values('userName', 'userPw')
    # for i in user:
    #     userName = user[i]['userName']
    #     userPw = user[i]['userPw']
    #     if p_userName == userName and p_userPw == p_userPw:
    #         return render(request,'main.html')


def login(request):

    return render(request,'login.html')