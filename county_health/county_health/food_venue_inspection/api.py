from . import models
from . import serializers
from rest_framework import viewsets, permissions


class employeeViewSet(viewsets.ModelViewSet):
    """ViewSet for the employee class"""

    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class reportViewSet(viewsets.ModelViewSet):
    """ViewSet for the report class"""

    queryset = models.report.objects.all()
    serializer_class = serializers.reportSerializer
    permission_classes = [permissions.IsAuthenticated]


class inspection_item_statusViewSet(viewsets.ModelViewSet):
    """ViewSet for the inspection_item_status class"""

    queryset = models.inspection_item_status.objects.all()
    serializer_class = serializers.inspection_item_statusSerializer
    permission_classes = [permissions.IsAuthenticated]


class inspection_itemViewSet(viewsets.ModelViewSet):
    """ViewSet for the inspection_item class"""

    queryset = models.inspection_item.objects.all()
    serializer_class = serializers.inspection_itemSerializer
    permission_classes = [permissions.IsAuthenticated]


class compliance_statusViewSet(viewsets.ModelViewSet):
    """ViewSet for the compliance_status class"""

    queryset = models.compliance_status.objects.all()
    serializer_class = serializers.compliance_statusSerializer
    permission_classes = [permissions.IsAuthenticated]


class priority_levelViewSet(viewsets.ModelViewSet):
    """ViewSet for the priority_level class"""

    queryset = models.priority_level.objects.all()
    serializer_class = serializers.priority_levelSerializer
    permission_classes = [permissions.IsAuthenticated]


class restaurantViewSet(viewsets.ModelViewSet):
    """ViewSet for the restaurant class"""

    queryset = models.restaurant.objects.all()
    serializer_class = serializers.restaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class restaurant_typeViewSet(viewsets.ModelViewSet):
    """ViewSet for the restaurant_type class"""

    queryset = models.restaurant_type.objects.all()
    serializer_class = serializers.restaurant_typeSerializer
    permission_classes = [permissions.IsAuthenticated]


