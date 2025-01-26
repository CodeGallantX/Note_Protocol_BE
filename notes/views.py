from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User, Notes
from .serializers import UserSerializer, NotesSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# User registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid or missing refresh token."}, status=status.HTTP_400_BAD_REQUEST)

# Send a note
class SendNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        serializer.initial_data['sender'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Note sent successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View received notes
class InboxView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Notes.objects.filter(receiver=request.user).order_by('-timestamp')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View sent notes
class SentNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Notes.objects.filter(sender=request.user).order_by('-timestamp')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)