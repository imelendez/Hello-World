from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import employee, report, inspection_item_status, inspection_item, compliance_status, priority_level, restaurant, restaurant_type
from .forms import employeeForm, reportForm, inspection_item_statusForm, inspection_itemForm, compliance_statusForm, priority_levelForm, restaurantForm, restaurant_typeForm


class employeeListView(ListView):
    model = employee


class employeeCreateView(CreateView):
    model = employee
    form_class = employeeForm


class employeeDetailView(DetailView):
    model = employee


class employeeUpdateView(UpdateView):
    model = employee
    form_class = employeeForm


class reportListView(ListView):
    model = report


class reportCreateView(CreateView):
    model = report
    form_class = reportForm


class reportDetailView(DetailView):
    model = report


class reportUpdateView(UpdateView):
    model = report
    form_class = reportForm


class inspection_item_statusListView(ListView):
    model = inspection_item_status


class inspection_item_statusCreateView(CreateView):
    model = inspection_item_status
    form_class = inspection_item_statusForm


class inspection_item_statusDetailView(DetailView):
    model = inspection_item_status


class inspection_item_statusUpdateView(UpdateView):
    model = inspection_item_status
    form_class = inspection_item_statusForm


class inspection_itemListView(ListView):
    model = inspection_item


class inspection_itemCreateView(CreateView):
    model = inspection_item
    form_class = inspection_itemForm


class inspection_itemDetailView(DetailView):
    model = inspection_item


class inspection_itemUpdateView(UpdateView):
    model = inspection_item
    form_class = inspection_itemForm


class compliance_statusListView(ListView):
    model = compliance_status


class compliance_statusCreateView(CreateView):
    model = compliance_status
    form_class = compliance_statusForm


class compliance_statusDetailView(DetailView):
    model = compliance_status


class compliance_statusUpdateView(UpdateView):
    model = compliance_status
    form_class = compliance_statusForm


class priority_levelListView(ListView):
    model = priority_level


class priority_levelCreateView(CreateView):
    model = priority_level
    form_class = priority_levelForm


class priority_levelDetailView(DetailView):
    model = priority_level


class priority_levelUpdateView(UpdateView):
    model = priority_level
    form_class = priority_levelForm


class restaurantListView(ListView):
    model = restaurant


class restaurantCreateView(CreateView):
    model = restaurant
    form_class = restaurantForm


class restaurantDetailView(DetailView):
    model = restaurant


class restaurantUpdateView(UpdateView):
    model = restaurant
    form_class = restaurantForm


class restaurant_typeListView(ListView):
    model = restaurant_type


class restaurant_typeCreateView(CreateView):
    model = restaurant_type
    form_class = restaurant_typeForm


class restaurant_typeDetailView(DetailView):
    model = restaurant_type


class restaurant_typeUpdateView(UpdateView):
    model = restaurant_type
    form_class = restaurant_typeForm

