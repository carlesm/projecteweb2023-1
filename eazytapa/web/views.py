from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import generic

from web.models import Bar, Tapa

# Create your views here.


def root(request):
    # bars = Bar.objects.all()
    # bars = [bar.name for bar in bars]
    # html = "<br />".join(bars)
    # return HttpResponse(html)
    bars = Bar.objects.all()
    return render(request,'web/index.html', { "bars": bars})

def bar(request, bar_id):
    try:
       bar = Bar.objects.get(pk=bar_id)
    except Bar.DoesNotExist:
        raise Http404('No hi ha aquest bar')
    return render(request, 'web/bar.html', {"bar":bar})

class TapaView(generic.DetailView):
    model = Tapa
    template_name = 'web/tapa.html'
