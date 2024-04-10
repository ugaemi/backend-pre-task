from rest_framework import filters, pagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from api.mixins import OwnerPermissionMixin
from api.v1.contacts.serializers import ContactListSerializer, ContactDetailSerializer, ContactLabelListSerializer, \
    ContactLabelDetailSerializer
from apps.contacts.models import Contact, ContactLabel


class ContactListCreateAPIView(OwnerPermissionMixin, ListCreateAPIView):
    model = Contact
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'email', 'phone']
    ordering = ['created_at']
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return super().get_queryset().prefetch_related('labels')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactListSerializer
        return ContactDetailSerializer


class ContactDetailAPIView(OwnerPermissionMixin, RetrieveUpdateDestroyAPIView):
    model = Contact
    serializer_class = ContactDetailSerializer


class ContactLabelListCreateAPIView(OwnerPermissionMixin, ListCreateAPIView):
    model = ContactLabel
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['created_at']
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactLabelListSerializer
        return ContactLabelDetailSerializer


class ContactLabelDetailAPIView(OwnerPermissionMixin, RetrieveUpdateDestroyAPIView):
    model = ContactLabel
    serializer_class = ContactLabelDetailSerializer
