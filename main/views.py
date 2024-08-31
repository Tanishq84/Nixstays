from django.shortcuts import render, redirect
from .models import Property
from .forms import ConsultationForm
from django.http import HttpResponseRedirect
from .models import Consultation, Reservation
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile, Testimonials
from django.db.models import Q
from .models import Property, Institute, Amenity


def explore(request):
    institute_id = request.GET.get('institute')
    query = request.GET.get('query', '')
    property_type = request.GET.get('type', '')
    properties = Property.objects.all()

    if institute_id:
        properties = properties.filter(nearby_institutes__id=institute_id)
    
    if property_type:
        properties = properties.filter(property_type=property_type)

    if query:
        properties = properties.filter(
            Q(name__icontains=query) |
            Q(locality__icontains=query) |
            Q(description__icontains=query)
        )

    # Add additional filtering logic as needed.

    context = {
        'institutes': Institute.objects.all(),
        'properties': properties,
        'institute_id': institute_id,
    }
    return render(request, 'explore.html', context)



def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    other = property.other_facilities.split(", ") if property.other_facilities else []
    return render(request, 'property_detail.html', {'property': property, 'other': other})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user.email = request.POST.get('email')
            user_profile.user.save()
            user_profile.save()
            return redirect('account_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form, 'email': request.user.email, 'name': user_profile.name, 'dp': user_profile.dp})
# Create your views here.
def home(request):
    properties = Property.objects.all()
    testimonials = Testimonials.objects.all()
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            Consultation.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mobile_number=form.cleaned_data['mobile_number'],
                date_time=form.cleaned_data['date_time'],
                institute=form.cleaned_data['institute'],
                custom_msg=form.cleaned_data['custom_msg']
            )
            return HttpResponseRedirect('/')
    else:
        form = ConsultationForm()
    return render(request, 'home.html', {'properties': properties, 'form': form, 'testimonials': testimonials, 'institutes': Institute.objects.all()})




@login_required
def reserve_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    Reservation.objects.create(user=request.user, property=property)
    return HttpResponseRedirect('/')


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'my_reservations.html', {'reservations': reservations})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

