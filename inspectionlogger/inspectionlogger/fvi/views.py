from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import inspection, inspectionItemStatus, inspectionItemDetail, priorityLevel, restaurant
from .forms import searchForm, inspectionForm, inspectionItemStatusForm, inspectionItemDetailForm, priorityLevelForm, restaurantForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db.models import Count, Min, Sum, Avg
from django.db.models import F, FloatField, Sum
from django.utils import timezone
from django.http import HttpResponseRedirect
import operator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin



def results(request):
    if request.method == 'GET':
        if request.GET.get('searchQuery'):
            query = '%s' % request.GET['searchQuery']
        else:
            query = 'You submitted nothing!'
        print(query)
     #using icontain field lookup to return case insensitive query result
    restaurants = restaurant.objects.filter(name__icontains=query) #resturn restaurant with matching name
    resCount=restaurants.count()
    print (resCount)
    return render(request, 'results.html', {'restaurant_list': restaurants, "searchQuery":query, "restaurantCount":resCount})

def index(request):
    current_restaurant_list = restaurant.objects.order_by('-name')[:5]
    template = loader.get_template('fvi/index.html')
    context = {
        'current_restaurant_list': current_restaurant_list,
    }
    mySearchForm = searchForm()
    return render(request, 'fvi/index.html', {'form': mySearchForm})
    # return HttpResponse(template.render(context, request))
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
class inspectionListView(ListView):
    model = inspection
class inspectionCreateView(CreateView):
    permission_required = 'catalog.Can_Create_Inspection'
    model = inspection
    form_class = inspectionForm
class inspectionDetailView(DetailView):
    model = inspection

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(inspectionDetailView, self).get_context_data(**kwargs)
        selfNOW=self.get_object()
        insobjs=inspectionItemStatus.objects.all()
        searchResultObj=insobjs.filter(inspectionId=selfNOW.id) #filters for inspections related to reastaurant now
        blue=insobjs.filter(inspectionId=selfNOW.id).aggregate(Sum(F('complianceStatus'), output_field=FloatField()))
        print(blue)
        context['totalScore'] = blue
        context['inspectionObjects_list'] = searchResultObj
        print("searchresultsis>>>>")
        print(searchResultObj)
        print("or")
        print(context['inspectionObjects_list'])
        print("CONTEXT HERE")
        print(context)
        return context

class inspectionUpdateView(UpdateView):
    permission_required = 'catalog.Can_Update_Inspection'
    model = inspection
    form_class = inspectionForm
class inspectionItemStatusListView(ListView):
    model = inspectionItemStatus
class inspectionItemStatusCreateView(CreateView):
    model = inspectionItemStatus
    form_class = inspectionItemStatusForm
class inspectionItemStatusDetailView(DetailView):
    model = inspectionItemStatus
class inspectionItemStatusUpdateView(UpdateView):
    model = inspectionItemStatus
    form_class = inspectionItemStatusForm
class inspectionItemDetailListView(ListView):
    model = inspectionItemDetail
class inspectionItemDetailCreateView(CreateView):
    model = inspectionItemDetail
    form_class = inspectionItemDetailForm
class inspectionItemDetailDetailView(DetailView):
    model = inspectionItemDetail
class inspectionItemDetailUpdateView(UpdateView):
    model = inspectionItemDetail
    form_class = inspectionItemDetailForm
class priorityLevelListView(ListView):
    model = priorityLevel
class priorityLevelCreateView(CreateView):
    model = priorityLevel
    form_class = priorityLevelForm
class priorityLevelDetailView(DetailView):
    model = priorityLevel
class priorityLevelUpdateView(UpdateView):
    model = priorityLevel
    form_class = priorityLevelForm
class restaurantListView(ListView):
    model = restaurant
    template_name = 'fvi/restaurant_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'restaurants'  # Default: object_list
    paginate_by = 3
    queryset = restaurant.objects.all()  # Default: Model.objects.all()
class restaurantCreateView(CreateView):
    permission_required = 'catalog.Can_Create_Restaurant'
    model = restaurant
    form_class = restaurantForm
class restaurantDetailView(DetailView):
    model = restaurant

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(restaurantDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(super(restaurantDetailView, self).get_context_data(**kwargs))
        # print("object attempt next")
        # print(self.get_object())
        selfNOW=self.get_object()
        # print(selfNOW.address)
        # print(selfNOW.id)
        # context['inspection_list'] = inspection.objects.all()//I DONT WANT ALL DELETE ME
        insobjs=inspection.objects.all()
        searchResultObj=insobjs.filter(restaurantId=selfNOW.id) #filters for inspections related to reastaurant now
        context['inspectionObjects_list'] = searchResultObj
        print("searchresultsis>>>>")
        print(searchResultObj)
        print("or")
        print(context['inspectionObjects_list'])
        print("CONTEXT HERE")
        print(context)
        return context

class restaurantUpdateView(UpdateView):
    permission_required = 'user.is_staff'
    model = restaurant
    form_class = restaurantForm
