from time import sleep


class User:
    """
    Класс описывающий объект пользователя User.
    """

    def __init__(self, nickname: str, password: str, age: int = 0):
        """
        Конструктор класса User.
        :param nickname: имя пользователя;
        :param password: пароль пользователя;
        :param age: возраст пользователя.
        """
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self) -> int:
        """
        Метод возвращающий hash объекта User.
        """
        # return hash((self.nickname, self.password))
        return hash(self.nickname)

    def __eq__(self, other):
        """
        Метод (перегрузка оператора ==)  проверки равенства двух объектов self и объект other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, User) and hash(self) == hash(other)

    def __str__(self):
        """
        Метод вывода строкового представлнгия объекта User.
        """
        return self.nickname


class Video:
    """
    Класс описывающий объект видео Video.
    """

    def __init__(self, title: str, duration: int = 0, time_now: int = 0, adult_mode: bool = False):
        """
        Конструктор класса Video.
        :param title: заголовок видео;
        :param duration: продолжительность видео в секундах;
        :param time_now: секунда остановки;
        :param adult_mode: ограничение по возрасту.
        """
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __hash__(self) -> int:
        """
        Метод возвращающий hash объекта Video.
        """
        return hash(self.title)

    def __eq__(self, other):
        """
        Метод (перегрузка оператора ==)  проверки равенства двух объектов self и объект other.
        Атрибуты:
        other - 2-й объект для сравнения.
        """
        return isinstance(other, Video) and hash(self) == hash(other)


class UrTube:
    """
    Класс описывающий объект UrTube.
    """

    def __init__(self, users=None, videos=None, current_user: User = None):
        """
        Конструктор класса UrTube.
        :param users: список пользователей;
        :param videos: список видео;
        :param current_user: текущий пользователь.
        """
        if users is None:
            self.users = []
        else:
            self.users = users

        if videos is None:
            self.videos = []
        else:
            self.videos = videos

        self.current_user = current_user

    def log_in(self, nickname: str, password: str):
        """
        Метод для входа в аккаунт.
        :param nickname: имя пользователя;
        :param password: пароль пользователя.
        :return: True если вход осуществлен корректно иначе False.
        """
        user = User(nickname, password)
        if user in self.users:
            user = self.users[self.users.index(user)]
            self.current_user = user
            return True
        else:
            return False

    def register(self, nickname: str, password: str, age: int):
        """
        Метод для регистрации пользователя.
        :param nickname: имя пользователя;
        :param password: пароль пользователя;
        :param age: возраст пользователя.
        """
        user = User(nickname, password, age)
        if user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.log_in(nickname, password)

    def log_out(self):
        """
        Метод для выхода текущего пользователя из аккаунта.
        """
        self.current_user = None

    def add(self, *args):
        """
        Метод для добавления видео.
        :param args: добавление объектов Video в список videos.
        """
        for video in args:
            if video in self.videos:
                pass
            else:
                self.videos.append(video)

    def get_videos(self, string=''):
        """
        Метод возвращающий список заголовков объектов Vidoe содержащихся в списке self.videos
        и содержащие в себе стоку string.
        :param string: строка поиска требуемых заголовков в списоке self.videos.
        :return: список заголовков удовлетворяющих критериям поиска.
        """
        return list(filter(lambda y: string.lower() in y.lower(), map(lambda x: x.title, self.videos)))

    def watch_video(self, title=''):
        """
        Метод возвращающий список заголовков объектов Vidoe содержащихся в списке self.videos
        и содержащие в себе стоку title.
        :param title: заголовок искомого видео в списоке self.videos.
        :return: список заголовков удовлетворяющих критериям поиска.
        """
        video = Video(title)
        if video in self.videos:
            video = self.videos[self.videos.index(video)]
            if self.current_user is None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            elif self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for i in range(video.time_now if video.time_now > 0 else 1, video.duration + 1):
                    print(i, end=' ')
                    sleep(1)
                print('Конец видео')
                video.time_now = 0
        else:
            pass


# Тестовые данные
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
