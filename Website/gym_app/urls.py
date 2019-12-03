"""gym_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gym_app.core import views
from rest_framework import routers
from .core.api_auth import ApiAuth

# router = routers.DefaultRouter()
# router.register(r'test-auth', views.TestAuthView,basename="TestAuth")
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('submit_form', views.submit_form, name = 'loanform'),
    # path('loanform/', views.LoanForm.as_view(), name='loanform'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('denied/', views.DeniedView.as_view(), name='denied'),
    path('preapproved/', views.PreapprovedView.as_view(), name='preapproved'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("test-auth/",views.api_hello),
    # path('calendar/', include("Calendar.urls"))

]
