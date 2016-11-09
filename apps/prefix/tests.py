# coding=utf-8
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from apps.prefix.views import prefixJSON
from .models import Prefix, Meaning, Word

__author__ = 'peter'


class PrefixTest(TestCase):
    def test_get_prefix_json(self):
        prefix = Prefix.new('aa')
        prefix.save()

        meaning1 = Meaning.new("中文", "en", prefix)
        meaning1.save()

        meaning2 = Meaning.new("ch2", "en2", prefix)
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
        response = prefixJSON(request, prefix.pk)
        print(response.content)
