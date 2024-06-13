from django.contrib import admin
from django.urls import path
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search_view, name='search'),
]