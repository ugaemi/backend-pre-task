from rest_framework import generics, filters, pagination
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwner
from api.v1.contacts.serializers import ContactListSerializer, ContactDetailSerializer
from apps.contacts.models import Contact


class ContactListCreateAPIView(generics.ListCreateAPIView):
    model = Contact
    permission_classes = [IsOwner, IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'email', 'phone']
    ordering = ['created_at']
    pagination_class = pagination.PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactListSerializer
        return ContactDetailSerializer


class ContactDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = Contact
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        return ContactDetailSerializer
