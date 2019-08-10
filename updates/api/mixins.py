from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CSRFExemptMixin(object):
    """
    é para eliminar o erro do request do csrf
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
