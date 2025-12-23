from rest_framework import serializers
from .models import TODO

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        # We list the fields we want to send to React
        fields = ['id', 'title', 'is_complete', 'created_at']
        # Note: If your model field is named 'status' instead of 'completed', 
        # change it above!