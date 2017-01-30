from django.conf.urls import url
from thewebapp.views import IndexView, CollegeListView, CollegeDetailView, DetailParticularView, LoginView, RegisterView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search/$', CollegeListView.as_view(), name="search"),
    url(r'^college/$', CollegeDetailView.as_view(), name="collegedetail"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),

    # url for college detail particular ex. Academics, Sports, etc.
    url(r'^college/col-det-particular/$', DetailParticularView.as_view())


]
