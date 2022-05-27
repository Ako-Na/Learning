from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render

# Create your views here.
class Profile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"current_user": str(request.user.id)}
        return Response(content, status=status.HTTP_200_OK)
