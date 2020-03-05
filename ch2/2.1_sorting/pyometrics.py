import time

class Metrics:

    def __init__(self, ref):
        self.calls = {}
        self.inject_spy_in_func(ref)

        
    def inject_spy_in_func(self, fn):
        self.safe_register(fn)
        self.inject(fn)

    
    def inject_spy_in_object(self, obj):
        pass

    def inject_spys_in_instance(self):
        #TODO: make generic
        pass
    
    def safe_register(self, fn):
        if not fn.__name__ in self.calls:
            self.calls[fn.__name__] = 0
            return True

    def inject(self, fn):
        origcode = fn.__code__
        fn.__code__ = compile('None', '', 'exec') # dereference the functions code
        
        def orig():
            pass
        orig.__code__ = origcode
        def spy(*args, **kwargs):
            start = 0
            self.calls[fn.__name__] += 1
            returnval = orig(*args, **kwargs)
            return returnval

        fn.__code__ = spy.__code__



    def _inject(self, instance, fn_name):
        if fn_name == '__class__':
            return
        self.calls[fn_name] = 0
        fn = getattr(instance, fn_name)
        def spy(*args, **kwargs):
            self.calls[fn_name] += 1
            start = 0
            returnval = fn(*args, **kwargs)
            end = 0
            return returnval
        
        setattr(instance, fn_name, spy)
        getattr(instance, fn_name).__name__ = fn_name
        
        
class Faker:

    def __init__(self):
        self.tally = 0

    def count(self):
        print(self)
        print(self.tally)
        self.tally += 1
        return self.tally 
    
    def test(self):
        print('testing testing 123')

