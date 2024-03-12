from django.urls import path
from .users_view import UserMethods
from .locations_view import LocationMethods
from .products_view import ProductMethods
from .salePlace_view import SalePlaceMethods
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserMethods)
router.register(r"products", ProductMethods)
router.register(r"salePlace", SalePlaceMethods)
router.register(r"locations", LocationMethods)

urlpatterns = router.urls

# urlpatterns =[
#     # path('', include(router.urls)),
#     path('users/', user_list),
# ]
