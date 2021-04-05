from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

from .models import MessageFromSpace
from .serializers import MessageSerializer


class AllMessagesViewSet(viewsets.ModelViewSet):
    queryset = MessageFromSpace.objects.all()
    serializer_class = MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageFromSpace.objects.filter(read=False)
    serializer_class = MessageSerializer

    def list(self, request, *args):
        if 'last_id' in request.query_params:
            last_id = request.query_params['last_id']
            items = MessageFromSpace.objects.filter(read=False, id__gt=last_id)
            if items:
                serializer_class = MessageSerializer(items, many=True)
                return Response(serializer_class.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            items = MessageFromSpace.objects.filter(read=False)
            serializer_class = MessageSerializer(items, many=True)
            return Response(serializer_class.data)

class MessageReaded(viewsets.ModelViewSet):
    queryset = MessageFromSpace.objects.filter(read=False)
    serializer_class = MessageSerializer

    def patch(self, request):
        readed_id = request.query_params['id']
        message = MessageFromSpace.objects.get(id=readed_id)
        message.read = True
        message.save()

        return Response()


def ViewForAllMessages(request):

    #messages = MessageFromSpace.objects.all()
    #serializer_class = MessageSerializer(messages, many=True)

    return render(request, '/home/lukura/Message-From-Space/backend/messanger/templates/dist/index.html')