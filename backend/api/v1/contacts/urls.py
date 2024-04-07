from django.urls import path

from .views import ContactListCreateAPIView, ContactDetailAPIView

urlpatterns = [
    path('', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('<int:pk>', ContactDetailAPIView.as_view(), name='contact-detail'),
]
