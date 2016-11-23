# coding=utf-8
import json

from django.db import IntegrityError
from django.db import models

__author__ = 'peter'


class Root(models.Model):
    type_choices = (
        ("prefix", "prefix"),
        ("root", "root"),
        ("suffix", "suffix"),
    )
    root = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=type_choices, default='prefix')

    class Meta:
        unique_together = ('root', 'type',)

    @staticmethod
    def new(root="", type="prefix"):
        r = Root()
        r.root = root
        r.type = type
        return r

    # 通过request请求来添加一个新的Root,失败返回None
    @staticmethod
    def add(request):
        if request.POST:
            root = request.POST.get("root", "").strip()
            type = request.POST.get("type", "prefix")
            if root:
                try:
                    r = Root.objects.get(root=root, type=type)
                except Root.DoesNotExist:
                    r = Root.new(root, type)
                    r.save()
                return r
        return None

    @staticmethod
    def get(pk):
        return Root.objects.get(pk=pk)

    @staticmethod
    def getAll(type=None):
        roots = Root.objects.filter()
        if type:
            roots = roots.filter(type=type)
        return roots.order_by('root')

    @staticmethod
    def getLettersByType(type):
        letters = []
        roots = Root.getAll(type)
        for root in roots:
            rs = root.root.split('/')
            for r in rs:
                letters.append(r[0])
        return sorted(set(letters))

    @staticmethod
    def getLetters():
        letters = {
            'prefix': Root.getLettersByType('prefix'),
            'root': Root.getLettersByType('root'),
            'suffix': Root.getLettersByType('suffix'),
        }
        return letters

    def as_json(self):
        j = dict(
            id=self.pk,
            root=self.root,
            type=self.type,
            meanings=[]
        )
        for meaning in Meaning.objects.filter(root=self):
            j['meanings'].append(meaning.as_json())
        return j

    @staticmethod
    def as_jsons(type=None):
        j = []
        roots = Root.getAll(type)
        for root in roots:
            j.append(root.as_json())
        return j

    def __str__(self):
        return self.root


class Meaning(models.Model):
    chinese = models.CharField(max_length=50, blank=True, null=True)
    english = models.CharField(max_length=50, blank=True, null=True)
    root = models.ForeignKey(Root)

    @staticmethod
    def new(chinese="", english="", root=None):
        m = Meaning()
        m.chinese = chinese
        m.english = english
        m.root = root
        return m

    # 通过request请求来添加其包含的meaning,并与Root相关联,失败返回False
    @staticmethod
    def add(request, root):
        if request.POST:
            for i in range(100):
                chinese = request.POST.get("meaning_chinese_" + str(i), "").strip()
                english = request.POST.get("meaning_english_" + str(i), "").strip()
                if chinese or english:
                    meaning = Meaning.new(chinese, english, root)
                    meaning.save()
                    # 添加Word
                    for j in range(100):
                        word = request.POST.get("word_word_%d_%d" % (i, j), "").strip()
                        if word:
                            Word.new(word, meaning).save()
            return True
        return False

    @staticmethod
    def get(pk):
        return Meaning.objects.get(pk=pk)

    @staticmethod
    def getAll():
        return Meaning.objects.all()

    def as_json(self):
        j = dict(
            id=self.pk,
            chinese=self.chinese,
            english=self.english,
            words=[],
        )
        for word in Word.objects.filter(meaning=self):
            j['words'].append(word.as_json())
        return j

    def __str__(self):
        return self.chinese + " " + self.english


class Word(models.Model):
    word = models.CharField(max_length=50)
    meaning = models.ForeignKey(Meaning)

    @staticmethod
    def new(word="", meaning=None):
        w = Word()
        w.word = word
        w.meaning = meaning
        return w

    @staticmethod
    def get(pk):
        return Word.objects.get(pk=pk)

    @staticmethod
    def getAll():
        return Word.objects.all()

    def as_json(self):
        return dict(
            id=self.pk,
            word=self.word,
        )

    def __str__(self):
        return self.word
