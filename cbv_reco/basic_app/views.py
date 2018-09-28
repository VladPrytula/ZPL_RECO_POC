from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from .reco_system.imf import ImplicitRecommender
from .models import PetOwner, Pet, Product

# Create your views here.


class PetOwnerListView(ListView):
    context_object_name = 'owners'
    model = PetOwner
    paginate_by = 10
    queryset = PetOwner.objects.all()


class PetOwnerDetailView(DetailView):
    imf = ImplicitRecommender()
    print(imf)
    context_object_name = 'owner_detail'
    model = PetOwner
    template_name = 'basic_app/petowner_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PetOwnerDetailView, self).get_context_data(**kwargs)
        print(int(context['owner_detail'].lookup_customers_idx))

        context['list_of_recos'] = PetOwnerDetailView.imf.recommend(int(context['owner_detail'].lookup_customers_idx))
        recommended_items = PetOwnerDetailView.imf.recommend(int(context['owner_detail'].lookup_customers_idx))
        recommended_products = Product.objects.all().filter(name__in=recommended_items)
        print(recommended_products)
        print(context)
        context['recommended_products'] =recommended_products
    
        return context 


""" def index(request):
    return render(request, 'index.html') """

""" class CBView(View):
    def get(self,request):
        return HttpResponse('classed based views are in works')
 """


class IndexView(TemplateView):
    template_name = 'index.html'


"""  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected'] = 'BASIC INJECTION'
        return context
 """
