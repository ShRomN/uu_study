from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


class MainPageView(TemplateView):
    """
    Класс представления для главной страницы в приложении
    """
    # Используемый шаблон представления для главной страницы
    template_name = 'main_page_template.html'


class GamesPageView(TemplateView):
    """
    Класс представления для страницы со списком игр.
    """
    # Используемый шаблон представления для страницы со списком игр. 
    template_name = 'games_page_template.html'
    
    def get_context_data(self, **kwargs):
        """
        Метод формирования контекста.
        """
        context = super().get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context


class CartPageView(TemplateView):
    """
    Класс представления для страницы с корзиной покупок.
    """
    # Используемый шаблон представления для страницы со списком избранных фильмов. 
    template_name = 'cart_page_template.html'



def sign_up_by_django(request):
    """
    Функция обрабатывающая запрос с использованием django.forms.
    :param request: объект запроса.
    :return: представление на основе шаблона - registration_page.html.
    """
    # Проверяем тип запроса (если он POST)
    if request.method == 'POST':
        # Создаем объект формы
        f_user = UserRegister(request.POST)

        # Проводим валидацию формы
        if f_user.is_valid():
            # Проводим проверку данных и в случае необходимости формируем сообщения об ошибках
            info = {}

            # Проверка соответствия паролей
            if f_user.cleaned_data['password'] != f_user.cleaned_data['repeat_password']:
                info['error'] = 'Пароли не совпадают'
            # Проверка возраста (старше 18)
            elif int(f_user.cleaned_data['age']) < 18:
                info['error'] = 'Вы должны быть старше 18'
            # Проверка отсутствия регистрирующегося пользователя на отсутствие никнейма в БД
            elif Buyer.objects.filter(name=f_user.cleaned_data['username']).exists():
                info['error'] = 'Пользователь уже существует'

            # В случае отсутствия ошибок (прохождения всех проверок) добавляем нового пользователя в БД
            else:
                buyer = Buyer.objects.create(
                    name=f_user.cleaned_data['username'],
                    password=hash(f_user.cleaned_data['password']),
                    balance=0,
                    age=int(f_user.cleaned_data['age'])
                )

                info['succes'] = f'Приветствуем, {str(buyer)}!'
            
            return render(request, 'registration_page.html', info)

    # В случае если запрос не POST возвращаем начальную страницу
    else:
        f_user = UserRegister()
        return  render(request, template_name='registration_page.html')
