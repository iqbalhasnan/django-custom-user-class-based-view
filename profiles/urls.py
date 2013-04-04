from django.conf.urls import patterns, include, url
from profiles.views import UserListView, UserDetailView, MessageAccountUserEdit, MessageProfileUserEdit
from django.conf import settings


urlpatterns = patterns('',
    url(r"^accounts/profile/$", UserListView.as_view(), name="user_list"),
    #index homepage
    url(r"^(?P<slug>[\w-]+)/$", UserDetailView.as_view(), name="user_detail"),
    #serve static file
    url(r"^user/settings/account/(?P<pk>[\w-]+)/$", MessageAccountUserEdit.as_view(), name="user_account_edit"),
    url(r"^user/settings/profile/(?P<pk>[\w-]+)/$", MessageProfileUserEdit.as_view(), name="user_profile_edit"),
)

