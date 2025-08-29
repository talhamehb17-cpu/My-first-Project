from django.urls import path
from . import views

urlpatterns = [
    path("testitems", views.get_testitems, name="get_testitems"),                  # GET all
    path("testitems-<int:item_id>", views.get_testitem, name="get_testitem"),      # GET single
    path("testitems-create", views.create_testitem, name="create_testitem"),       # POST
    path("testitems-<int:item_id>-update", views.update_testitem, name="update_testitem"),  # PUT
    path("testitems-<int:item_id>-delete", views.delete_testitem, name="delete_testitem"),  # DELETE
]
