import datetime

def add_time(dt, **kwargs):
    return dt + datetime.timedelta(**kwargs)

class FilterModule(object):

    def filters(self):
        return {
            'add_time': add_time
        }