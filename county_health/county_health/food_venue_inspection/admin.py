from django.contrib import admin
from django import forms
from .models import employee, report, inspection_item_status, inspection_item, compliance_status, priority_level, restaurant, restaurant_type

class employeeAdminForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = '__all__'


class employeeAdmin(admin.ModelAdmin):
    form = employeeAdminForm
    list_display = ['id', 'first_name', 'last_name', 'email', 'address']
    readonly_fields = ['id', 'first_name', 'last_name', 'email', 'address']

admin.site.register(employee, employeeAdmin)


class reportAdminForm(forms.ModelForm):

    class Meta:
        model = report
        fields = '__all__'


class reportAdmin(admin.ModelAdmin):
    form = reportAdminForm
    list_display = ['id', 'time_in', 'time_out', 'purpose_of_inspection', 'COS_violation_count']
    readonly_fields = ['id', 'time_in', 'time_out', 'purpose_of_inspection', 'COS_violation_count']

admin.site.register(report, reportAdmin)


class inspection_item_statusAdminForm(forms.ModelForm):

    class Meta:
        model = inspection_item_status
        fields = '__all__'


class inspection_item_statusAdmin(admin.ModelAdmin):
    form = inspection_item_statusAdminForm
    list_display = ['id']
    readonly_fields = ['id']

admin.site.register(inspection_item_status, inspection_item_statusAdmin)


class inspection_itemAdminForm(forms.ModelForm):

    class Meta:
        model = inspection_item
        fields = '__all__'


class inspection_itemAdmin(admin.ModelAdmin):
    form = inspection_itemAdminForm
    list_display = ['id', 'subhead', 'description']
    readonly_fields = ['id', 'subhead', 'description']

admin.site.register(inspection_item, inspection_itemAdmin)


class compliance_statusAdminForm(forms.ModelForm):

    class Meta:
        model = compliance_status
        fields = '__all__'


class compliance_statusAdmin(admin.ModelAdmin):
    form = compliance_statusAdminForm
    list_display = ['id', 'code', 'spelled_out_compstatus']
    readonly_fields = ['id', 'code', 'spelled_out_compstatus']

admin.site.register(compliance_status, compliance_statusAdmin)


class priority_levelAdminForm(forms.ModelForm):

    class Meta:
        model = priority_level
        fields = '__all__'


class priority_levelAdmin(admin.ModelAdmin):
    form = priority_levelAdminForm
    list_display = ['name', 'id', 'level_points']
    readonly_fields = ['name', 'id', 'level_points']

admin.site.register(priority_level, priority_levelAdmin)


class restaurantAdminForm(forms.ModelForm):

    class Meta:
        model = restaurant
        fields = '__all__'


class restaurantAdmin(admin.ModelAdmin):
    form = restaurantAdminForm
    list_display = ['id', 'name', 'owner', 'license_permit']
    readonly_fields = ['id', 'name', 'owner', 'license_permit']

admin.site.register(restaurant, restaurantAdmin)


class restaurant_typeAdminForm(forms.ModelForm):

    class Meta:
        model = restaurant_type
        fields = '__all__'


class restaurant_typeAdmin(admin.ModelAdmin):
    form = restaurant_typeAdminForm
    list_display = ['type']
    readonly_fields = ['type']

admin.site.register(restaurant_type, restaurant_typeAdmin)


