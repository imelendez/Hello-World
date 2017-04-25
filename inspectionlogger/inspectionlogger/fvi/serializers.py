from . import models

from rest_framework import serializers


class inspectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.inspection
        fields = (
            'pk', 
            'id', 
            'timeIn', 
            'timeOut', 
            'purposeOfInspection', 
        )


class inspectionItemStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.inspectionItemStatus
        fields = (
            'pk', 
            'id', 
            'complianceStatus', 
        )


class inspectionItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.inspectionItemDetail
        fields = (
            'pk', 
            'subhead', 
            'description', 
            'id', 
        )


class priorityLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.priorityLevel
        fields = (
            'pk', 
            'name', 
            'levelPoints', 
            'description', 
        )


class restaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.restaurant
        fields = (
            'pk', 
            'id', 
            'name', 
            'address', 
            'owner', 
            'licensePermit', 
            'restaurantType', 
            'riskType', 
        )


