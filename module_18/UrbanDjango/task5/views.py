from django.shortcuts import render
from .forms import UserRegister
from .user import User, users


def sign_up_by_html(request):
    """
    Функция обрабатывающая запрос без использованиея django.forms.
    :param request: объект запроса.
    :return: представление на основе шаблона - registration_page.html.
    """
    # Проверяем тип запроса (если он POST)
    if request.method == 'POST':
        info = {}

        # Проводим проверку данных и в случае необходимости формируем сообщения об ошибках
        if request.POST.get('password') != request.POST.get('repeat_password'):
            info['error'] = 'Пароли не совпадают'
        elif int(request.POST.get('age')) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif User.in_list(request.POST.get('username'), users):
            info['error'] = 'Пользователь уже существует'
        
        # В случае отсутствия ошибок добавляем нового пользователя и формируем  соответствующее сообщение
        else:
            user = User(
                request.POST.get('username'),
                request.POST.get('password'),
                int(request.POST.get('age'))
            )

            users.append(user)

            info['succes'] = f'Приветствуем, {user.username}!'
        
        return render(request, 'fifth_task/registration_page.html', info)

    # В случае если запрос не POST возвращаем начальную страницу
    else:
        return render(request, template_name='fifth_task/registration_page.html')


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
            info = {}

            # Проводим проверку данных и в случае необходимости формируем сообщения об ошибках
            if f_user.cleaned_data['password'] != f_user.cleaned_data['repeat_password']:
                info['error'] = 'Пароли не совпадают'
            elif int(f_user.cleaned_data['age']) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif User.in_list(f_user.cleaned_data['username'], users):
                info['error'] = 'Пользователь уже существует'

            # В случае отсутствия ошибок добавляем нового пользователя и формируем  соответствующее сообщение
            else:
                user = User(
                    f_user.cleaned_data['username'],
                    f_user.cleaned_data['password'],
                    f_user.cleaned_data['age']
                )

                users.append(user)

                info['succes'] = f'Приветствуем, {user.username}!'
            
            return render(request, 'fifth_task/registration_page.html', info)

    # В случае если запрос не POST возвращаем начальную страницу
    else:
        f_user = UserRegister()
        return  render(request, template_name='fifth_task/registration_page.html')
