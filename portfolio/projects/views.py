from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework import authentication, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating, updating
    and retrieving projects for
    the portfolio site.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
