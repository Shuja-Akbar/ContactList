# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ContactList
from django.views import generic


class ListOfContactView(generic.ListView):
    model = ContactList


class ContactDetailsView(generic.DetailView):
    model = ContactList


class AddContact(generic.DetailView):
    model = ContactList


class ContactCreate(generic.CreateView):
    model = ContactList
    fields = ['name', 'email', 'address', 'phone']
    success_url = '/contact/'
