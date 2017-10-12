# DB router for edutime

class EdutimeDBRouter(object):
    """
    A router to control edutime db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on edutime models to 'edudb'"
        from django.conf import settings
        if not settings.DATABASES.has_key('edutime'):
            return None
        if model._meta.app_label == 'edutime':
            return 'edudb'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on edutime models to 'edudb'"
        from django.conf import settings
        if not settings.DATABASES.has_key('edutime'):
            return None
        if model._meta.app_label == 'edutime':
            return 'edudb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in edutime is involved"
        from django.conf import settings
        if not settings.DATABASES.has_key('edutime'):
            return None
        if obj1._meta.app_label == 'edutime' or obj2._meta.app_label == 'edutime':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the edutime app only appears on the 'edutime' db"
        from django.conf import settings
        if not settings.DATABASES.has_key('edutime'):
            return None
        if db == 'edudb':
            return model._meta.app_label == 'edutime'
        elif model._meta.app_label == 'edutime':
            return False
        return None