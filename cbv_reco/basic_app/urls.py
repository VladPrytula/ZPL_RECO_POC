from django.urls import path
from .views import PetOwnerListView


app_name = 'basic_app'

urlpatterns = [
    path('', PetOwnerListView.as_view(), name='list')
]