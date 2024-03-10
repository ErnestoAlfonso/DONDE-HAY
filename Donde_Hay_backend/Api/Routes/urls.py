from django.urls import path
from .users_view import UserMethods
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserMethods)

urlpatterns = router.urls

# urlpatterns =[
#     # path('', include(router.urls)),
#     path('users/', user_list),
# ]