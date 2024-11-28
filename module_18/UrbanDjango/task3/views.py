from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """
    Класс представления для главной страницы в приложении - task3
    """
    # Используемый шаблон представления для главной страницы
    template_name = 'third_task/main_page_template.html'


class MoviesPageView(TemplateView):
    """
    Класс представления для страницы со списком фильмв.
    """
    # Используемый шаблон представления для страницы со списком фильмов. 
    template_name = 'third_task/movies_page_template.html'

    def get_context_data(self, **kwargs):
        """
        Метод формирования контекста.
        """
        context = super().get_context_data(**kwargs)
        context['movies'] = {
            'movie1': 'Москва слезам не верит',
            'movie2': 'Летят журавли',
            'movie3': 'Они сражались за Родину'
        }
        return context


class FavoritesPageView(TemplateView):
    """
    Класс представления для страницы с избранными фильмами.
    """
    # Используемый шаблон представления для страницы со списком избранных фильмов. 
    template_name = 'third_task/favorites_page_template.html'