from .models import BlogEntry
from .serializers import BlogEntrySerializer
from rest_framework import viewsets
from rest_framework import authentication, permissions


class BlogEntryViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating, updating
    and viewing blog entries.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogEntrySerializer
    queryset = BlogEntry.objects.all()
