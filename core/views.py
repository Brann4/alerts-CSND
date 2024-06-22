from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, req, *args, **kwargs):
        context = {
            
        }
        return render(req, 'index.html', context)