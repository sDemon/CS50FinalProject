from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from loginsys.views import login, logout, register

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^password_reset/$', password_reset, {'template_name': 'reset/password_reset_form.html', 'post_reset_redirect': 'password_reset_done', 'email_template_name': 'reset/password_reset_email.html'}, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, {'template_name': 'reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'reset/password_reset_confirm.html', 'post_reset_redirect': 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', password_reset_complete, {'template_name': 'reset/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^login/$', login, name='login'),
]