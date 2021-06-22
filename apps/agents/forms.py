from django import forms

from apps.leads.models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user',)
