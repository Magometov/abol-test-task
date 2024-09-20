from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("book/", include("src.apps.api.urls.book_urls")),
]
