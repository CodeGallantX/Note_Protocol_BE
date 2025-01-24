from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Notes, User
from .serializers import UserSerializer, NotesSerializer

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendNotesView(APIView):
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Note sent successfully!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FetchNotesView(APIView):
    def post(self, request, username):
        user = User.objects.get(username=username).first()
        if not user:
            return Response({'message': "User not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        notes = Notes.objects.filter(receiver=user)
        serializer = NotesSerializer(notes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)