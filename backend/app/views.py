from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from json import loads
from .models import User


def querySet2Json(querySet):
    return loads(serialize("json", querySet))


def index(request):
    return JsonResponse({
        "code": 200,
        "message": "请求成功",
        "data": querySet2Json(User.objects.all())
    })
