class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def start(self):
        print(f"{self.brand} {self.model} ({self.year}) заводится.")

class Garage:
    def __init__(self):# Убедитесь что вы в правильной директории с файлом main.py
    # Создаем .gitignore
    echo "__pycache__/" > .gitignore
    echo "*.pyc" >> .gitignore
    echo ".idea/" >> .gitignore
    echo "venv/" >> .gitignore

    # Создаем README.md
    echo "# Система управления гаражом" > README.md
    echo "" >> README.md
    echo "Проект на Python для управления автомобилями в гараже." >> README.md
    echo "" >> README.md
    echo "## Функционал" >> README.md
    echo "- Добавление автомобилей" >> README.md
    echo "- Просмотр списка автомобилей" >> README.md
    echo "- Удаление автомобилей" >> README.md

    # Инициализируем Git и добавляем файлы
    git init
    git add main.py .gitignore README.md
    git commit -m "Первоначальная версия проекта"
    git branch -M master
    git remote add origin https://github.com/ViltrumiteWarrior/random-project-in-lesson.git
    git push -u origin master# Убедитесь что вы в правильной директории с файлом main.py
    # Создаем .gitignore
    echo "__pycache__/" > .gitignore
    echo "*.pyc" >> .gitignore
    echo ".idea/" >> .gitignore
    echo "venv/" >> .gitignore

    # Создаем README.md
    echo "# Система управления гаражом" > README.md
    echo "" >> README.md
    echo "Проект на Python для управления автомобилями в гараже." >> README.md
    echo "" >> README.md
    echo "## Функционал" >> README.md
    echo "- Добавление автомобилей" >> README.md
    echo "- Просмотр списка автомобилей" >> README.md
    echo "- Удаление автомобилей" >> README.md

    # Инициализируем Git и добавляем файлы
    git init
    git add main.py .gitignore README.md
    git commit -m "Первоначальная версия проекта"
    git branch -M master
    git remote add origin https://github.com/ViltrumiteWarrior/random-project-in-lesson.git
    git push -u origin master
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for i, car in enumerate(self.cars):
            print(f"{i + 1}: {car}")

    def remove_car(self, index):
        if 0 <= index < len(self.cars):
            removed_car = self.cars.pop(index)
            print(f"Удалена машина: {removed_car}")
        else:
            print("Нет такой машины")

garage = Garage()

cars = [
    Car("Toyota", "Camry", 2020),
    Car("BMW", "X5", 2021),
    Car("Mercedes", "E-Class", 2019),
    Car("Audi", "A6", 2022),
    Car("Honda", "Civic", 2021),
    Car("Volkswagen", "Golf", 2020),
    Car("Tesla", "Model 3", 2022),
    Car("Porsche", "911", 2021),
    Car("Lexus", "RX", 2020),
    Car("Ford", "Mustang", 2022)
]

for car in cars:
    garage.add_car(car)
    car.start()

print("\nСписок всех машин в гараже:")
garage.show_cars()

print("\nУдаляем машину с индексом 0:")
garage.remove_car(0)

print("\nОбновленный список машин:")
garage.show_cars()