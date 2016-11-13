# coding=utf-8
import json

from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .models import Root, Meaning, Word

__author__ = 'peter'

type_options = [
    {
        "text": "Prefix",
        "value": "prefix",
    },
    {
        "text": "Root",
        "value": "root",
    },
    {
        "text": "Suffix",
        "value": "suffix",
    }
]


# 添加前缀
def add(request):
    if request.POST:
        # 添加前缀
        root = Root.add(request)
        if not root:
            return redirect("word:add")
        # 添加前缀的意思和例词
        Meaning.add(request, root)
        return redirect("word:all")
    ctx = {
        "type_options": type_options,
        "default_type": request.GET.get("type", "prefix")
    }
    ctx.update(csrf(request))
    return render(request, 'root/add.html', ctx)


def edit(request, id):
    root = Root.get(id)
    ctx = {
        "type_options": type_options,
        "default_type": root.type,
        'root': root,
    }
    ctx.update(csrf(request))
    return render(request, 'root/edit.html', ctx)


# 显示所有词根
def list(request):
    type = request.GET.get("type", "prefix")
    letter = request.GET.get("letter", None)
    ctx = {
        'type': type,
        'curLetter': letter,
        'letters': Root.getLetters(type),
        'rootJsons': Root.as_jsons(type),
        'roots': Root.getAll(type, letter),
        'all_url': reverse("word:list") + '?type=' + type,
    }
    return render(request, "root/list.html", ctx)


def meaningTemplate(request):
    return render(request, 'root/meaningTemplate.html',
                  {
                      'index': request.GET.get('index', '0'),
                  })


def wordTemplate(request):
    return render(request, 'root/wordTemplate.html',
                  {
                      'meaningIndex': request.GET.get('meaningIndex', '0'),
                      'wordIndex': request.GET.get('wordIndex', '0'),
                  })


def rootJSON(request, id):
    root = Root.get(id)
    data = root.as_json()
    return HttpResponse(json.dumps(data), content_type='application/json')


def rootsJSON(request):
    data = []
    roots = Root.getAll()
    for root in roots:
        data.append(root.as_json())
    return HttpResponse(json.dumps(data), content_type='application/json')
