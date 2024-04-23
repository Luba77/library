from django.views import generic


class BaseView(generic.TemplateView):
    template_name = 'index.html'
