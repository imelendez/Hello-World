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
from django.db.models import Count, Min, Sum, Avg


class inspectionManager(models.Manager):
    def inspection_total(self):
        print("here")
        return self.objects.annotate(Count('inspectionitemstatus'))


class inspection(models.Model):
    PURPOSE_OPTIONS = (
        ('C', 'Compliance'),
        ('R', 'Routine'),
        ('F', 'Field Investigation'),
        ('V', 'Visit'),
        ('O', 'Other'),
    )
    # Fields
    id = models.IntegerField(primary_key=True)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField()
    purposeOfInspection = models.CharField(max_length=1, choices=PURPOSE_OPTIONS)

    # Relationship Fields
    employeeUsername = models.ForeignKey(settings.AUTH_USER_MODEL, )
    restaurantId = models.ForeignKey('fvi.restaurant', )

    class Meta:
        ordering = ('-pk',)

    objects = inspectionManager()
    # def __unicode__(self):
    #     return u'%s' % self.pk
    def __str__(self):
        return "%s %s" % (self.restaurantId.name, str(self.timeIn))

    def get_absolute_url(self):
        return reverse('fvi_inspection_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('fvi_inspection_update', args=(self.pk,))

    class Meta:
        permissions=(("create_inspection","can create inspetions"),
                     ("view_inspection","can view inspections"),
                     ("update_inspection","cann update inspections"))


class inspectionItemStatus(models.Model):
    OUT=0
    IN=1
    NO=2
    NA=3
    COS=4
    R=5
    INSPECTIONSTATUS = (
        (OUT, 'not in compliance'),
        (IN, 'in compliance'),
        (NO, 'not observed'),
        (NA, 'not applicable '),
        (R, 'corrected on site'),
    )
    # Fields
    id = models.IntegerField(primary_key=True)
    complianceStatus = models.IntegerField(choices=INSPECTIONSTATUS)

    # Relationship Fields
    inspectionId = models.ForeignKey('fvi.inspection', )
    itemDetailsId = models.ForeignKey('fvi.inspectionItemDetail', )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.itemDetailsId.description

    def get_absolute_url(self):
        return reverse('fvi_inspectionitemstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('fvi_inspectionitemstatus_update', args=(self.pk,))


class inspectionItemDetail(models.Model):

    # Fields
    subhead = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    id = models.IntegerField(primary_key=True)

    # Relationship Fields
    priorityLevelId = models.ForeignKey('fvi.priorityLevel', )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('fvi_inspectionitemdetail_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('fvi_inspectionitemdetail_update', args=(self.pk,))


class priorityLevel(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    levelPoints = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return str(self.levelPoints)

    def get_absolute_url(self):
        return reverse('fvi_prioritylevel_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('fvi_prioritylevel_update', args=(self.pk,))


class restaurant(models.Model):
    RISK_TYPES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    RESTAURANT_TYPES = (
        ('B', 'Buffet'),
        ('F', 'Fast Food'),
        ('S', 'Small Shop'),
    )
    # Fields
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    owner = models.CharField(max_length=30)
    licensePermit = models.IntegerField()
    restaurantType = models.CharField(max_length=1, choices=RESTAURANT_TYPES)
    riskType = models.CharField(max_length=1, choices=RISK_TYPES)


    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fvi_restaurant_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('fvi_restaurant_update', args=(self.pk,))


