from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from datetime import datetime





from wiki.models import Page
from wiki.forms import PageForm



class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page
    
    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page,
          'form': PageForm()
        })

    def post(self, request, slug, *args, **kwargs):
      form = PageForm(request.POST)

      if form.is_valid:
        page = self.get_queryset().get(slug__iexact=slug)
        page.title  = request.POST['title']
        page.content = request.POST['content']
        page.modified = datetime.now()
        page.slug = slugify(Page.title, allow_unicode=True)
        page.author = request.user
        page.save()
        return HttpResponseRedirect(
          reverse('wiki-details-page', args=[page.slug]))
      return render(request, 'page.html', {'form': form})

class PageCreateView(LoginRequiredMixin, CreateView):

  def get(self, request, *args, **kwargs):
    context = {
      'form': PageForm()
    }
    return render(request, 'create.html', context)

  def post(self, request, *args, **kwargs):
    form = PageForm(request.POST)
    
    if form.is_valid:
      page = form.save(commit=False)
      page.author = request.user
      page.save()
      return HttpResponseRedirect(
        reverse('wiki-details-page', args=[page.slug]))
    #else
    return render(request, 'create.html', { 'form':form })