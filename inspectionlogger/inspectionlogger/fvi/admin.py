from django.contrib import admin
from django import forms
from .models import inspection, inspectionItemStatus, inspectionItemDetail, priorityLevel, restaurant

class inspectionAdminForm(forms.ModelForm):

    class Meta:
        model = inspection
        fields = '__all__'


class inspectionAdmin(admin.ModelAdmin):
    form = inspectionAdminForm
    list_display = ['id', 'timeIn', 'timeOut', 'purposeOfInspection']
    readonly_fields = ['id']
    # readonly_fields = ['id'], 'timeIn', 'timeOut', 'purposeOfInspection']

admin.site.register(inspection, inspectionAdmin)


class inspectionItemStatusAdminForm(forms.ModelForm):

    class Meta:
        model = inspectionItemStatus
        fields = '__all__'


class inspectionItemStatusAdmin(admin.ModelAdmin):
    form = inspectionItemStatusAdminForm
    list_display = ['id', 'complianceStatus']
    readonly_fields = ['id']
    # readonly_fields = ['id', 'complianceStatus']

admin.site.register(inspectionItemStatus, inspectionItemStatusAdmin)


class inspectionItemDetailAdminForm(forms.ModelForm):

    class Meta:
        model = inspectionItemDetail
        fields = '__all__'


class inspectionItemDetailAdmin(admin.ModelAdmin):
    form = inspectionItemDetailAdminForm
    list_display = ['subhead', 'description', 'id']
    readonly_fields = ['id']
    # readonly_fields = ['subhead', 'description', 'id']

admin.site.register(inspectionItemDetail, inspectionItemDetailAdmin)


class priorityLevelAdminForm(forms.ModelForm):

    class Meta:
        model = priorityLevel
        fields = '__all__'


class priorityLevelAdmin(admin.ModelAdmin):
    form = priorityLevelAdminForm
    list_display = ['name', 'levelPoints', 'description']
    # readonly_fields = ['name', 'levelPoints', 'description']

admin.site.register(priorityLevel, priorityLevelAdmin)


class restaurantAdminForm(forms.ModelForm):

    class Meta:
        model = restaurant
        fields = '__all__'


class restaurantAdmin(admin.ModelAdmin):
    form = restaurantAdminForm
    list_display = ['id', 'name', 'address', 'owner', 'licensePermit', 'restaurantType', 'riskType']
    readonly_fields = ['id']
    # readonly_fields = ['id', 'name', 'address', 'owner', 'licensePermit', 'restaurantType', 'riskType']

admin.site.register(restaurant, restaurantAdmin)


