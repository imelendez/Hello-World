
from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'employee', api.employeeViewSet)
router.register(r'report', api.reportViewSet)
router.register(r'inspection_item_status', api.inspection_item_statusViewSet)
router.register(r'inspection_item', api.inspection_itemViewSet)
router.register(r'compliance_status', api.compliance_statusViewSet)
router.register(r'priority_level', api.priority_levelViewSet)
router.register(r'restaurant', api.restaurantViewSet)
router.register(r'restaurant_type', api.restaurant_typeViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for employee
    url(r'^food_venue_inspection/employee/$', views.employeeListView.as_view(), name='food_venue_inspection_employee_list'),
    url(r'^food_venue_inspection/employee/create/$', views.employeeCreateView.as_view(), name='food_venue_inspection_employee_create'),
    url(r'^food_venue_inspection/employee/detail/(?P<pk>\S+)/$', views.employeeDetailView.as_view(), name='food_venue_inspection_employee_detail'),
    url(r'^food_venue_inspection/employee/update/(?P<pk>\S+)/$', views.employeeUpdateView.as_view(), name='food_venue_inspection_employee_update'),
)

urlpatterns += (
    # urls for report
    url(r'^food_venue_inspection/report/$', views.reportListView.as_view(), name='food_venue_inspection_report_list'),
    url(r'^food_venue_inspection/report/create/$', views.reportCreateView.as_view(), name='food_venue_inspection_report_create'),
    url(r'^food_venue_inspection/report/detail/(?P<pk>\S+)/$', views.reportDetailView.as_view(), name='food_venue_inspection_report_detail'),
    url(r'^food_venue_inspection/report/update/(?P<pk>\S+)/$', views.reportUpdateView.as_view(), name='food_venue_inspection_report_update'),
)

urlpatterns += (
    # urls for inspection_item_status
    url(r'^food_venue_inspection/inspection_item_status/$', views.inspection_item_statusListView.as_view(), name='food_venue_inspection_inspection_item_status_list'),
    url(r'^food_venue_inspection/inspection_item_status/create/$', views.inspection_item_statusCreateView.as_view(), name='food_venue_inspection_inspection_item_status_create'),
    url(r'^food_venue_inspection/inspection_item_status/detail/(?P<pk>\S+)/$', views.inspection_item_statusDetailView.as_view(), name='food_venue_inspection_inspection_item_status_detail'),
    url(r'^food_venue_inspection/inspection_item_status/update/(?P<pk>\S+)/$', views.inspection_item_statusUpdateView.as_view(), name='food_venue_inspection_inspection_item_status_update'),
)

urlpatterns += (
    # urls for inspection_item
    url(r'^food_venue_inspection/inspection_item/$', views.inspection_itemListView.as_view(), name='food_venue_inspection_inspection_item_list'),
    url(r'^food_venue_inspection/inspection_item/create/$', views.inspection_itemCreateView.as_view(), name='food_venue_inspection_inspection_item_create'),
    url(r'^food_venue_inspection/inspection_item/detail/(?P<pk>\S+)/$', views.inspection_itemDetailView.as_view(), name='food_venue_inspection_inspection_item_detail'),
    url(r'^food_venue_inspection/inspection_item/update/(?P<pk>\S+)/$', views.inspection_itemUpdateView.as_view(), name='food_venue_inspection_inspection_item_update'),
)

urlpatterns += (
    # urls for compliance_status
    url(r'^food_venue_inspection/compliance_status/$', views.compliance_statusListView.as_view(), name='food_venue_inspection_compliance_status_list'),
    url(r'^food_venue_inspection/compliance_status/create/$', views.compliance_statusCreateView.as_view(), name='food_venue_inspection_compliance_status_create'),
    url(r'^food_venue_inspection/compliance_status/detail/(?P<pk>\S+)/$', views.compliance_statusDetailView.as_view(), name='food_venue_inspection_compliance_status_detail'),
    url(r'^food_venue_inspection/compliance_status/update/(?P<pk>\S+)/$', views.compliance_statusUpdateView.as_view(), name='food_venue_inspection_compliance_status_update'),
)

urlpatterns += (
    # urls for priority_level
    url(r'^food_venue_inspection/priority_level/$', views.priority_levelListView.as_view(), name='food_venue_inspection_priority_level_list'),
    url(r'^food_venue_inspection/priority_level/create/$', views.priority_levelCreateView.as_view(), name='food_venue_inspection_priority_level_create'),
    url(r'^food_venue_inspection/priority_level/detail/(?P<pk>\S+)/$', views.priority_levelDetailView.as_view(), name='food_venue_inspection_priority_level_detail'),
    url(r'^food_venue_inspection/priority_level/update/(?P<pk>\S+)/$', views.priority_levelUpdateView.as_view(), name='food_venue_inspection_priority_level_update'),
)

urlpatterns += (
    # urls for restaurant
    url(r'^food_venue_inspection/restaurant/$', views.restaurantListView.as_view(), name='food_venue_inspection_restaurant_list'),
    url(r'^food_venue_inspection/restaurant/create/$', views.restaurantCreateView.as_view(), name='food_venue_inspection_restaurant_create'),
    url(r'^food_venue_inspection/restaurant/detail/(?P<pk>\S+)/$', views.restaurantDetailView.as_view(), name='food_venue_inspection_restaurant_detail'),
    url(r'^food_venue_inspection/restaurant/update/(?P<pk>\S+)/$', views.restaurantUpdateView.as_view(), name='food_venue_inspection_restaurant_update'),
)

urlpatterns += (
    # urls for restaurant_type
    url(r'^food_venue_inspection/restaurant_type/$', views.restaurant_typeListView.as_view(), name='food_venue_inspection_restaurant_type_list'),
    url(r'^food_venue_inspection/restaurant_type/create/$', views.restaurant_typeCreateView.as_view(), name='food_venue_inspection_restaurant_type_create'),
    url(r'^food_venue_inspection/restaurant_type/detail/(?P<pk>\S+)/$', views.restaurant_typeDetailView.as_view(), name='food_venue_inspection_restaurant_type_detail'),
    url(r'^food_venue_inspection/restaurant_type/update/(?P<pk>\S+)/$', views.restaurant_typeUpdateView.as_view(), name='food_venue_inspection_restaurant_type_update'),
)

