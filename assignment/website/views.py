from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
import requests
# Create your views here.


class Index(View):
    def get(self, request):
        path = "{0}api/gale/".format(request.build_absolute_uri())
        try:
            return render(request, "index.html", {"path": path})
        except Exception as e:
            print(e, "-----------error")
            return HttpResponse("error")
