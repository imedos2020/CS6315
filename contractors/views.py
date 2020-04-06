from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Contractor


# class ContractorListView(ListView):
#     template_name = 'base.html'
#     queryset = Contractor.objects.all()

def get_contractors(request):
    return render(request, 'contractorList.html', {'list': Contractor.objects.all()})
