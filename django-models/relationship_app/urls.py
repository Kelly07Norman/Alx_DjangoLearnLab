from django.urls import path
from .views import list_books, LibraryDetailView, register  # Ensure 'register' is imported
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', views.home, name='home')
]
