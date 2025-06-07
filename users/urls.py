from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import UserPage, CustomRegisterView, VerifyCode


urlpatterns = [
    path('<int:pk>', UserPage.as_view(), name = 'user_page'),
    path('signup/', CustomRegisterView.as_view(), name = 'signup_page'),
    path('verify/', VerifyCode.as_view(), name = 'verify_page'),
    path('login/', LoginView.as_view(template_name='login_page.html', next_page=settings.SITE_URL), name = 'login_page'),
    path('logout/', LogoutView.as_view(next_page=settings.SITE_URL), name = 'logout_page'),
]
