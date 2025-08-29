from rest_framework import serializers
from Database.models import TestItem   # ✅ yahan apna TestItem model import ho raha hai

class TestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestItem
        fields = '__all__'   # sab fields frontend ko bhejne ke liye
