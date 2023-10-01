from django.urls import path

from . import views

app_name = "lunchmap"

urlpatterns = [
    path("", views.ListView.as_view(), name="list"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.UpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]