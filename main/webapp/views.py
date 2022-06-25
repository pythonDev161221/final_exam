from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import AnnounceForm, AnnounceModerForm
from webapp.models import Announce


class AnnounceListView(ListView):
    model = Announce
    paginate_by = 10
    template_name = "announce/announce_list.html"
    context_object_name = 'announces'


class AnnounceCreateView(CreateView):
    model = Announce
    form_class = AnnounceForm
    template_name = "announce/announce_create.html"
    success_url = reverse_lazy("webapp:announce_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AnnounceUpdateView(UpdateView):
    model = Announce
    form_class = AnnounceForm
    template_name = "announce/announce_update.html"
    success_url = reverse_lazy("webapp:announce_list")


class AnnounceDetailView(DetailView):
    model = Announce
    template_name = 'announce/announce_detail.html'


class AnnounceDeleteView(DeleteView):
    model = Announce
    success_url = reverse_lazy("webapp:announce_list")
    template_name = "announce/announce_delete.html"


class AnnounceNewList(ListView):
    model = Announce
    context_object_name = 'announces'
    template_name = 'announce/moder_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status__exact='new').order_by("-created_at")
        return queryset


class AnnounceModUpdate(UpdateView):
    model = Announce
    template_name = "announce/moder_update.html"
    form_class = AnnounceModerForm
