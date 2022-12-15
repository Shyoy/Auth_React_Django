from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.index),
    path('products/', views.all_products, name='products'),
    path('products/<pk>', views.product_detail, name='product'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

