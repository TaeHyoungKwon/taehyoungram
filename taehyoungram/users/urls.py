from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(
        regex=r'^explorer/$',
        view=views.ExploerUsers.as_view(),
        name='exploer_user'
    ),
]
