from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Lead, Agent
from .forms import LeadForm


def landing_page(request):
    return render(request, 'landing.html')


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})


def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')
    return render(request, 'leads/lead_create.html', {'form': form})


def lead_update(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(reverse('leads:lead_detail', args=[pk]))
    return render(request, 'leads/lead_update.html', {'lead': lead, 'form': form})


def lead_delete(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    lead.delete()
    return redirect('leads:lead_list')
