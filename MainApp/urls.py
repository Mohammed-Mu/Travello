from django.urls import path
from . import views


urlpatterns=[
    path("",views.home, name="home"),
    path("index",views.home, name="home"),
    path("home",views.home, name="home"),
    path("about",views.about,name="about"),
    path("admins",views.admin,name="admin"),
    path("add_page",views.add_page,name="add_page"),
    path("view_page",views.view_page,name="view_page"),
    path("del_page",views.del_page,name="del_page"),
    path("del_page",views.del_page,name="del_page"),
    path("enter",views.enter,name="enter"),
    path("update_data",views.update_data,name="update_data"),
    path('update?ids=<str:id>',views.update,name="update"),
    path("dashboard",views.dashboard, name="dashboard"),
]