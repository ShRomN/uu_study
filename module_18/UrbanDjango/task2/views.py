from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def func_view(request):
    """
    Функция возвращающая представление с помощью функционального подхода.
    :param request: объект запроса.
    :return: представление на основе шаблона - func_template.html.
    """
    return render(request, template_name='second_task/func_template.html')


class ClassView(TemplateView):
    """
    Класс илюстрирующий использование классового подхода возвращения представления.
    """
    # Используемый шаблон представления
    template_name = 'second_task/class_template.html'
