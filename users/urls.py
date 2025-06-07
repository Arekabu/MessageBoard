from django.urls import path
from .views import UserPage, CustomRegisterView


urlpatterns = [
    path('<int:pk>', UserPage.as_view(), name = 'user_page'),
    path('signup/', CustomRegisterView.as_view(), name = 'signup_page'),
    path('verify/', CustomRegisterView.as_view(), name = 'verify_page'),
]
