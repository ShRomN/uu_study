import numpy as np
# import matplotlib.pyplot as plt

class Gridworld:
    """
    Класс описывающий объект Gridworld.
    """
    def __init__(self, N:int=5, M:int=5, start_state=(0, 0), target_state=None, alpha=0.1, num_episodes=10, gamma=0.9, epsilon=0.1):
        """
        Конструктор класса Gridworld.
        :param N: размер поля по вертикали;
        :param M: размер поля по горизонтали;
        :param start_state: местоположение начального состояния обучения;
        :param target_state: местоположение целевого состояния обучения;
        :param alph: шаг обучения (learning rate);
        :param num_episodes: количество эпизодов обучения (итераций);
        :param gamma: коэффициент дисконтирования (discount factor);
        :param epsilon: вероятность случайного действия.
        """
        self.N = N
        self.M = M
        self.start_state = start_state

        if target_state is None:
            self.target_state = (self.N - 1, self.M - 1)
        else:
            self.target_state = target_state

        self.alpha = alpha
        self.num_episodes = num_episodes
        self.gamma = gamma
        self.epsilon = epsilon

        self.actions = [
            {'name': 'вверх', 'move': (-1, 0)},
            {'name': 'вниз', 'move': (1, 0)},
            {'name': 'влево', 'move': (0, -1)},
            {'name': 'вправо', 'move': (0, 1)}
        ]

        self.game_field = self._game_field_init()
        self.Q_table = self._Q_table_init()
        self.states = self._states_init()
        self.rewards = self._rewards_init()

    def _game_field_init(self):
        """
        Метод создания поля и инициализации его.
        """
        return np.zeros((self.N, self.M))
    
    def _Q_table_init(self):
        """
        Метод создания и инициализации Q-таблицы нулевыми значениями.
        """
        return np.zeros((self.N, self.M, len(self.actions)))
    
    def _Q_table_reset(self):
        """
        Метод сброса значений Q-таблицы до первоначального состояния.
        """
        self._Q_table_init()
    
    def _states_init(self):
        """
        Метод создания и инициализации таблицы состояний.
        """
        return [(i, j) for i in range(self.N) for j in range(self.M)]

    def _rewards_init(self):
        """
        Метод создания и инициализации таблицы вознаграждений.
        """
        r_table = np.full((self.N, self.M), -0.1)
        r_table[self.target_state] = 1.0
        print(r_table)
        return r_table
        
        # return np.array([[-0.1, -0.1, -0.1, -0.1, -0.1],
        #                 [-0.1, -0.1, -0.1, -0.1, -0.1],
        #                 [-0.1, -0.1, -0.1, -0.1, -0.1],
        #                 [-0.1, -0.1, -0.1, -0.1, -0.1],
        #                 [-0.1, -0.1, -0.1, -0.1, 1.0]])

        # return np.array([[0, -1, -1, -1, -1],
        #                 [-1, -1, -1, -1, -1],
        #                 [-1, -1, -1, -1, -1],
        #                 [-1, -1, -1, -1, -1],
        #                 [-1, -1, -1, -1, 10]])
        
        # return np.array([[1, 1, 1, 1, 1],
        #                 [1, 1, 1, 1, 1],
        #                 [1, 1, 1, 1, 1],
        #                 [1, 1, 1, 1, 1],
        #                 [1, 1, 1, 1, 0]])


    def choose_action(self, state):
        """
        Выбора следующего действия.
        :param state: текущее состояние.
        :return: оптимальное или случайное действие.
        """
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions) # случайное действие
        else:
            action = self.actions[np.argmax(self.Q_table[state])] # оптимальное действие

        return action

    def train_Q_learning(self):
        """
        Метод обучения модели с использованием алгоритма Q-Learning.
        """
        # Сбрасываем значения Q-таблицы перед обучением
        self._Q_table_reset()

        # Основной цикл обучения
        for _ in range(self.num_episodes):
            state = self.start_state # начальное состояние
            
            while state != self.target_state: # пока агент не достигнет целевой клетки
                action = self.choose_action(state) # определяем действие
                next_state = self.make_move(state, action) # получение следующего состояния
                reward = self.rewards[next_state] # получение награды
                best_next_action = self.actions[np.argmax(self.Q_table[next_state])]
                self.Q_table[state][self.actions.index(action)] += self.alpha * ((reward + self.gamma * self.Q_table[next_state][self.actions.index(best_next_action)]) - self.Q_table[state][self.actions.index(action)]) # обновление Q-значения
                state = next_state


    def train_sarsa(self):
        """
        Метод обучения модели с использованием алгоритма SARSA.
        """
        # Сбрасываем значения Q-таблицы перед обучением
        self._Q_table_reset()

        # Основной цикл обучения
        for _ in range(self.num_episodes):
            state = self.start_state
            
            while state != self.target_state: # пока агент не достигнет целевой клетки
                action = self.choose_action(state) # определяем действие
                next_state = self.make_move(state, action) # получение следующего состояния
                reward = self.rewards[next_state] # получение награды
                next_action = self.choose_action(next_state) # выбор следующего действия
                self.Q_table[state][self.actions.index(action)] += self.alpha * ((reward + self.gamma * self.Q_table[next_state][self.actions.index(next_action)]) - self.Q_table[state][self.actions.index(action)])
                state, action = next_state, next_action # обновление состояния
  
    def make_move(self, state, action):
        """
        Метод передвижения.
        :param state: текущее состояние;
        :param action: применяемое действие (направление передвижения).
        :return: оптимальное или случайное действие.
        """
        next_state = (state[0] + action['move'][0], state[1] + action['move'][1])
        if next_state[0] < 0 or next_state[0] >= self.N or next_state[1] < 0 or next_state[1] >= self.M:
            next_state = state  # оставаться на месте, если выходит за пределы

        return next_state
    
    def show_Q_table(self):
        """
        Метод отображения Q-таблицы.
        """
        print(np.argmax(self.Q_table, axis=2))

    # def plot_Q_table(self):
    #     """
    #     Метод графического отображения Q-таблицы.
    #     """
    #     # Функция ценности
    #     value_function = np.max(self.Q_table, axis=2)

    #     plt.figure(figsize=(10, 6))

    #     # Политика
    #     policy = np.argmax(self.Q_table, axis=2)

    #     plt.subplot(1, 2, 1)
    #     plt.title('Политика')
    #     plt.imshow(policy, cmap='viridis', origin='upper')
    #     for i in range(self.N):
    #         for j in range(self.N):
    #             plt.text(j, i, policy[i, j], ha='center', va='center', color='white')

    #     # Функция ценности
    #     plt.subplot(1, 2, 2)
    #     plt.title('Функция ценности')
    #     plt.imshow(value_function, cmap='viridis', origin='upper')
    #     for i in range(self.N):
    #         for j in range(self.N):
    #             plt.text(j, i, round(value_function[i, j], 2), ha='center', va='center', color='white')

    #     plt.show()
        

gw = GridworldSarsa()

gw.train_Q_learning()
gw.show_Q_table()
# gw.plot_Q_table()

gw.train_sarsa()
gw.show_Q_table()
# gw.plot_Q_table()
