from django.urls import path
from . import views

urlpatterns = [
    path('list',views.list_base, name="py.list"),
    path('list-comprehensions',  views.list_comprehensions, name="py.list_comprehensions"),
    path('nested-list-comprehensions',  views.nested_list_comprehensions, name="py.nested_list_comprehensions"),
]
