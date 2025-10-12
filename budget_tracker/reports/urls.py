from django.urls import path
from .views import SummaryView, FilterView

urlpatterns = [
    path('summary/', SummaryView.as_view(), name='summary'),
    path('filter/', FilterView.as_view(), name='filter'),
]