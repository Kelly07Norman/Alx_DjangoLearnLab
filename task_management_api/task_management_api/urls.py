from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Include task URLs
    path('api/', include('users.urls')),   # Include user URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing tokens
]
