from django.conf.urls import url
from .views import SignUpView, LogoutView, LoginView

app_name = 'users'

urlpatterns = [
    url(r'^register/$', SignUpView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
