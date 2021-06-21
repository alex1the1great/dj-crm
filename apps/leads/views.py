from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse

from .models import Lead
from .forms import LeadForm


class LandingPage(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        send_mail(
            subject='A lead has been created',
            message='Go to site to see the new lead',
            from_email='admin@test.com',
            recipient_list=['new@lead.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')
