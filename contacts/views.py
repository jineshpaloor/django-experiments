# Create your views here.
import forms
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from contacts.models import Contact


class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'

class ContactView(DetailView):

    model = Contact
    template_name = 'contact_detail.html'

class CreateContactView(CreateView):

    model = Contact
    #template_name = 'contact_form.html'
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context

class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'contact_confirm_delete.html'

    def get_success_url(self):
        return reverse('contacts-list')

class EditContactAddressView(UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()
