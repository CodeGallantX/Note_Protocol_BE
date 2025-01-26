from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView, SendNoteView, InboxView, SentNotesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('write/', SendNoteView.as_view(), name='send_note'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('sent/', SentNotesView.as_view(), name='sent_notes'),
]
