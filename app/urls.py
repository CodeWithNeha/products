
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'products', ProductsViewManage)
router.register(r'fetchMostSearched',FetchMostSearched)
urlpatterns = router.urls