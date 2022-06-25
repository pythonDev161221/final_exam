from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from accounts.models import Client

User = get_user_model()

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
        except ObjectDoesNotExist:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:announce_list')
        else:
            context['has_error'] = True
    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:announce_list')


class Profile(DetailView):
    model = Client
    template_name = "accounts/profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data()
        print(context)
        print(context.get('client'))
        print(context.values())
        return context
