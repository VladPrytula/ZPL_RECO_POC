from django.urls import path, re_path
from .views import PetOwnerListView, PetOwnerDetailView


app_name = 'basic_app'

urlpatterns = [
    path('', PetOwnerListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$',PetOwnerDetailView.as_view(), name='detail'),
]