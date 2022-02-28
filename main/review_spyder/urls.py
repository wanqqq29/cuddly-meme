from django.urls import path, include
from review_spyder import views

urlpatterns = [
    path('',views.get_index_page),
    path('spyder/', views.spyder),
]
