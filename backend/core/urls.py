from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HabitViewSet,
    DailyLogViewSet,
    BuilderManifestoViewSet,
    SMSMessageViewSet,
    generate_gpt_message,
    verify_password,
)

router = DefaultRouter()
router.register(r'habits', HabitViewSet)
router.register(r'logs', DailyLogViewSet)
router.register(r'manifesto', BuilderManifestoViewSet)
router.register(r'messages', SMSMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-message/', generate_gpt_message),
    path('verify-password/', verify_password, name='verify-password'),
]
