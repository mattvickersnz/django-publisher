"""
Signal receiving functions which handle Publisher
related logic when model instances are about to be saved or deleted.
"""
from datetime import datetime

from django.db.models.query import Q

__all__ = ('pre_save',)

def pre_save(instance, **kwargs):
    """
    If this is being published, set the published date.
    """
    if kwargs.get('raw'):
        return
        
    opts = instance._meta
    
    published = getattr(instance, opts.published_attr)
    publicationDate = getattr(instance, opts.publicationDate_attr)
    
    if(published and publicationDate is None):
        setattr(instance, opts.publicationDate_attr, datetime.now())
        