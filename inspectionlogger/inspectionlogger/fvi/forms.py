from django import forms
from .models import inspection, inspectionItemStatus, inspectionItemDetail, priorityLevel, restaurant

class inspectionForm(forms.ModelForm):
    class Meta:
        model = inspection
        fields = ['id', 'timeIn', 'timeOut', 'purposeOfInspection', 'employeeUsername', 'restaurantId']


class inspectionItemStatusForm(forms.ModelForm):
    class Meta:
        model = inspectionItemStatus
        fields = ['id', 'complianceStatus', 'inspectionId', 'itemDetailsId']


class inspectionItemDetailForm(forms.ModelForm):
    class Meta:
        model = inspectionItemDetail
        fields = ['subhead', 'description', 'id', 'priorityLevelId']


class priorityLevelForm(forms.ModelForm):
    class Meta:
        model = priorityLevel
        fields = ['name', 'levelPoints', 'description']


class restaurantForm(forms.ModelForm):
    class Meta:
        model = restaurant
        fields = ['id', 'name', 'address', 'owner', 'licensePermit', 'restaurantType', 'riskType']


class searchForm(forms.Form):
    searchQuery = forms.CharField(max_length=100, initial='search')