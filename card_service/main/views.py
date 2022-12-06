from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView
from .models import Card


class CardListView(ListView):
    model = Card
    template_name = 'main/card_list.html'
    context_object_name = 'cards'


class CardGeneratorView(RedirectView):
    url = reverse_lazy('card_list')

    def get(self, request, *args, **kwargs):

        return super(CardGeneratorView, self).get(request, *args, **kwargs)


class CardDeleteView(RedirectView):
    url = reverse_lazy('card_list')

    def get(self, request, *args, **kwargs):
        card_pk = request.GET.get('card_pk')
        card = get_object_or_404(Card, pk=card_pk)
        card.delete()
        return super(CardDeleteView, self).get(request, *args, **kwargs)
