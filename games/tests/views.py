from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Game, User, OnlineGameStore
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic




def like(request, pk):
    game_details = get_object_or_404(Game, pk=request.POST["game_id"])
    liked = False
    if game_details.likes.filter(id=request.user.id).exists():
        game_details.likes.remove(request.user)

    else:
        game_details.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('tests:detail', args=[str(pk)]))



class DetailView(generic.DetailView):
    model = Game
    template_name = 'tests/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Game, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        print(total_likes)
        return context

    def __str__(self):
        return self.get_game_genre_display()


class StoreView(generic.DetailView):
    model = OnlineGameStore
    template_name = 'tests/online_store.html'


class IndexView(generic.ListView):
    template_name = 'tests/index.html'
    context_object_name = 'latest_game_list'

    def get_queryset(self):
        """Return the last five published games."""
        return Game.objects.order_by('-rel_date')[:5]
