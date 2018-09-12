class animals:
  def __init__(self, new_name, new_color, new_weight,new_satiety):
    self.name = new_name
    self.color = new_color
    self.weight = new_weight
    self.satiety = new_satiety
  description = "какое-то животное..."
  voice = "издаёт какие-то звуки..."
  def food(self):
    if self.satiety >= 0 :return " \n животное нужно кормить\n"
    return " \n животное сыто\n"
  def annotation(self):
    return self.name + "цвет" + self.color + "," + str(self.weight) + "кг," + "издает:" + self.voice + self.food()

# Абстрактные млекопитающие

class mammal(animals):
  milk = 0
  wool = 0
  def fresh_product(self):
    if self.wool >= 1 and self.milk <= 0 :
      return "\n Получено килограмм шерти: " + str(self.wool)
    if self.milk >= 1 and self.wool <= 0 :
      return "\n Получено литров молока: " + str(self.milk)
    if self.milk >= 1 and self.wool >= 1 :
      return "\n Получено килограмм шерти: " + str(self.wool) + "\n Получено литров молока: " + str(self.milk)
    else:
      return "\n Животное не даёт молоко или шерсть"

  def annotation(self):
    return  self.name + ":\n Цвет: " + self.color +"\n" + " Вес " + str(self.weight) + " кг, \n Издает: " + self.voice + self.fresh_product() + self.food()

# Абстрактные птицы

class birds(animals):
  eggs = 0

  def get_eggs(self):
    if self.eggs >= 1 :
      return "\n Получено яиц: " + str(self.eggs)
    else :
      return "\n Птица не даёт яйца... :-("
  def annotation(self):
    return self.name + ":\n цвет: " + self.color +"\n" + " вес " + str(self.weight) + " кг, \n издает: " + self.voice + self.get_eggs() + self.food()

# Реальные животные

class ducks(birds):
  voice = "кря-кря!"


class goose(birds):
  voice = "га-га-га!"

class chicken(birds):
  voice = "О-ко-ко-ко-ко!"
  satiety=15

class cows(mammal):
  milk = 7
  voice = "му-у-у-у-у!!!"
  
class goats(mammal):
  milk = 3
  voice = "бе-е!!!"

class sheeps(mammal):
  wool = 5
  voice = "ба-а-аэ!!!"

grey = goose("Cерый", "серый", 2.5, 11)
grey.eggs = 0
print("гусь:", "\n", grey.annotation())
white = goose("Белый", "белый", 2.4, 0)
white.eggs = 0
print("гусь:", "\n", white.annotation())
manka = cows("Манька", "черный", 600, 12)
print("корова:", "\n", manka.annotation())
barash = sheeps ("Барашек", "берый", 78, 4)
print("овца:", "\n", barash.annotation())
kudriash = sheeps ("Кудрявый", "берый", 82, 15)
print("овца:", "\n", kudriash.annotation())
shanel = chicken ("Ко-ко", "тёмно-красный", 0.5, 16)
shanel.eggs = 10
print("курица:", "\n", shanel.annotation())
cwohch = chicken ("Кукареку", "тёмно-красный", 0.5, 0)
cwohch.eggs = 10
print("курица:", "\n", cwohch.annotation())
horns = goats ("Рога", "серый", 90, -3)
horns.milk = 4
print("коза:", "\n", horns.annotation())
hooves = goats ("Копыта", "серый", 70, 0)
horns.milk = 3
print("коза:", "\n", hooves.annotation())
lagy_gaga = ducks ("Кряква", "тёмно-красный", 0.5, 99)
lagy_gaga.eggs = 5
print("утка:", "\n", lagy_gaga.annotation())

list_animals = [grey, white, manka, barash, kudriash, shanel, cwohch, horns, hooves, lagy_gaga]
max_weight = 0
sum_weight = 0
count_animals = 0

for animal in list_animals:
  sum_weight += animal.weight 
  count_animals += 1
  if animal.weight > max_weight:
    max_weight = animal.weight
    name_max_weight = animal.name

print ("Больше всех весит " + str(name_max_weight) + ", его(её  ) вес = " + str(max_weight) + ". \nВсего животные весят " + str(sum_weight) + "\nКол-во животных = " + str(count_animals) + ".\nИли кол-во животных через функцию len = " + str(len(list_animals)))
kg = sum_weight / count_animals

print("Средний вес животного: " + str(int(kg)) + " киллограмма")