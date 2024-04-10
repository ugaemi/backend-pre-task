from api.tests import TestUserAPITestCase
from apps.contacts.models import Contact, ContactLabel


class ContactAPIViewTestCase(TestUserAPITestCase):
    def setUp(self):
        super().setUp()
        self.url = '/api/v1/contacts/'

    def test_create_contact(self):
        data = {
            'name': '김유경',
            'company': '키즈노트',
            'position': '백엔드 개발자',
            'email': 'ugaemi@kidsnote.com',
            'phone': '010-1234-5678',
        }
        response = self.client.post(f"{self.url}", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['company'], data['company'])
        self.assertEqual(response.data['position'], data['position'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['phone'], data['phone'])

    def test_list_contact(self):
        Contact.objects.create(
            owner=self.user,
            name='김유경',
            company='키즈노트',
            position='백엔드 개발자',
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_contact(self):
        contact = Contact.objects.create(
            owner=self.user,
            name='김유경',
            company='키즈노트',
            position='백엔드 개발자',
            email='ugaemi@kidsnote.com',
            phone='010-1234-5678',
        )
        response = self.client.get(f'{self.url}{contact.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], contact.name)
        self.assertEqual(response.data['company'], contact.company)
        self.assertEqual(response.data['position'], contact.position)
        self.assertEqual(response.data['email'], contact.email)
        self.assertEqual(response.data['phone'], contact.phone)

    def test_update_contact(self):
        contact = Contact.objects.create(
            owner=self.user,
            name='김유경',
            company='키즈노트',
            position='백엔드 개발자',
            email='ugaemi@kidsnote.com',
            phone='010-1234-5678',
        )
        data = {
            'email': 'ugaemi2@kidsnote.com',
            'phone': '010-5678-1234',
        }
        response = self.client.patch(f'{self.url}{contact.pk}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['phone'], data['phone'])

    def test_delete_contact(self):
        contact = Contact.objects.create(
            owner=self.user,
            name='김유경',
            company='키즈노트',
            position='백엔드 개발자',
        )
        response = self.client.delete(f'{self.url}{contact.pk}/')
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        super().tearDown()
        Contact.objects.all().delete()


class ContactLabelAPIViewTestCase(TestUserAPITestCase):
    def setUp(self):
        super().setUp()
        self.url = '/api/v1/contacts/labels/'

    def test_create_contact_label(self):
        data = {
            'name': '친구',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])

    def test_list_contact_label(self):
        ContactLabel.objects.create(
            owner=self.user,
            name='친구',
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_contact_label(self):
        contact_label = ContactLabel.objects.create(
            owner=self.user,
            name='친구',
        )
        response = self.client.get(f'{self.url}{contact_label.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], contact_label.name)

    def test_update_contact_label(self):
        contact_label = ContactLabel.objects.create(
            owner=self.user,
            name='친구',
        )
        data = {
            'name': '가족',
        }
        response = self.client.patch(f'{self.url}{contact_label.pk}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_contact_label(self):
        contact_label = ContactLabel.objects.create(
            owner=self.user,
            name='친구',
        )
        response = self.client.delete(f'{self.url}{contact_label.pk}/')
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        super().tearDown()
        ContactLabel.objects.all().delete()
