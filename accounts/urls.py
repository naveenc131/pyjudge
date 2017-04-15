from django.conf.urls import url
from django.contrib.auth import views
from .forms import LoginForm
#from . import views as oview


urlpatterns = [
				url(r'login', views.login,{'template_name': 'login_form.html', 'authentication_form': LoginForm}, name='login'),
				#url(r'logout_view', oviews.logout_view, name='logout'),

				]