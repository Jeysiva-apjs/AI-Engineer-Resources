import pytest
from inventory_management import Inventory

@pytest.fixture
def inventory():
    inventory = Inventory()
    inventory.add_stock("potato", 5)
    return inventory


def test_add_stock(inventory):
    inventory.add_stock("apple", 5)
    assert inventory.stock["apple"] == 5
    
def test_remove_stock(inventory):
    inventory.remove_stock("potato", 3)
    assert inventory.stock["potato"] == 2
    
def test_check_availability(inventory):
    assert inventory.check_availability("potato", 5) == True

def test_remove_stock_with_insufficient_inventory(inventory):
    with pytest.raises(ValueError):
        assert inventory.remove_stock("potato", 15)
    
def test_full_inventory_cycle(inventory):
    # test entire cycle which is add_stock -> remove_stock -> check_availibility
    inventory.add_stock("mango", 10)
    assert inventory.stock["mango"] == 10

    inventory.remove_stock("mango", 6)
    assert inventory.stock["mango"] == 4

    assert inventory.check_availability("mango", 4) == True

