# coding=utf-8
from django import template
from django.template.loader import render_to_string

__author__ = 'peter'

register = template.Library()


def render_template_file(file_name, ctx):
    template_file = "django2html/material_ui/%s.html" % file_name
    return render_to_string(template_file, context=ctx)


def getFullButtonColor(color):
    if not color.startswith('btn-'):
        color = 'btn-' + color
    return color


@register.simple_tag
def button(href, text, style, color, type="", extraClass=""):
    ctx = {
        'href': href,
        'text': text,
        'style': style,
        'color': color,
        'type': type,
        'extraClass': extraClass,
    }
    return render_template_file("button", ctx)


@register.simple_tag
def raisedBtn(href, text, color, type="", extraClass=""):
    return button(href, text, 'btn-raised', getFullButtonColor(color), type=type, extraClass=extraClass)


@register.simple_tag
def flatBtn(href, text, color, type="", extraClass=""):
    return button(href, text, '', getFullButtonColor(color), type=type, extraClass=extraClass)


@register.simple_tag
def floatInput(id, label, text=""):
    ctx = {
        'id': id,
        'label': label,
        'text': text,
    }
    return render_template_file("floatInput", ctx)


@register.simple_tag
def realBtn(id, text, color, type="", extraClass=""):
    ctx = {
        'id': id,
        'text': text,
        'color': getFullButtonColor(color),
        'type': type,
        'extraClass': extraClass,
    }
    return render_template_file("realButton", ctx)


@register.simple_tag
def select(id, label, options, defaultValue=""):
    ctx = {
        'id': id,
        'label': label,
        'options': options,
        'defaultValue': defaultValue,
    }
    return render_template_file("select", ctx)
