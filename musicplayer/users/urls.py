from django.urls import path

from .views import ChangePasswordView
from .views import UserDetailView
from .views import UserLoginView
from .views import UserLogoutView
from .views import UserRegisterView

urlpatterns = [
    path('authentication/register/', UserRegisterView.as_view(), name='user_register'),
    path('authentication/login/', UserLoginView.as_view(), name='user_login'),
    path('authentication/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('authentication/change-password/', ChangePasswordView.as_view(), name='user_change_password'),
    path('detail/<str:user_id>/', UserDetailView.as_view(), name='user-detail'),

    # path('authentication/social/', include('allauth.urls')),
    # path('authentication/google/', SocialLogin.google_token, name='google_login'),
    # path('authentication/facebook/', SocialLogin.facebook_token, name='facebook_login'),
]
