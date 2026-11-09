from rest_framework import serializers

from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    """Краткий сериализатор для вложенного вывода."""
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']
        read_only_fields = ['created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Полная информация по датчику — со всеми измерениями."""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorSerializer(serializers.ModelSerializer):
    """Краткая информация по датчику — для списка и создания."""

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    """Создание измерения (ID датчика подставляется из URL)."""

    class Meta:
        model = Measurement
        fields = ['temperature', 'image']