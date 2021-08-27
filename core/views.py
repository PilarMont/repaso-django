from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404

class HomeView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'index.html', context )