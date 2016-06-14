"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, patterns
from django.contrib import admin
from .views import ProjectList, ProjectCreate, ProjectUpdate, ProjectDelete
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        ProjectList.as_view(), name='project-list'),
    url(r'add/$',
        ProjectCreate.as_view(), name='project-add'),
    url(r'(?P<pk>[0-9]+)/$',
        ProjectUpdate.as_view(), name='project-update'),
    url(r'(?P<pk>[0-9]+)/delete/$',
        ProjectDelete.as_view(), name='project-delete'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout,
        {'next_page': 'project-list'}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
