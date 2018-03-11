
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feeds',
    ),

    url(
        regex=r'(?P<image_id>\d+)/like/',
        view=views.LikeImage.as_view(),
        name='like_image',
    ),

    url(
        regex=r'(?P<image_id>\d+)/comment/',
        view=views.CommentOnImage.as_view(),
        name='comment_image',
    ),

]