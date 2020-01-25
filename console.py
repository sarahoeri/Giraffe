# strings
print("doesn't")
print('doesn\'t')
print('"Yes, we\'ll come", they said')

p = 'First line. \nSecond line. \nThird line'
print(p)

print(r"D:\MOVIES\y. sheldon")

# Lists
lucky_numbers = [1, 3, 5, 37, 32, 27, 18, 22, 12, 19, 25, 35, 27, 11, 29, 30]
phone_models = ["Huawei", "Techno", "Samsung", "Infinix", "Nokia"]
phone_models.extend(lucky_numbers)
phone_models.append("Creed")
phone_models.insert(2, "Kelly")
phone_models.remove("Kelly")
phone_models[3] = "Apple"
phone_models.pop()
lucky_numbers.sort()
lucky_numbers.reverse()

lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)

print(phone_models.index("Nokia"))