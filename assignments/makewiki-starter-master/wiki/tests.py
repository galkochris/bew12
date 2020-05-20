  
from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page
from django.utils.text import slugify

# Create your tests here.
class WikiPageTest(TestCase):

    def test_wiki_details_page_test(self):
        user = User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        page = Page.objects.create(title="test page", content="test", author=user)
        page.save()

        response = self.client.get('/%s/' %slugify(page.title))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    def test_wiki_detail_page_edit(self):
        user = User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        page = Page.objects.create(title="test page", content="test", author=user)
        page.save()
        edit = {
            'title': 'title',
            'content': 'content'
        }

        response = self.client.post('/%s/' %slugify(page.title), edit)
        updated = Page.objects.get(title = edit['title'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated.title, edit['title'])


    def test_wiki_creation_page_test(self):
        user = User.objects.create_user(username='me', password='djangopony')
        self.client.login(username='me', password='djangopony')

        create = {
            'title': 'title',
            'content': 'content'
        }

        response = self.client.post('/wiki/create/', create)
        updated = Page.objects.get(title = create['title'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated.title, create['title'])