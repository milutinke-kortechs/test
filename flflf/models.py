# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from annoying.fields import AutoOneToOneField
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, default='a')


class Profile(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')

class Preference(models.Model):
    profile = AutoOneToOneField(Profile, on_delete=models.CASCADE, primary_key=True, related_name='preference')