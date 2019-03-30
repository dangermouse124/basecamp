from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.views.generic import CreateView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . models import temp_max_min
from . models import temp_10min


# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def index(request):
    #return HttpResponse("<h1>Basecamp Homepage</h1>")
    return render (request, 'mqtt/mqttbase.html')

@login_required(login_url=reverse_lazy('login'))
def shed(request):
    #return HttpResponse("<h1>Basecamp Homepage</h1>")
    return render (request, 'mqtt/web_gpio.html')


@login_required(login_url=reverse_lazy('login'))
def tenMin(request):
    #pagename = '/' + pagename
    context = {
        'maxmin_list':temp_max_min.objects.all,
        'tenmin_list':temp_10min.objects.all,
    }
    #assert False
    return render (request, 'mqtt/carport.html', context)


