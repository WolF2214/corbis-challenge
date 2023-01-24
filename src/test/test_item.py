import pytest

from base.models import Item

@pytest.mark.django_db
def test_item_creation():
    item = Item.objects.create_item(
        code='1004',
        name='Arena Fina',
        price='4000',
        quantity='23'
    )
    assert item.name == 'Arena fina'
    