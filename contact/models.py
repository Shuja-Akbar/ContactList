# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ContactList(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=150, null=True)