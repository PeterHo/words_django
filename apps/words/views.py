# coding=utf-8

from django.shortcuts import render, redirect

__author__ = 'peter'


def home(request):
    return render(request, "words/home.html")
