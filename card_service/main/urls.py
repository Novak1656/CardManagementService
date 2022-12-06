from django.urls import path
from .views import CardListView, CardGeneratorView

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('cards/generate/', CardGeneratorView.as_view(), name='card_generate'),
    path('cards/delete/', CardGeneratorView.as_view(), name='card_delete'),
]
