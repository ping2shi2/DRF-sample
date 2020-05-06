from django.urls import path
from .views import *

app_name = 'sample_api'

urlpatterns = [
    path('nested-list/', NestedListView.as_view(), name='nested-list'),
    path('logging-exp/', LoggingExceptListView.as_view(), name='logging-exp'),
]
