from typing import Any
from django.shortcuts import HttpResponse, render
from goods.models import Categories
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - главная'
        context['content'] = 'Магазин мебели Home'
        return context
    
class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - о нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'cool store'
        return context
# def index(request):

#     context = {
#         'title':'Home',
#         'content': 'Roma'
       
#     }
#     return render(request, 'main/index.html', context)

# def about(request):
#     context = {
#         'title':'Home - про нас',
#         'content': 'О нас',
#         'text_on_page': 'Text info'
#     }
#     return render(request, 'main/about.html', context)