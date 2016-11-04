# coding=utf-8
from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Prefix, Meaning, Word

__author__ = 'peter'


class WordInline(NestedStackedInline):
    model = Word
    extra = 1
    fk_name = 'meaning'


class MeaningInline(NestedStackedInline):
    model = Meaning
    extra = 1
    fk_name = 'prefix'
    inlines = [WordInline]


class PrefixAdmin(NestedModelAdmin):
    search_fields = (
        'prefix',
    )
    inlines = [MeaningInline]


admin.site.register(Prefix, PrefixAdmin)
admin.site.register(Meaning)
admin.site.register(Word)
