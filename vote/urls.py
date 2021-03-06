from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "vote"
urlpatterns = [
    url(r'^$', views.VotePage.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote$', views.vote, name='vote'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r"^(?P<pk>\d+)/results/api_get/$", views.ajax_get, name="ajax_get"),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r'^login/$', LoginView.as_view(template_name="vote/login.html"), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name="admin/base.html"), name='logout'),

]