from django.conf.urls import url
from .views import SignUpView, LogoutView, LoginView, UserDetailView

app_name = 'users'

urlpatterns = [
    url(r'^register/$', SignUpView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^books/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
]
