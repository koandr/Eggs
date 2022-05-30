from random import randint
print("Свято пасхи")
class Eggs:
    def __init__(self, t, v):
        self.hardness = t
        self.speed = v

    def interaction(self):
        return self.hardness * self.speed

print("Казка про курочку Рябу")
print("Жили - були дід та баба, і була у них курочка Ряба.\n"
      "І знесла вона два яєчка")
a = input("Введіть 1, якщо справляєте свято Христового Воскресіння,\n"
          "або інший символ, якщо ні")
print(a)
if a != 1:

    print("І виросло в них два півня.\n"
          "Ось і казочці кінець,\n"
          "добрий з півнів холодець")

else:

    egg1 = Eggs(randint(1, 3), randint(1, 3))
    egg2 = Eggs(randint(1, 3), randint(1, 3))

    if egg1.interaction() > egg2.interaction():
        print("Перше яйце перемогло, міцності залишилось",
              round((egg1.interaction() - egg2.interaction()) / egg1.speed))
    elif egg2.interaction() > egg1.interaction():
        print("Друге яйце перемогло, міцності залишилось",
              round((egg2.interaction() - egg1.interaction()) / egg2.speed))
    else:
        print("Нічия")


