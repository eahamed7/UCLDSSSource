from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(
        r'^course-autocomplete/$',
        views.CourseAutoComplete.as_view(),
        name='course-autocomplete',
    ),


] 