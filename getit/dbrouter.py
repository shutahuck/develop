# DB router for getit

class GetItDBRouter(object):
    """
    A router to control getit db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on getit models to 'default'"
        from django.conf import settings
        if not settings.DATABASES.has_key('getit'):
            return None
        if model._meta.app_label == 'getit':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on getit models to 'default'"
        from django.conf import settings
        if not settings.DATABASES.has_key('getit'):
            return None
        if model._meta.app_label == 'getit':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in getit is involved"
        from django.conf import settings
        if not settings.DATABASES.has_key('getit'):
            return None
        if obj1._meta.app_label == 'getit' or obj2._meta.app_label == 'getit':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the getit app only appears on the 'getit' db"
        from django.conf import settings
        if not settings.DATABASES.has_key('getit'):
            return None
        if db == 'default':
            return model._meta.app_label == 'getit'
        elif model._meta.app_label == 'getit':
            return False
        return None