from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^explorer/$',
        view=views.ExploerUsers.as_view(),
        name='exploer_user'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),

    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
]
