from django.urls import path, include
from review_spyder import views

urlpatterns = [
    path('', views.get_index_page),
    path('foo/', views.foo),
    path('spyder/', views.spyder),
    path('getInfo/', views.getinfo),
    path('getReview/', views.getreview),
    path('sentiments1/', views.api1),
    path('getWordCloud/', views.WordCloud),
    path('test/', views.test)
]
