class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация экземпляра класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self._name = name  # Непубличный атрибут, чтобы скрыть детали реализации
        self._age = age    # Непубличный атрибут, чтобы скрыть детали реализации

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.
        По умолчанию возвращает "Some sound".
        """
        return "Some sound"

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return f"{self.__class__.__name__}(Name: {self._name}, Age: {self._age})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление животного.
        """
        return f"{self.__class__.__name__}(name='{self._name}', age={self._age})"

    class Dog(Animal):
        """
        Класс для собак, наследующий от класса Animal.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            Инициализация экземпляра класса Dog.

            :param name: Имя собаки.
            :param age: Возраст собаки в годах.
            :param breed: Порода собаки.
            """
            super().__init__(name, age)  # Вызов конструктора базового класса
            self.breed = breed  # Публичный атрибут для хранения породы собаки

        def speak(self) -> str:
            """
            Метод, который возвращает звук, издаваемый собакой.

            Переопределен, чтобы вернуть специфический звук для собак.
            """
            return "Woof!"

        def __str__(self) -> str:
            """
            Возвращает строковое представление собаки.
            """
            return f"{super().__str__()}, Breed: {self.breed}"

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление собаки.
            """
            return f"{super().__repr__()}, breed='{self.breed}'"

        class Cat(Animal):
            """
            Класс для кошек, наследующий от класса Animal.
            """

            def __init__(self, name: str, age: int, color: str) -> None:
                """
                Инициализация экземпляра класса Cat.

                :param name: Имя кошки.
                :param age: Возраст кошки в годах.
                :param color: Цвет кошки.
                """
                super().__init__(name, age)  # Вызов конструктора базового класса
                self.color = color  # Публичный атрибут для хранения цвета кошки

            def speak(self) -> str:
                """
                Метод, который возвращает звук, издаваемый кошкой.

                Переопределен, чтобы вернуть специфический звук для кошек.
                """
                return "Meow!"

            def __str__(self) -> str:
                """
                Возвращает строковое представление кошки.
                """
                return f"{super().__str__()}, Color: {self.color}"

            def __repr__(self) -> str:
                """
                Возвращает официальное строковое представление кошки.
                """
                return f"{super().__repr__()}, color='{self.color}'"

            if __name__ == "__main__":
                dog = Dog(name="Buddy", age=3, breed="Golden Retriever")
                cat = Cat(name="Whiskers", age=2, color="Black")

                print(dog)  # Выводит информацию о собаке
                print(cat)  # Выводит информацию о кошке
                print(dog.speak())  # Выводит звук собаки
                print(cat.speak())  # Выводит звук кошки