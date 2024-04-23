from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, View, FormView
from .forms import UserLoginForm, UserSignUpForm
from .models import User


class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = User.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        user = authenticate(
            request=self.request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())

        return super(LoginView, self).get(self, request, *args, **kwargs);

    def form_valid(self, form):
        user = authenticate(email=form.cleaned_data['email'],
                            password=form.cleaned_data['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)


class LogoutView(View):
    success_url = reverse_lazy('home')

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(self.success_url)










