from django.shortcuts import HttpResponse, render
from goods.models import Categories
# Create your views here.
def index(request):

    context = {
        'title':'Home',
        'content': 'Roma'
       
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title':'Home - про нас',
        'content': 'О нас',
        'text_on_page': 'Text info'
    }
    return render(request, 'main/about.html', context)