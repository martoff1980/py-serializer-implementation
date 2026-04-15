from rest_framework import serializers
from car.models import Car


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        # adjust min/max to match your model's validators
        min_value=1,
        max_value=10000
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True, required=False
    )

    def create(self, validated_data: dict) -> Car:
        return Car(**validated_data)
