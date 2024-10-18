from django.urls import path
from recipes.views import about, home, contact

urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contact)
]