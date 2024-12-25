from django.shortcuts import render  # type: ignore
from django.views.generic import TemplateView  # type: ignore


# Create your views here.
def func_view(request):
    return render(request, 'second_task/func_template.html')


class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'
