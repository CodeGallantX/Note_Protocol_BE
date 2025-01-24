from django.urls import path
from .views import RegisterView, SendNotesView, FetchNotesView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("send-notes/", SendNotesView.as_view(), name="send-notes"),
    path("fetch-notes/<str:username>/", FetchNotesView.as_view(), name="fetch-notes"),
]
