from django.urls import path, include
from workspace.views import change_password, create_game, workspace, workspace_detail_game, update_game, delete_game, login_user, logout_user, register_user, profile, change_profile
urlpatterns = [
    path('workspace-detail-game<int:id>', workspace_detail_game, name="workspace_detail_game"),
    path('update-game/<int:id>', update_game, name="update_game"),
    path('delete-game/<int:id>', delete_game, name="delete_game"),
    path('profile/', profile, name="profile"),
    path('change-profile/', change_profile, name="change_profile"),
    path('change-password/', change_password, name="change_password"),
    path('create-game/', create_game, name="create_game"),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('', workspace, name='workspace'),
]