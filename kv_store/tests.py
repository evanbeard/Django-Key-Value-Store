from django.test import TestCase
from django.contrib.auth.models import User
import simplejson

class TestKVStore(TestCase):
    urls = 'kv_store.urls'
    test_payload = {'animal':'dog', 'city':'Buffalo', 'color':'blue'}

    def setUp(self):
        User.objects.create_user('testclient', 'testclient@test.client', 'password')

    def test_store(self):
        """
        Test storing values.
        """
        response = self.client.post('/store/', self.test_payload)
        # make sure login is required
        self.failUnlessEqual(response.status_code, 302)

        self.client.login(username='testclient', password='password')
        response = self.client.post('/store/', self.test_payload)
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(response.content, 'success')

    def test_retrieve(self):
        """
        Test retrieving values after they are stored.
        """
        response = self.client.post('/store/', self.test_payload)
        # make sure login is required
        self.failUnlessEqual(response.status_code, 302)

        self.client.login(username='testclient', password='password')
        self.client.post('/store/', self.test_payload)

        # test overriding an existing key
        self.client.post('/store/', {'animal':'dolphin'})
        retrieved = self.client.get('/retrieve/?animal&color')
        self.failUnlessEqual(retrieved.status_code, 200)
        self.failUnlessEqual(simplejson.loads(retrieved.content), {'1:animal':'dolphin', '1:color':'blue'})
