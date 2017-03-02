from django import forms
from .models import employee, report, inspection_item_status, inspection_item, compliance_status, priority_level, restaurant, restaurant_type


class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'restaurant_id']


class reportForm(forms.ModelForm):
    class Meta:
        model = report
        fields = ['id', 'time_in', 'time_out', 'purpose_of_inspection', 'COS_violation_count', 'employee_id', 'restaurant_id']


class inspection_item_statusForm(forms.ModelForm):
    class Meta:
        model = inspection_item_status
        fields = ['id', 'report_id']


class inspection_itemForm(forms.ModelForm):
    class Meta:
        model = inspection_item
        fields = ['id', 'subhead', 'description', 'inspection_item_status_id']


class compliance_statusForm(forms.ModelForm):
    class Meta:
        model = compliance_status
        fields = ['id', 'code', 'spelled_out_compstatus', 'inspection_item_status_id']


class priority_levelForm(forms.ModelForm):
    class Meta:
        model = priority_level
        fields = ['name', 'id', 'level_points', 'inspection_item_id']


class restaurantForm(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ['id', 'name', 'owner', 'license_permit']


class restaurant_typeForm(forms.ModelForm):
    class Meta:
        model = restaurant_type
        fields = ['type', 'restaurant_id']


