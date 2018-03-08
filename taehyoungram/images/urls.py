
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^feeds/$',
        view=views.Feed.as_view(),
        name='feeds',
    ),


]