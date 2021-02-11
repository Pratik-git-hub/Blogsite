from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('create_post/',views.create,name = "create"),
    path('search_results/',views.search_res,name = 'search_res')
]