# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from rest_framework import decorators, response, routers, serializers, viewsets


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve: do some shit
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @decorators.list_route(methods=["put"])
    def some_put(self, request):
        return response.Response()

    def get_description(self):
        return "Group endpoint"


router = routers.DefaultRouter()
router.register("group", GroupViewSet)
