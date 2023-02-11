from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_flammability_type():
    prod = Product('Test Product')
    assert isinstance(prod.flammability, float)


def test_default_weight():
    prod = Product("Test Product")
    assert prod.weight == 2


def test_generate_product():
    assert len(generate_products()) == 30
