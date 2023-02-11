import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

'''Function creates a list of 30 products with a randomly
   generated name, price, weight, and flammability.'''


def generate_products(num_products=30):
    prod_list = []
    for i in range(0, num_products):
        adj = random.sample(ADJECTIVES, 1)
        nou = random.sample(NOUNS, 1)
        name = adj[0] + " " + nou[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prod_list.append(Product(name, price, weight, flammability))
    return prod_list


'''This function returns a tuple of the number of unique
   product names, the average price, the average weight,
   and the average flammability'''


def inventory_report(prod_list):
    unique = set([i.name for i in prod_list])
    mean_price = sum([i.price for i in prod_list])/len(prod_list)
    mean_weight = sum([i.weight for i in prod_list])/len(prod_list)
    mean_flammability = sum([i.flammability for i in prod_list])/len(prod_list)
    return (len(unique), mean_price, mean_weight, mean_flammability)


if __name__ == '__main__':
    print(inventory_report(generate_products(num_products=30)))
