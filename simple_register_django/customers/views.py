from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Customer


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        email = request.POST['email']
        Customer.objects.create(email=email)

        return HttpResponse()
