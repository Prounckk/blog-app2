
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("accounts.urls")),
    path("blog/", include("blog.urls")),
]