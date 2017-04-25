import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import inspection, inspectionItemStatus, inspectionItemDetail, priorityLevel, restaurant
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_inspection(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["timeIn"] = "timeIn"
    defaults["timeOut"] = "timeOut"
    defaults["purposeOfInspection"] = "purposeOfInspection"
    defaults.update(**kwargs)
    if "employeeUsername" not in defaults:
        defaults["employeeUsername"] = create_django_contrib_auth_models_user()
    if "restaurantId" not in defaults:
        defaults["restaurantId"] = create_restaurant()
    return inspection.objects.create(**defaults)


def create_inspectionitemstatus(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["complianceStatus"] = "complianceStatus"
    defaults.update(**kwargs)
    if "inspectionId" not in defaults:
        defaults["inspectionId"] = create_inspection()
    if "itemDetailsId" not in defaults:
        defaults["itemDetailsId"] = create_inspectionitemdetail()
    return inspectionItemStatus.objects.create(**defaults)


def create_inspectionitemdetail(**kwargs):
    defaults = {}
    defaults["subhead"] = "subhead"
    defaults["description"] = "description"
    defaults["id"] = "id"
    defaults.update(**kwargs)
    if "priorityLevelId" not in defaults:
        defaults["priorityLevelId"] = create_prioritylevel()
    return inspectionItemDetail.objects.create(**defaults)


def create_prioritylevel(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["levelPoints"] = "levelPoints"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return priorityLevel.objects.create(**defaults)


def create_restaurant(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["name"] = "name"
    defaults["address"] = "address"
    defaults["owner"] = "owner"
    defaults["licensePermit"] = "licensePermit"
    defaults["restaurantType"] = "restaurantType"
    defaults["riskType"] = "riskType"
    defaults.update(**kwargs)
    return restaurant.objects.create(**defaults)


class inspectionViewTest(unittest.TestCase):
    '''
    Tests for inspection
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inspection(self):
        url = reverse('fvi_inspection_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inspection(self):
        url = reverse('fvi_inspection_create')
        data = {
            "id": "id",
            "timeIn": "timeIn",
            "timeOut": "timeOut",
            "purposeOfInspection": "purposeOfInspection",
            "employeeUsername": create_django_contrib_auth_models_user().pk,
            "restaurantId": create_restaurant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inspection(self):
        inspection = create_inspection()
        url = reverse('fvi_inspection_detail', args=[inspection.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inspection(self):
        inspection = create_inspection()
        data = {
            "id": "id",
            "timeIn": "timeIn",
            "timeOut": "timeOut",
            "purposeOfInspection": "purposeOfInspection",
            "employeeUsername": create_django_contrib_auth_models_user().pk,
            "restaurantId": create_restaurant().pk,
        }
        url = reverse('fvi_inspection_update', args=[inspection.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class inspectionItemStatusViewTest(unittest.TestCase):
    '''
    Tests for inspectionItemStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inspectionitemstatus(self):
        url = reverse('fvi_inspectionitemstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inspectionitemstatus(self):
        url = reverse('fvi_inspectionitemstatus_create')
        data = {
            "id": "id",
            "complianceStatus": "complianceStatus",
            "inspectionId": create_inspection().pk,
            "itemDetailsId": create_inspectionitemdetail().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inspectionitemstatus(self):
        inspectionitemstatus = create_inspectionitemstatus()
        url = reverse('fvi_inspectionitemstatus_detail', args=[inspectionitemstatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inspectionitemstatus(self):
        inspectionitemstatus = create_inspectionitemstatus()
        data = {
            "id": "id",
            "complianceStatus": "complianceStatus",
            "inspectionId": create_inspection().pk,
            "itemDetailsId": create_inspectionitemdetail().pk,
        }
        url = reverse('fvi_inspectionitemstatus_update', args=[inspectionitemstatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class inspectionItemDetailViewTest(unittest.TestCase):
    '''
    Tests for inspectionItemDetail
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inspectionitemdetail(self):
        url = reverse('fvi_inspectionitemdetail_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inspectionitemdetail(self):
        url = reverse('fvi_inspectionitemdetail_create')
        data = {
            "subhead": "subhead",
            "description": "description",
            "id": "id",
            "priorityLevelId": create_prioritylevel().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inspectionitemdetail(self):
        inspectionitemdetail = create_inspectionitemdetail()
        url = reverse('fvi_inspectionitemdetail_detail', args=[inspectionitemdetail.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inspectionitemdetail(self):
        inspectionitemdetail = create_inspectionitemdetail()
        data = {
            "subhead": "subhead",
            "description": "description",
            "id": "id",
            "priorityLevelId": create_prioritylevel().pk,
        }
        url = reverse('fvi_inspectionitemdetail_update', args=[inspectionitemdetail.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class priorityLevelViewTest(unittest.TestCase):
    '''
    Tests for priorityLevel
    '''
    def setUp(self):
        self.client = Client()

    def test_list_prioritylevel(self):
        url = reverse('fvi_prioritylevel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_prioritylevel(self):
        url = reverse('fvi_prioritylevel_create')
        data = {
            "name": "name",
            "levelPoints": "levelPoints",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_prioritylevel(self):
        prioritylevel = create_prioritylevel()
        url = reverse('fvi_prioritylevel_detail', args=[prioritylevel.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_prioritylevel(self):
        prioritylevel = create_prioritylevel()
        data = {
            "name": "name",
            "levelPoints": "levelPoints",
            "description": "description",
        }
        url = reverse('fvi_prioritylevel_update', args=[prioritylevel.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class restaurantViewTest(unittest.TestCase):
    '''
    Tests for restaurant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_restaurant(self):
        url = reverse('fvi_restaurant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_restaurant(self):
        url = reverse('fvi_restaurant_create')
        data = {
            "id": "id",
            "name": "name",
            "address": "address",
            "owner": "owner",
            "licensePermit": "licensePermit",
            "restaurantType": "restaurantType",
            "riskType": "riskType",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_restaurant(self):
        restaurant = create_restaurant()
        url = reverse('fvi_restaurant_detail', args=[restaurant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_restaurant(self):
        restaurant = create_restaurant()
        data = {
            "id": "id",
            "name": "name",
            "address": "address",
            "owner": "owner",
            "licensePermit": "licensePermit",
            "restaurantType": "restaurantType",
            "riskType": "riskType",
        }
        url = reverse('fvi_restaurant_update', args=[restaurant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


