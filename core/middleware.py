import threading
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import os


class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-Custom-App'] = 'CustomizationDemo/1.0'
        return response


class RequestCountMiddleware(MiddlewareMixin):
    _lock = threading.Lock()

    def __init__(self, get_response=None):
        super().__init__(get_response)
        log_dir = getattr(settings, 'LOG_DIR', None)
        if not log_dir:
            log_dir = os.path.join(settings.BASE_DIR, 'logs')
        self.count_file = os.path.join(log_dir, 'request_count.txt')
        # ensure file exists
        os.makedirs(log_dir, exist_ok=True)
        if not os.path.exists(self.count_file):
            with open(self.count_file, 'w') as f:
                f.write('0')

    def process_request(self, request):
        # increment counter in a file (simple, not optimized)
        with self._lock:
            try:
                with open(self.count_file, 'r') as f:
                    val = int(f.read() or '0')
            except Exception:
                val = 0
            val += 1
            with open(self.count_file, 'w') as f:
                f.write(str(val))
