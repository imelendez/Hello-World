from . import models
from . import serializers
from rest_framework import viewsets, permissions


class inspectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the inspection class"""

    queryset = models.inspection.objects.all()
    serializer_class = serializers.inspectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class inspectionItemStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the inspectionItemStatus class"""

    queryset = models.inspectionItemStatus.objects.all()
    serializer_class = serializers.inspectionItemStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class inspectionItemDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for the inspectionItemDetail class"""

    queryset = models.inspectionItemDetail.objects.all()
    serializer_class = serializers.inspectionItemDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class priorityLevelViewSet(viewsets.ModelViewSet):
    """ViewSet for the priorityLevel class"""

    queryset = models.priorityLevel.objects.all()
    serializer_class = serializers.priorityLevelSerializer
    permission_classes = [permissions.IsAuthenticated]


class restaurantViewSet(viewsets.ModelViewSet):
    """ViewSet for the restaurant class"""

    queryset = models.restaurant.objects.all()
    serializer_class = serializers.restaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


