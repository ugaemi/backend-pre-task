from django.urls import path, include


urlpatterns = [
    path('contacts/', include('api.v1.contacts.urls')),
]
