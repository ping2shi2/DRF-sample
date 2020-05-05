from django.urls import path
from .views import NestedListView

app_name = 'sample_api'

urlpatterns = [
    path('nested-list/', NestedListView.as_view(), name='nested-list'),
]
