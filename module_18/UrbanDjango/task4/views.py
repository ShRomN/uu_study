from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """
    Класс представления для главной страницы в приложении - task4
    """
    # Используемый шаблон представления для главной страницы
    template_name = 'fourth_task/main_page_template.html'


class MoviesPageView(TemplateView):
    """
    Класс представления для страницы со списком фильмв.
    """
    # Используемый шаблон представления для страницы со списком фильмов. 
    template_name = 'fourth_task/movies_page_template.html'
    context = {
        'movie_1': 'Москва слезам не верит',
        'movie_2': 'Летят журавли',
        'movie_3': 'Они сражались за Родину'
    }


class FavoritesPageView(TemplateView):
    """
    Класс представления для страницы с избранными фильмами.
    """
    # Используемый шаблон представления для страницы со списком избранных фильмов. 
    template_name = 'fourth_task/favorites_page_template.html'