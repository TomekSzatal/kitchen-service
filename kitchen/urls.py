from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    CookListView,
    DishTypeListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView, DishDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
            "cooks/",
            CookListView.as_view(),
            name="cook-list",
        ),
    path(
            "dishTypes/",
            DishTypeListView.as_view(),
            name="dishtype-list",
        ),
    ]

app_name = "kitchen"