from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        html = '<form action="." method="post"><input type="email" name="email"><button type="submit">Submit</button></form>'
        return HttpResponse(html)
