VERSION = (0, 1, 'pre')

__all__ = ('register',)

class AlreadyRegistered(Exception):
    """
    An attempt was made to register a model with the publisher more than once.
    """
    pass

registry = []

def register(model, published_attr='published', publicationDate_attr='publicationDate', published_manager_attr='public'):
    """
    Sets the given model class up for Publisher.
    """
 
    from django.db.models import signals as model_signals
    from django.db.models import FieldDoesNotExist, BooleanField, DateTimeField
    from django.utils.translation import ugettext as _
    
    from publisher.signals import pre_save
    from publisher.managers import PublisherManager

    
    if model in registry:
        return
    registry.append(model)

    # Add publisher options to the model's Options
    opts = model._meta
    opts.published_attr = published_attr
    opts.publicationDate_attr = publicationDate_attr
    opts.published_manager_attr = published_manager_attr
    
    # Add publisher fields if they do not exist
    for attr in [published_attr, publicationDate_attr]:
        try:
            opts.get_field(attr)
        except FieldDoesNotExist:
            if attr == published_attr:
                BooleanField(editable=True).contribute_to_class(model, attr)
            elif attr ==  publicationDate_attr:
                DateTimeField(editable=False,blank=True,null=True).contribute_to_class(model, attr)
  
    # Add a custom publisher manager
    PublisherManager(published_attr, publicationDate_attr).contribute_to_class(model, published_manager_attr)
    setattr(model, '_publisher_manager', getattr(model, published_manager_attr))

    # Set up signal receiver to manage the publisher when instances of the
    # model are about to be saved.
    model_signals.pre_save.connect(pre_save, sender=model) 