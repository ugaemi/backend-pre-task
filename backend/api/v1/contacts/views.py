from rest_framework import generics, permissions, filters, pagination

from apps.contacts.models import Contact
from api.v1.contacts.serializers import ContactListSerializer, ContactDetailSerializer


class ContactListCreateAPIView(generics.ListCreateAPIView):
    model = Contact
    permission_classes = [permissions.IsAuthenticated]
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
