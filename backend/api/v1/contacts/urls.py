from django.urls import path

from .views import ContactListCreateAPIView, ContactDetailAPIView, ContactLabelListCreateAPIView, \
    ContactLabelDetailAPIView

urlpatterns = [
    path('', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('<int:pk>', ContactDetailAPIView.as_view(), name='contact-detail'),
    path('labels', ContactLabelListCreateAPIView.as_view(), name='contact-label-list-create'),
    path('labels/<int:pk>', ContactLabelDetailAPIView.as_view(), name='contact-label-detail'),
]
