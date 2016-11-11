# coding=utf-8
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from .views import rootJSON
from .models import Root, Meaning, Word

__author__ = 'peter'


class RootTest(TestCase):
    def test_get_root_json(self):
        root = Root.new('aa')
        root.save()

        meaning1 = Meaning.new("中文", "en", root)
        meaning1.save()

        meaning2 = Meaning.new("ch2", "en2", root)
        meaning2.save()

        word11 = Word.new("w11", meaning1)
        word11.save()
        word12 = Word.new("w12", meaning1)
        word12.save()
        word21 = Word.new("w21", meaning2)
        word21.save()
        word22 = Word.new("w22", meaning2)
        word22.save()

        request = HttpRequest()
        response = rootJSON(request, root.pk)
        print(response.content)
