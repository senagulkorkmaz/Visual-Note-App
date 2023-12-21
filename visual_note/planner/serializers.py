from rest_framework import serializers
from planner.models import Planner


class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = '__all__'
