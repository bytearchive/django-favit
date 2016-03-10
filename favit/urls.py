from django.conf.urls import patterns, url

from .views import add_or_remove, remove


urlpatterns = [
    url(r'^add-or-remove$', add_or_remove),
    url(r'^remove$', remove),
]
