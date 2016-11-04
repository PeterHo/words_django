# coding=utf-8
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .models import Prefix, Meaning, Word

__author__ = 'peter'


# 添加前缀
def add(request):
    if request.POST:
        # 添加前缀
        prefix = Prefix.add(request)
        if not prefix:
            return redirect("prefix:add")
        # 添加前缀的意思和例词
        Meaning.add(request, prefix)
        return redirect("prefix:all")
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'prefix/add.html', ctx)


def list(request, letter=None):
    ctx = {
        'curLetter': letter,
        'letters': Prefix.getLetters(),
        'prefixes': Prefix.getAll(letter),
    }
    return render(request, "prefix/list.html", ctx)


def meaningTemplate(request):
    return render(request, 'prefix/meaningTemplate.html',
                  {
                      'index': request.GET.get('index', '0'),
                  })


def wordTemplate(request):
    return render(request, 'prefix/wordTemplate.html',
                  {
                      'meaningIndex': request.GET.get('meaningIndex', '0'),
                      'wordIndex': request.GET.get('wordIndex', '0'),
                  })
