# serializers.py
from rest_framework import serializers
from .models import LibraryHistory

class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '_all_'