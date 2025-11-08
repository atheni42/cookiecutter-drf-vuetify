from knox import views as knox_views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from backend.mymodel.views import DummyViewSet
from backend.tokenauth.views import LoginView

router = routers.DefaultRouter()
router.register(r"api/dummy", DummyViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path(r'api/login/', LoginView.as_view(), name='knox_login'),
    path(r'api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'api/logoutall/', knox_views.LogoutAllView.as_view(),
         name='knox_logoutall'),
]
