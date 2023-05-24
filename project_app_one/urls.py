from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='landing_page'),
    
    ######################### control flow tool #####################################################
    
    path('if-else', views.if_else, name="core.if_else"),
    path('for-loop', views.for_loop, name="core.for_loop"),
    path('break-continue', views.break_continue, name="py.break_continue"),
    path('match',views.match, name="py.match"),
    
    ######################### function #####################################################
    
    path('lambda-function',views.lambda_function, name="py.lambda"),
    path('lambda',views.lambda_with_filter_map_reduce, name="py.lambda_with_filter_map_reduce"),
    
]
