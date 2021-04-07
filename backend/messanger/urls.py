
from django.urls import path, re_path

from rest_framework import routers

from .views import (MessageViewSet, MessageReaded, ViewForAllMessages)



router = routers.DefaultRouter()
router.register('get_messages', MessageViewSet, basename='messages')

urlpatterns = [
    path(r'^$', ViewForAllMessages, name='all-messages'),
    re_path('mark_read/', MessageReaded.as_view()),
    ] + router.urls