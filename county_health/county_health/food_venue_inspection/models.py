from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class employee(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    # Relationship Fields
    restaurant_id = models.ForeignKey('food_venue_inspection.restaurant', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_employee_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_employee_update', args=(self.pk,))


class report(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    purpose_of_inspection = models.IntegerField()
    COS_violation_count = models.IntegerField()

    # Relationship Fields
    employee_id = models.ForeignKey('food_venue_inspection.employee', )
    restaurant_id = models.ForeignKey('food_venue_inspection.restaurant', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_report_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_report_update', args=(self.pk,))


class inspection_item_status(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)

    # Relationship Fields
    report_id = models.ForeignKey('food_venue_inspection.report', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_inspection_item_status_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_inspection_item_status_update', args=(self.pk,))


class inspection_item(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    subhead = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    # Relationship Fields
    inspection_item_status_id = models.ForeignKey('food_venue_inspection.inspection_item_status', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_inspection_item_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_inspection_item_update', args=(self.pk,))


class compliance_status(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    spelled_out_compstatus = models.TextField(max_length=100)

    # Relationship Fields
    inspection_item_status_id = models.ForeignKey('food_venue_inspection.inspection_item_status', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_compliance_status_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_compliance_status_update', args=(self.pk,))


class priority_level(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    level_points = models.IntegerField()

    # Relationship Fields
    inspection_item_id = models.ForeignKey('food_venue_inspection.inspection_item', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_priority_level_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_priority_level_update', args=(self.pk,))


class restaurant(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    owner = models.TextField(max_length=100)
    license_permit = models.IntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_restaurant_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_restaurant_update', args=(self.pk,))


class restaurant_type(models.Model):

    # Fields
    type = models.CharField(max_length=30)

    # Relationship Fields
    restaurant_id = models.ForeignKey('food_venue_inspection.restaurant', )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('food_venue_inspection_restaurant_type_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('food_venue_inspection_restaurant_type_update', args=(self.pk,))


