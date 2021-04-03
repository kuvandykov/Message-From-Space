from django.urls import path
from django.views.generic import RedirectView

from rest_framework import routers

from .views import (MessageViewSet, MessageReaded, 
                AllMessagesViewSet, ViewForAllMessages)



router = routers.DefaultRouter()
#router.register(r'^$', AllMessagesViewSet)
router.register('get_messages', MessageViewSet, basename='messages')
router.register('mark_read', MessageReaded)

urlpatterns = [path('messanger', ViewForAllMessages, name='all-messages')] + router.urls