from django.views.generic import ListView, DetailView
from .snacks import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'candy_snacks'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
