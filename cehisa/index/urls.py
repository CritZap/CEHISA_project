from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'index.views.index'),
)

