from django.core.urlresolvers import reverse
from django.db import models


class Page(models.Model):
    word = models.CharField(max_length=200, unique=True)
    display_name = models.CharField(max_length=200)
    definition = models.TextField(null=True)

    class Meta:
        ordering = (
            'display_name',
        )

    def __unicode__(self):
        return self.display_name

    def comments_count(self):
        return self.comments.count()

    def short_definition(self):
        return self.definition[:97] + "..." if len(self.definition) > 97 else self.definition

    # def get_absolute_url(self):
    #     return reverse('pages.views.detail', args=[self.id])


class Comment(models.Model):
    page = models.ForeignKey(Page, related_name='comments')  #related_name is used for relating from page to it's comments
    rating = models.IntegerField(choices=[(x, x) for x in xrange(1, 6)])
    comment = models.TextField()
