from django.urls import path

from kitchen.views import index, DishListView, CookListView, DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "Dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
            "Cooks/",
            CookListView.as_view(),
            name="cook-list",
        ),
    path(
            "DishTypes/",
            DishTypeListView.as_view(),
            name="dishtype-list",
        ),
    ]

app_name = "kitchen"