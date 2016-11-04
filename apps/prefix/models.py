# coding=utf-8
from django.db import IntegrityError
from django.db import models

__author__ = 'peter'


class Prefix(models.Model):
    prefix = models.CharField(max_length=50, unique=True)

    @staticmethod
    def new(prefix=""):
        p = Prefix()
        p.prefix = prefix
        return p

    # 通过request请求来添加一个新的Prefix,失败返回None
    @staticmethod
    def add(request):
        if request.POST:
            prefix = request.POST.get("prefix", "")
            if prefix:
                try:
                    p = Prefix.objects.get(prefix=prefix)
                except Prefix.DoesNotExist:
                    p = Prefix.new(prefix)
                    p.save()
                return p
        return None

    @staticmethod
    def get(pk):
        return Prefix.objects.get(pk=pk)

    @staticmethod
    def getAll(letter=None):
        if letter:
            return Prefix.objects.filter(prefix__startswith=letter)
        return Prefix.objects.all()

    @staticmethod
    def getLetters():
        return sorted(set(map(lambda p: p.prefix[0], Prefix.objects.all())))

    def __str__(self):
        return self.prefix


class Meaning(models.Model):
    chinese = models.CharField(max_length=50, blank=True, null=True)
    english = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.ForeignKey(Prefix)

    @staticmethod
    def new(chinese="", english="", prefix=None):
        m = Meaning()
        m.chinese = chinese
        m.english = english
        m.prefix = prefix
        return m

    # 通过request请求来添加其包含的meaning,并与Prefix相关联,失败返回False
    @staticmethod
    def add(request, prefix):
        if request.POST:
            for i in range(100):
                chinese = request.POST.get("meaning_chinese_" + str(i), "")
                english = request.POST.get("meaning_english_" + str(i), "")
                if chinese or english:
                    meaning = Meaning.new(chinese, english, prefix)
                    meaning.save()
                    # 添加Word
                    for j in range(100):
                        word = request.POST.get("word_word_%d_%d" % (i, j))
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

    def __str__(self):
        return self.word
