growth_rate = 1.15

curr_population = int(input("Enter current population: "))
future_population = curr_population * (growth_rate ** 5)
print("Population after 5 years:", int(future_population))
