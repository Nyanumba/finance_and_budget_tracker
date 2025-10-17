from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, ProfileFrontendView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/', include('transactions.urls')),
    path('api/reports/', include('reports.urls')),
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/new/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    path('transactions/export/', views.transaction_export, name='transaction_export'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileFrontendView.as_view(), name='profile'),
]