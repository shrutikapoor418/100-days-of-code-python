################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
def fun():
  def drink_potion():
    potion_strength=2
    print(potion_strength)
   print(potion_strength)
fun()
