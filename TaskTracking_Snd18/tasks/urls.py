from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path("", views.anime_page_list, name='anime-page-list'),
    path("anime/<int:pk>/", views.anime_page_detail, name='anime-page-detail'),
    path("create/", views.anime_page_create, name='anime-page-create'),
    path("update/<int:pk>/", views.anime_page_update, name='anime-page-update'),
    path("delete/<int:pk>/", views.anime_page_delete, name='anime-page-delete'),

    path("api/anime/", views.anime_list, name='anime-list'),
    path("api/anime/<int:pk>/", views.anime_detail, name='anime-detail'),
    path("api/create/", views.anime_create, name='anime-create'),
    path("api/update/<int:pk>/", views.anime_update, name='anime-update'),
    path("api/delete/<int:pk>/", views.anime_delete, name='anime-delete'),

    path("register/", views.register_view, name='register'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
]
