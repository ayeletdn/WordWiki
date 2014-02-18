from django.core.management.base import BaseCommand
from pages.models import Page, Comment
import random
import string


def rand_letter():
    return random.choice(string.lowercase)


def rand_word():
    return "".join([rand_letter() for i in xrange(random.randint(4, 10))])


def rand_sentence():
    return " ".join([rand_word() for i in xrange(random.randint(10, 30))])


def rand_paragraph():
    return ".  ".join([rand_sentence() for i in xrange(random.randint(3, 10))]) + "."


def rand_definition():
    return "\n".join([rand_paragraph() for i in xrange(random.randint(3, 10))])

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        for page in Page.objects.filter(comments__isnull=True):
            page.comments.add(Comment(comment=rand_sentence(), rating=random.randint(1, 5)))

        for page in Page.objects.filter(definition=None):
            page.definition = rand_definition()
            page.save()