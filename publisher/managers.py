from django.db import models

class PublisherManager(models.Manager):
    def __init__(self, published_attr, publicationDate_attr):
        super(PublisherManager, self).__init__()
        self.published_attr = published_attr
        self.publicationDate_attr = publicationDate_attr
    
    def get_query_set(self):
        filterargs = {self.published_attr : True}
        return super(PublisherManager, self).get_query_set().filter(**filterargs)