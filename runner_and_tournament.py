class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        # Добавлена сортировка по убыванию
        self.participants = sorted(list(participants), key=lambda x: x.speed, reverse=True)

    def start(self):
        # ------- 1-й вариант -------
        # finishers = {}
        # place = 1
        # while self.participants:
        #     for participant in self.participants:
        #         participant.run()
        #         if participant.distance >= self.full_distance:
        #             # Изменено формирование значений словаря
        #             finishers[place] = str(participant)
        #             place += 1
        #             self.participants.remove(participant)
        # ----------------------------

        # ------- 2-й вариант -------
        finishers = dict(map(lambda x: (x[0] + 1, str(x[1])), enumerate(self.participants)))
        self.participants.clear()
        # ----------------------------


        return finishers
