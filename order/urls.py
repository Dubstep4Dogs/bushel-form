from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("", views.OrderView.as_view()),
    path("thank-you", views.thank_you),
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/edit/", views.order_edit, name="order_edit"),
    path("orders/<int:pk>/delete/", views.order_delete, name="order_delete"),
]