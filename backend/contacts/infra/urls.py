from contacts.presenters.views.contacts import ContactsViewSet
from contacts.presenters.views.auth import (
    CustomUserCreate,
    ObtainTokenPairWithEmailView
)
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)
router.register("", ContactsViewSet, basename="api")

app_name = "contacts"

urlpatterns = [
    path("", include(router.urls)),
    path('auth/user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('auth/token/obtain/', ObtainTokenPairWithEmailView.as_view(), name='token_create'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]