from Database.models import TestItem
from utility.serializer import testitem_serializer

def get_all_items():
    items = TestItem.objects.all()
    return [testitem_serializer(item) for item in items]   # JSON-safe dicts


# Create a new item
def create_item(name, description):
    return TestItem.objects.create(name=name, description=description)
