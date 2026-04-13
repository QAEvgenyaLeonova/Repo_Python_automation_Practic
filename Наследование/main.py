from cats import Cat

# Создаём объект класса Cat
my_cat = Cat('Барсик', 'Рыжий')

# Вызываем методы:
my_cat.make_sound() # Барсик говорит: Мяу! (переопределённый метод)
my_cat.eat() # Барсик ест. (унаследованный метод)
my_cat.purr() # Барсик мурлычет: Мурр-мурр! (новый метод)

print(f'Имя: {my_cat.name}')
print(f'Вид: {my_cat.species}')
print(f'Цвет: {my_cat.color}')
