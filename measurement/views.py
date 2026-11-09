from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from .models import Measurement, Sensor
from .serializers import (
    MeasurementCreateSerializer,
    SensorDetailSerializer,
    SensorSerializer,
)


class SensorViewSet(viewsets.ModelViewSet):
    """
    CRUD для датчиков.
    POST   /sensors/            — создать
    GET    /sensors/            — список
    GET    /sensors/{id}/       — детали
    PUT    /sensors/{id}/       — обновить
    PATCH  /sensors/{id}/       — частично обновить
    DELETE /sensors/{id}/       — удалить
    """
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        return SensorSerializer

    # Дополнительный эндпоинт: POST /sensors/{id}/measurements/
    # Создать измерение для конкретного датчика
    def create_measurement(self, request, pk=None):
        sensor = self.get_object()
        serializer = MeasurementCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sensor=sensor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)