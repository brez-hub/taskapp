# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core import serializers


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачa'
