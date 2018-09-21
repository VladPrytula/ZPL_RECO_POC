from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import PetOwner, Pet, Product

# Create your views here.

class OwnerListView(ListView):
    model = PetOwner

class OwnerDetailView(DetailView):
    model = PetOwner
    template_name = 'basic_app/owner_detail.html'



""" def index(request):
    return render(request, 'index.html') """

""" class CBView(View):
    def get(self,request):
        return HttpResponse('classed based views are in works')
 """


""" class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected'] = 'BASIC INJECTION'
        return context
 """
