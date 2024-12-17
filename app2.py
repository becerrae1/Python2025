from app import Hat

hat_1 = Hat("Nike", "Blue", "Yankee", "No Brim")

print(hat_1.make)
print(hat_1.color)
print(hat_1.brand)
print(hat_1.brim)

hat_1.fit()
hat_1.hellYeah()


colors = ["magenta", "blue", "green"]

colors.append("Purple")

colors.extend([1, 2, 3])
print(colors)

print(len(colors))