import random
random_num_generator = random.randint(10,20)
print(random_num_generator)

random_float_generator = random.uniform(10,20)
print(random_float_generator)

random_num = random.random() *23
print(random_num)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")