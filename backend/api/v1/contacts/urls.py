from django.urls import path, include

from .views import ContactListCreateAPIView

urlpatterns = [
    path('', ContactListCreateAPIView.as_view(), name='contact-list-create'),
]
