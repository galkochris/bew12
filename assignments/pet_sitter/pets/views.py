from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from datetime import datetime





from pets.models import Pet, Appointment
from pets.forms import PetForm



class PetListView(ListView):
    """ Renders a list of all Pages. """
    model = Pet

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PetDetailView(DetailView):
    model = Pet
    template_name = 'detail.html'
    
    def get(self, **kwargs):
        """ Returns a specific pet page by pk. """
        context = super().get_context_data(**kwargs)
        context['pet_form'] = PetForm()
        return context

    def post(self, request, pk):
      form = PetForm(request.POST)

      if form.is_valid:
        pet = form.save(commit=False)
        pet.pet = Pet.objects.get(pk=pk)
        pet.name  = request.POST['name']
        pet.species = request.POST['species']
        pet.breed = request.POST['breed']
        pet.weight_in_pounds = request.POST['weight_in_pounds']
        pet.modified = datetime.now()
        pet.owner = request.user
        pet.save()
        return HttpResponseRedirect(
          reverse('pets-details-page', args=[pk]))
      return render(request, 'pet.html', {'form': form})

class PetCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')


    def get(self, request):
        context = {
        'form': PetForm()
        }
        return render(request, 'create.html', context)

    def post(self, request, *args):
        form = PetForm(request.POST)
        
        if form.is_valid:
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return HttpResponseRedirect(
                reverse('pets-details-page', args=[pet.id]))
        #else
        return render(request, 'create.html', { 'form':form })