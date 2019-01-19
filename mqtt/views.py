from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def index(request):
    #return HttpResponse("<h1>Basecamp Homepage</h1>")
    return render (request, 'mqtt/mqtt.html')

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)