from django.urls import path

from rest_framework import routers

from .views import MessageViewSet, MessageReaded, AllMessagesViewSet



router = routers.DefaultRouter()
#router.register(r'^$', AllMessagesViewSet)
router.register('get_messages', MessageViewSet, basename='messages')
router.register('mark_read', MessageReaded)

urlpatterns = router.urls