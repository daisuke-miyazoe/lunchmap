from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from lunchmap import views

# DefaultRouter クラスのインスタンスを代入
defaultRouter = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
defaultRouter.register('category',views.CategoryViewSet)
defaultRouter.register('shop',views.ShopViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lunchmap/', include('lunchmap.urls')),
    path('api/', include(defaultRouter.urls)),
]
