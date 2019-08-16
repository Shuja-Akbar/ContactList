from django.test import TestCase
from contact.models import ContactList


class ContactListTestCase(TestCase):
    def setUp(self):
        ContactList.objects.create(name="Shuja", email="shuja@gmail.com", phone="123456", address="asd")
        ContactList.objects.create(name="adnan", email="adnan@gmail.com", phone="123456", address="asd")

    def test_contacts(self):
        contact1 = ContactList.objects.get(name="Shuja")
        #import pdb;
        #pdb.set_trace();
        self.assertEqual(contact1.name,"Shuja")