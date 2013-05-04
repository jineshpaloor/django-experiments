# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from contacts.models import Contact
#from contacts.forms import ContactForm


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")


class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'


class CreateContactView(CreateView):

    #form_class = ContactForm
    model = Contact
    template_name = 'contact_form.html'

    def get_success_url(self):
        return reverse('contacts-list')
