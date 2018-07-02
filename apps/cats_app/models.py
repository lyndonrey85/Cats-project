# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

# Create your models here.
class CatManager(models.Manager):
    def validate_input(self, post_data):
        errors = []
        if(int(post_data["age"]) > 25):
            errors.append("That cat is too old")
        if not post_data["name"].isalpha():
            errors.append("Only letters in a cat name!")
        return errors


class Cat(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    objects = CatManager()