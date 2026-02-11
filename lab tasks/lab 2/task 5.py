import numpy as np
data = np.arange(1, 7*24 + 1).reshape(7, 24)
print("Complete Sensor Data (7 days x 24 hours):")
print(data)

day1_every_other = data[0, ::2]
print("\nEvery other hour from Day 1:")
print(day1_every_other)


first_12_all_days = data[:, :12]
print("\nFirst 12 hours for all days:")
print(first_12_all_days)

every_6th_hour = data[:, ::6]
print("\nEvery 6th hour across the week:")
print(every_6th_hour)

last_three_days = data[4:7, :]
print("\nLast three days (Day 5 to Day 7):")
print(last_three_days)

day3_reversed = data[2, ::-1]
print("\nReversed hourly data for Day 3:")
print(day3_reversed)

first4_every_3rd = data[:4, ::3]
print("\nEvery 3rd hour from first 4 days:")
print(first4_every_3rd)
