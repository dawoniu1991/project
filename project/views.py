#coding=utf-8
from django.shortcuts import render


def left_view(request):
    return render(request,'left.html')


def top_view(request):
    return render(request,'top.html')


def center_view(request):
    return render(request,'center.html')


def down_view(request):
    return render(request,'down.html')