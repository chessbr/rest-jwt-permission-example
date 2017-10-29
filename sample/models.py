# -*- coding: utf-8 -*-
from django.db import models


class GroupScope(models.Model):
    group = models.ForeignKey("auth.Group", related_name="scopes")
    scope = models.CharField(max_length=250)

    class Meta:
        unique_together = ("group", "scope")
