import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import employee, report, inspection_item_status, inspection_item, compliance_status, priority_level, restaurant, restaurant_type
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


def create_employee(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults["email"] = "email"
    defaults["address"] = "address"
    defaults.update(**kwargs)
    if "restaurant_id" not in defaults:
        defaults["restaurant_id"] = create_restaurant()
    return employee.objects.create(**defaults)


def create_report(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["time_in"] = "time_in"
    defaults["time_out"] = "time_out"
    defaults["purpose_of_inspection"] = "purpose_of_inspection"
    defaults["COS_violation_count"] = "COS_violation_count"
    defaults.update(**kwargs)
    if "employee_id" not in defaults:
        defaults["employee_id"] = create_employee()
    if "restaurant_id" not in defaults:
        defaults["restaurant_id"] = create_restaurant()
    return report.objects.create(**defaults)


def create_inspection_item_status(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults.update(**kwargs)
    if "report_id" not in defaults:
        defaults["report_id"] = create_report()
    return inspection_item_status.objects.create(**defaults)


def create_inspection_item(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["subhead"] = "subhead"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    if "inspection_item_status_id" not in defaults:
        defaults["inspection_item_status_id"] = create_inspection_item_status()
    return inspection_item.objects.create(**defaults)


def create_compliance_status(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["code"] = "code"
    defaults["spelled_out_compstatus"] = "spelled_out_compstatus"
    defaults.update(**kwargs)
    if "inspection_item_status_id" not in defaults:
        defaults["inspection_item_status_id"] = create_inspection_item_status()
    return compliance_status.objects.create(**defaults)


def create_priority_level(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["id"] = "id"
    defaults["level_points"] = "level_points"
    defaults.update(**kwargs)
    if "inspection_item_id" not in defaults:
        defaults["inspection_item_id"] = create_inspection_item()
    return priority_level.objects.create(**defaults)


def create_restaurant(**kwargs):
    defaults = {}
    defaults["id"] = "id"
    defaults["name"] = "name"
    defaults["owner"] = "owner"
    defaults["license_permit"] = "license_permit"
    defaults.update(**kwargs)
    return restaurant.objects.create(**defaults)


def create_restaurant_type(**kwargs):
    defaults = {}
    defaults["type"] = "type"
    defaults.update(**kwargs)
    if "restaurant_id" not in defaults:
        defaults["restaurant_id"] = create_restaurant()
    return restaurant_type.objects.create(**defaults)


class employeeViewTest(unittest.TestCase):
    '''
    Tests for employee
    '''
    def setUp(self):
        self.client = Client()

    def test_list_employee(self):
        url = reverse('food_venue_inspection_employee_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        url = reverse('food_venue_inspection_employee_create')
        data = {
            "id": "id",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "address": "address",
            "restaurant_id": create_restaurant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_employee(self):
        employee = create_employee()
        url = reverse('food_venue_inspection_employee_detail', args=[employee.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_employee(self):
        employee = create_employee()
        data = {
            "id": "id",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "address": "address",
            "restaurant_id": create_restaurant().pk,
        }
        url = reverse('food_venue_inspection_employee_update', args=[employee.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class reportViewTest(unittest.TestCase):
    '''
    Tests for report
    '''
    def setUp(self):
        self.client = Client()

    def test_list_report(self):
        url = reverse('food_venue_inspection_report_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_report(self):
        url = reverse('food_venue_inspection_report_create')
        data = {
            "id": "id",
            "time_in": "time_in",
            "time_out": "time_out",
            "purpose_of_inspection": "purpose_of_inspection",
            "COS_violation_count": "COS_violation_count",
            "employee_id": create_employee().pk,
            "restaurant_id": create_restaurant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_report(self):
        report = create_report()
        url = reverse('food_venue_inspection_report_detail', args=[report.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_report(self):
        report = create_report()
        data = {
            "id": "id",
            "time_in": "time_in",
            "time_out": "time_out",
            "purpose_of_inspection": "purpose_of_inspection",
            "COS_violation_count": "COS_violation_count",
            "employee_id": create_employee().pk,
            "restaurant_id": create_restaurant().pk,
        }
        url = reverse('food_venue_inspection_report_update', args=[report.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class inspection_item_statusViewTest(unittest.TestCase):
    '''
    Tests for inspection_item_status
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inspection_item_status(self):
        url = reverse('food_venue_inspection_inspection_item_status_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inspection_item_status(self):
        url = reverse('food_venue_inspection_inspection_item_status_create')
        data = {
            "id": "id",
            "report_id": create_report().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inspection_item_status(self):
        inspection_item_status = create_inspection_item_status()
        url = reverse('food_venue_inspection_inspection_item_status_detail', args=[inspection_item_status.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inspection_item_status(self):
        inspection_item_status = create_inspection_item_status()
        data = {
            "id": "id",
            "report_id": create_report().pk,
        }
        url = reverse('food_venue_inspection_inspection_item_status_update', args=[inspection_item_status.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class inspection_itemViewTest(unittest.TestCase):
    '''
    Tests for inspection_item
    '''
    def setUp(self):
        self.client = Client()

    def test_list_inspection_item(self):
        url = reverse('food_venue_inspection_inspection_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_inspection_item(self):
        url = reverse('food_venue_inspection_inspection_item_create')
        data = {
            "id": "id",
            "subhead": "subhead",
            "description": "description",
            "inspection_item_status_id": create_inspection_item_status().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_inspection_item(self):
        inspection_item = create_inspection_item()
        url = reverse('food_venue_inspection_inspection_item_detail', args=[inspection_item.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_inspection_item(self):
        inspection_item = create_inspection_item()
        data = {
            "id": "id",
            "subhead": "subhead",
            "description": "description",
            "inspection_item_status_id": create_inspection_item_status().pk,
        }
        url = reverse('food_venue_inspection_inspection_item_update', args=[inspection_item.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class compliance_statusViewTest(unittest.TestCase):
    '''
    Tests for compliance_status
    '''
    def setUp(self):
        self.client = Client()

    def test_list_compliance_status(self):
        url = reverse('food_venue_inspection_compliance_status_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_compliance_status(self):
        url = reverse('food_venue_inspection_compliance_status_create')
        data = {
            "id": "id",
            "code": "code",
            "spelled_out_compstatus": "spelled_out_compstatus",
            "inspection_item_status_id": create_inspection_item_status().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_compliance_status(self):
        compliance_status = create_compliance_status()
        url = reverse('food_venue_inspection_compliance_status_detail', args=[compliance_status.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_compliance_status(self):
        compliance_status = create_compliance_status()
        data = {
            "id": "id",
            "code": "code",
            "spelled_out_compstatus": "spelled_out_compstatus",
            "inspection_item_status_id": create_inspection_item_status().pk,
        }
        url = reverse('food_venue_inspection_compliance_status_update', args=[compliance_status.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class priority_levelViewTest(unittest.TestCase):
    '''
    Tests for priority_level
    '''
    def setUp(self):
        self.client = Client()

    def test_list_priority_level(self):
        url = reverse('food_venue_inspection_priority_level_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_priority_level(self):
        url = reverse('food_venue_inspection_priority_level_create')
        data = {
            "name": "name",
            "id": "id",
            "level_points": "level_points",
            "inspection_item_id": create_inspection_item().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_priority_level(self):
        priority_level = create_priority_level()
        url = reverse('food_venue_inspection_priority_level_detail', args=[priority_level.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_priority_level(self):
        priority_level = create_priority_level()
        data = {
            "name": "name",
            "id": "id",
            "level_points": "level_points",
            "inspection_item_id": create_inspection_item().pk,
        }
        url = reverse('food_venue_inspection_priority_level_update', args=[priority_level.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class restaurantViewTest(unittest.TestCase):
    '''
    Tests for restaurant
    '''
    def setUp(self):
        self.client = Client()

    def test_list_restaurant(self):
        url = reverse('food_venue_inspection_restaurant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_restaurant(self):
        url = reverse('food_venue_inspection_restaurant_create')
        data = {
            "id": "id",
            "name": "name",
            "owner": "owner",
            "license_permit": "license_permit",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_restaurant(self):
        restaurant = create_restaurant()
        url = reverse('food_venue_inspection_restaurant_detail', args=[restaurant.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_restaurant(self):
        restaurant = create_restaurant()
        data = {
            "id": "id",
            "name": "name",
            "owner": "owner",
            "license_permit": "license_permit",
        }
        url = reverse('food_venue_inspection_restaurant_update', args=[restaurant.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class restaurant_typeViewTest(unittest.TestCase):
    '''
    Tests for restaurant_type
    '''
    def setUp(self):
        self.client = Client()

    def test_list_restaurant_type(self):
        url = reverse('food_venue_inspection_restaurant_type_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_restaurant_type(self):
        url = reverse('food_venue_inspection_restaurant_type_create')
        data = {
            "type": "type",
            "restaurant_id": create_restaurant().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_restaurant_type(self):
        restaurant_type = create_restaurant_type()
        url = reverse('food_venue_inspection_restaurant_type_detail', args=[restaurant_type.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_restaurant_type(self):
        restaurant_type = create_restaurant_type()
        data = {
            "type": "type",
            "restaurant_id": create_restaurant().pk,
        }
        url = reverse('food_venue_inspection_restaurant_type_update', args=[restaurant_type.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


