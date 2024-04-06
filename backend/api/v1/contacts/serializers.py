from rest_framework import serializers

from apps.contacts.models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'profile_image_url', 'name', 'company', 'position', 'email', 'phone')


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'owner')
