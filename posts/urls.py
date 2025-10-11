from django.urls import path
from .views import HomepageView, PostCreateView

urlpatterns = [
	path("", HomepageView.as_view(), name="home"),
	path("add/", PostCreateView.as_view(), name="add_post"),

]