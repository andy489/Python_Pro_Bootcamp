# Modify Global Scope

enemies = "Skeleton"


def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
