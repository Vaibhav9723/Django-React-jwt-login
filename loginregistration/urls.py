from django.urls import path
from .views import *


urlpatterns = [
    path('create',regcustomer),
    # path('loginU',logincustomer),
    path('loginU', login_with_jwt),
    path('dashboard',user_dashboard),
]


