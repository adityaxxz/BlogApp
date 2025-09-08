from django.urls import path
from .views import UserRegister
# from .views import BlacklistTokenUpdateView
# from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegister.as_view(), name="register_user"),
    # path('login/', TokenObtainPairView.as_view(), name="login_user"),
    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist')
]