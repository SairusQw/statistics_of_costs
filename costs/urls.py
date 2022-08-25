from django.urls import path

from costs.views import \
    index, \
    CostListView, \
    CostCreateView, \
    CostDeleteView, \
    CostUpdateView, \
    delete_all,\
    CustomUserListView,\
    CustomUserDetailView,\
    CustomUserCreateView,\
    CustomUserDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "costs/",
        CostListView.as_view(),
        name="cost_list"
    ),
    path(
        "costs/create/",
        CostCreateView.as_view(),
        name="cost_create",
    ),
    path(
        "costs/<int:pk>/update/",
        CostUpdateView.as_view(),
        name="cost_update",
    ),
    path(
        "costs/<int:pk>/delete/",
        CostDeleteView.as_view(),
        name="cost_delete",
    ),
    path(
        "costs/delete/all/",
        delete_all,
        name="cost_delete_all",
    ),
    path(
        "users/",
        CustomUserListView.as_view(),
        name="user_list"
    ),
    path(
        "users/<int:pk>/",
        CustomUserDetailView.as_view(),
        name="user_detail"
    ),
    path(
        "users/create/",
        CustomUserCreateView.as_view(),
        name="user_create"
    ),
    path(
        "users/<int:pk>/delete/",
        CustomUserDeleteView.as_view(),
        name="user_delete"
    ),
]

app_name = "costs"
