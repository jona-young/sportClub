from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views as member_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('bookings/', include('bookings.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    path('profile/', member_views.profile, name='profile'),

]
