import random

if __name__ == "__main__":
    # these three attributes exist in random
    random_attr = random.choice(("gammavariate", "lognormvariate", "normalvariate"))
    # get one of three functions in random
    random_func = getattr(random, random_attr)
    # call the function
    print(f"A {random_attr} random value: {random_func(1, 1)}")
    pass
