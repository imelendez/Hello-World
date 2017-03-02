from . import models

from rest_framework import serializers


class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.employee
        fields = (
            'pk', 
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'address', 
        )


class reportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.report
        fields = (
            'pk', 
            'id', 
            'time_in', 
            'time_out', 
            'purpose_of_inspection', 
            'COS_violation_count', 
        )


class inspection_item_statusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.inspection_item_status
        fields = (
            'pk', 
            'id', 
        )


class inspection_itemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.inspection_item
        fields = (
            'pk', 
            'id', 
            'subhead', 
            'description', 
        )


class compliance_statusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.compliance_status
        fields = (
            'pk', 
            'id', 
            'code', 
            'spelled_out_compstatus', 
        )


class priority_levelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.priority_level
        fields = (
            'pk', 
            'name', 
            'id', 
            'level_points', 
        )


class restaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.restaurant
        fields = (
            'pk', 
            'id', 
            'name', 
            'owner', 
            'license_permit', 
        )


class restaurant_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.restaurant_type
        fields = (
            'pk', 
            'type', 
        )


