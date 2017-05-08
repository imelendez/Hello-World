from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'inspection', api.inspectionViewSet)
router.register(r'inspectionitemstatus', api.inspectionItemStatusViewSet)
router.register(r'inspectionitemdetail', api.inspectionItemDetailViewSet)
router.register(r'prioritylevel', api.priorityLevelViewSet)
router.register(r'restaurant', api.restaurantViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/fvi/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
)

urlpatterns += (
    # urls for inspection
    url(r'^fvi/inspection/$', views.inspectionListView.as_view(), name='fvi_inspection_list'),
    url(r'^fvi/inspection/create/$', views.inspectionCreateView.as_view(), name='fvi_inspection_create'),
    url(r'^fvi/inspection/detail/(?P<pk>\S+)/$', views.inspectionDetailView.as_view(), name='fvi_inspection_detail'),
    url(r'^fvi/inspection/update/(?P<pk>\S+)/$', views.inspectionUpdateView.as_view(), name='fvi_inspection_update'),
)

urlpatterns += (
    # urls for inspectionItemStatus
    url(r'^fvi/inspectionitemstatus/$', views.inspectionItemStatusListView.as_view(), name='fvi_inspectionitemstatus_list'),
    url(r'^fvi/inspectionitemstatus/create/$', views.inspectionItemStatusCreateView.as_view(), name='fvi_inspectionitemstatus_create'),
    url(r'^fvi/inspectionitemstatus/detail/(?P<pk>\S+)/$', views.inspectionItemStatusDetailView.as_view(), name='fvi_inspectionitemstatus_detail'),
    url(r'^fvi/inspectionitemstatus/update/(?P<pk>\S+)/$', views.inspectionItemStatusUpdateView.as_view(), name='fvi_inspectionitemstatus_update'),
)

urlpatterns += (
    # urls for inspectionItemDetail
    url(r'^fvi/inspectionitemdetail/$', views.inspectionItemDetailListView.as_view(), name='fvi_inspectionitemdetail_list'),
    url(r'^fvi/inspectionitemdetail/create/$', views.inspectionItemDetailCreateView.as_view(), name='fvi_inspectionitemdetail_create'),
    url(r'^fvi/inspectionitemdetail/detail/(?P<pk>\S+)/$', views.inspectionItemDetailDetailView.as_view(), name='fvi_inspectionitemdetail_detail'),
    url(r'^fvi/inspectionitemdetail/update/(?P<pk>\S+)/$', views.inspectionItemDetailUpdateView.as_view(), name='fvi_inspectionitemdetail_update'),
)

urlpatterns += (
    # urls for priorityLevel
    url(r'^fvi/prioritylevel/$', views.priorityLevelListView.as_view(), name='fvi_prioritylevel_list'),
    url(r'^fvi/prioritylevel/create/$', views.priorityLevelCreateView.as_view(), name='fvi_prioritylevel_create'),
    url(r'^fvi/prioritylevel/detail/(?P<pk>\S+)/$', views.priorityLevelDetailView.as_view(), name='fvi_prioritylevel_detail'),
    url(r'^fvi/prioritylevel/update/(?P<pk>\S+)/$', views.priorityLevelUpdateView.as_view(), name='fvi_prioritylevel_update'),
)

urlpatterns += (
    # urls for restaurant
    url(r'^fvi/restaurant/$', views.restaurantListView.as_view(), name='fvi_restaurant_list'),
    url(r'^fvi/restaurant/create/$', views.restaurantCreateView.as_view(), name='fvi_restaurant_create'),
    url(r'^fvi/restaurant/detail/(?P<pk>\S+)/$', views.restaurantDetailView.as_view(), name='fvi_restaurant_detail'),
    url(r'^fvi/restaurant/update/(?P<pk>\S+)/$', views.restaurantUpdateView.as_view(), name='fvi_restaurant_update'),
    # url(r'^fvi/restaurant/inspections/(?P<pk>\S+)/$', views.PublisherBookList.as_view(), name='fvi_publisherbook_list')
)

