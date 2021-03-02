from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Cliente
 
class IndexView(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    permission_required = 'cliente.permiso_vercliente'
    template_name = 'cliente/index.html'
    context_object_name = 'cliente_list'

class DetailView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    permission_required = 'cliente.permiso_crearcliente'
    model = Cliente
    template_name = 'cliente/detail.html'

class ResultsView(LoginRequiredMixin,PermissionRequiredMixin,generic.DetailView):
    permission_required = 'cliente.permiso_actualizarcliente'
    model = Cliente
    template_name = 'cliente/results.html'