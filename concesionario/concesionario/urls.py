# concesionario/urls.py

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from prueba import views  # Asegúrate de que 'prueba' es tu aplicación principal
from prueba.auth_views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Define las URLs de tu proyecto concesionario
urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el admin de Django
    path('catalog/', include('catalog.urls')),  # Incluir las URLs de la aplicación 'catalog'
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


