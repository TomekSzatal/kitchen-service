from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    CookListView,
    DishTypeListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    CookDeleteView,
    CookUpdateView,
    CookCreateView,
    CookDetailView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishTypeCreateView
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
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dishtype-list",
        ),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create",
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
    ]

app_name = "kitchen"