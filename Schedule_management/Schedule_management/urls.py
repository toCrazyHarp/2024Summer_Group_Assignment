"""Schedule_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mainpage import views as mainpage_views
from Info import views as info_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Info/',info_views.Info),
    path('',mainpage_views.mainpage),
    path('Info/add/',info_views.add),
    path('Info/edit/',info_views.edit),
    path('Info/delete/',info_views.delete),
     path('Info/shorter/',info_views.shorter),
    path('Info/longer/',info_views.longer),
    path('Info/routine/',info_views.routine),
]
