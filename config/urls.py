"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Prography API Doc')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='dicemono api')),
    path('api/doc/', schema_view),
    path('api/get_token/', obtain_auth_token),
]
