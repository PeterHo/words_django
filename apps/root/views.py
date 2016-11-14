# coding=utf-8
import json

from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.template.loader import render_to_string

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
        return redirect(reverse("word:all") + '?type=' + root.type)
    ctx = {
        "type_options": type_options,
        "default_type": request.GET.get("type", "prefix"),
        "list_url": reverse("word:list")
    }
    ctx.update(csrf(request))
    return render(request, 'root/add.html', ctx)


def edit(request, id):
    root = Root.get(id)
    if request.POST:
        root.delete()
        # 添加前缀
        root = Root.add(request)
        # 添加前缀的意思和例词
        Meaning.add(request, root)
        return redirect(reverse("word:all") + '?type=' + root.type)
    ctx = {
        "type_options": type_options,
        "default_type": root.type,
        'root': root,
        'rootJson': root.as_json(),
        "list_url": reverse("word:list")
    }
    ctx.update(csrf(request))
    return render(request, 'root/edit.html', ctx)


# 显示所有词根
def list(request):
    type = request.GET.get("type", "prefix")
    ctx = {
        'type': type,
        'letters': Root.getLetters(),
        'rootsJson': Root.as_jsons(),
        'roots': Root.getAll(),
        "list_url": reverse("word:list"),
        'add_url': reverse("word:add"),
        'edit_url': reverse("word:edit", kwargs={'id': '123456'}),
    }
    return render(request, "root/list.html", ctx)


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
