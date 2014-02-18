from django.test import TestCase
from django.db import IntegrityError
from pages.models import Page, Comment


def create_page(key, display_name, definition):
    p = Page.objects.create(word=key, display_name=display_name, definition=definition)
    return p


def create_comment(page, comment, rank):
    c = Comment.objects.create(page=page, comment=comment, rating=rank)
    return c


class PageTest(TestCase):
    def test_page_create(self):
        """
        Test page creation with alphanumeric key.
        """
        word = 'alphanumeric'
        name = 'Alphanumeric'
        definition = 'a combination of alphabetic and numeric characters'
        page = create_page(word, name, definition)
        self.assertIsNotNone(page)
        self.assertEqual(word, page.word)
        self.assertEqual(name, page.display_name)
        self.assertEqual(definition, page.definition)

    def test_page_no_key(self):
        """
        Test page creation with no key
        """
        definition = 'no key'
        self.assertRaises(IntegrityError, create_page, None, 'word', definition)

    def test_page_unique_key(self):
        """
        Test that no two pages can be created with the same key
        """
        word = 'same_key'
        display_name = 'Same key'
        definition = 'Two words with the same key'
        page1 = create_page(word, display_name, definition)
        self.assertRaises(IntegrityError, create_page, word, display_name, definition)

    def test_page_description_blank(self):
        """
        Test that the description can remain blank
        """
        key = 'word'
        name = 'Word'
        page = create_page(key, name, None)
        self.assertIsInstance(page, Page)

    def test_generate_page_with_five_comments(self):
        page = create_page('word', 'Word', 'A definition of a word')
        for i in xrange(5):
            create_comment(page, 'This is a terrbile page', 1)
        self.assertEqual(5, page.comment_set.count())