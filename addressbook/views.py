from django.views.generic import View
from django.http import HttpResponse


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")


