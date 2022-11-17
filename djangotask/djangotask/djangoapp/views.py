from django.shortcuts import render
from . models import Place
from . models import Team


# Create your views here.
def demo(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, 'index.html', {'res1': obj1, 'res2': obj2})
