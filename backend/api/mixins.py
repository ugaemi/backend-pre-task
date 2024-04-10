from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwner


class OwnerPermissionMixin:
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
