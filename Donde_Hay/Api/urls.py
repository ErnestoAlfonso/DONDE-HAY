from django.urls import path
from .views import user_list
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('users', user_list, basename='users')

urlpatterns =[
    # path('', include(router.urls)),
    path('users/', user_list),
]