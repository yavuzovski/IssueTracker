from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name="main"),
    # url(r'^issues/new$', AddIssueView.as_view(), name="new_issue")
]
