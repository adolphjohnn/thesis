from django.urls import path
from .views import login_user, qanda, change, dashboard, signout, session,course,logs,feedback,searchBar,rate
from .import views 

urlpatterns = [
    path('', views.home, name="home"),
    
    path('session/', session, name="session"),
    path('editView/<code>', views.editView),
    path('courseView/<code>', views.courseView),
    path('levelView/<code>', views.levelView),
    path('dashboard/', dashboard, name="dashboard"),
    path('signout', signout, name="signout"),
    path('login_user/', login_user, name="login_user"),
    path('qanda/', qanda, name="qanda"),
    path('search/', views.searchBar, name='search'),
    path('course/', course, name="course"),
    path('logs/', logs, name="logs"),
    path('feedback/', feedback, name="feedback"),
    path('rate/', rate, name="rate"),
    path('change/', change, name="change"),
    path('deleteLogs/<code>', views.deleteLogs),
    path("indexhom/", views.indexhom, name="indexhom"),
    path("get-value", views.getValue),

]