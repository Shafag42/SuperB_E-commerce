from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden 
from core.models import BlockedIP
  

class BlockIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blocked_ips = BlockedIP.objects.all()
        blocked_ip_QS = [ip.ip_addr for ip in blocked_ips]
        if request.META['REMOTE_ADDR'] in blocked_ip_QS:
            return HttpResponseForbidden('<h1>Permission Denied</h1>')
        # return request

    def process_exception(self, request, exception):
        print(request.path)
        print(exception)