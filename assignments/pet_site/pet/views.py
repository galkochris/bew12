from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone

from pet.models import Pet, Appointment


class HomeView(ListView):
    def get(self, request):
        return render(request, 'home.html')

class PetCreateView(CreateView):
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'weight_in_pounds', 'Owner']
    template_name = 'pet/create_pet.html'

class PetListView (ListView):
    model = Pet

    def get(self, request):
        pets = self.get_queryset().all()
        return render(request, 'pet/pet_list.html', {'pets': pets})

class PetDetailView(DetailView):
    def get(self, request, pet_id):
        return render(request, 'pet/pet_detail.html', {'pet': Pet.objects.get(id=pet_id)})

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['date_of_appointment', 'duration_minutes', 'special_instructions', 'pet', 'appointment_name']
    template_name = 'calendar/create_appointment.html'

class CalendarListView(ListView):
    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()
        return render(request, 'calendar/calendar_list.html', {
            'appointment': appointments.filter(
                date_of_appointment__gte = timezone.now()
            ).order_by('date_of_appointment' 'date_of_appointment')
        })
    


class LoginView():
    pass

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'