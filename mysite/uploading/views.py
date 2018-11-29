# mysite/uploading/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from rest_framework.parsers import FileUploadParser
from asgiref.sync import async_to_sync
import base64

# Create your views here.
class UploadTextView(APIView):
    def post(self, request, format=None):
        message = request.query_params['message']
        if not message:
            raise ParseError("Empty content")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("chat", {
            "type": "chat.message",
            "message": message,
        })

        return Response({'status': 'ok'})

class UploadImageView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("chat", {
            "type": "chat.message",
            "image64": base64.b64encode(f.read()).decode("ascii"),
        })

        return Response({'status': 'ok'})
