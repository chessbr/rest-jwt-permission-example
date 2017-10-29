# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from rest_jwt_permission.scopes import get_all_permission_providers_scopes

from .models import GroupScope


class GroupScopeAdminForm(forms.ModelForm):
    scope = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(GroupScopeAdminForm, self).__init__(*args, **kwargs)
        scopes = get_all_permission_providers_scopes()
        choices = [(scope.identifier, "{} - {}".format(scope.identifier, scope.get_description())) for scope in scopes]
        self.fields["scope"].choices = choices

    class Meta:
        model = GroupScope
        fields = "__all__"


@admin.register(GroupScope)
class GroupScopeAdmin(admin.ModelAdmin):
    form = GroupScopeAdminForm
    list_display = ("group", "scope")
