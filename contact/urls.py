from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListOfContactView.as_view(),name='list_of_contacts'),
    url(r'^(?P<pk>[0-9]+)/$', views.ContactDetailsView.as_view(), name='detail'),
    url(r'^add/$', views.ContactCreate.as_view(), name='add'),
]