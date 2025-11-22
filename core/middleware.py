"""Middleware that adds a custom header and maintains a simple request counter.

Note: the request counter stores values in a file and is not suitable for
production or multi-process servers. It is intended only as a demonstration.
"""

import threading
from typing import Callable, Optional

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import HttpRequest, HttpResponse
import os


class CustomHeaderMiddleware(MiddlewareMixin):
    """Add a custom header to every response."""

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        response['X-Custom-App'] = 'CustomizationDemo/1.0'
        return response


class RequestCountMiddleware(MiddlewareMixin):
    """A simple middleware that counts requests by incrementing a file.

    This implementation is protected by a threading lock to reduce races in
    a single-process deployment, but it is not safe for multi-process
    servers. Use a shared counter (Redis, Prometheus) in production.
    """

    _lock = threading.Lock()

    def __init__(self, get_response: Optional[Callable] = None) -> None:
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

    def process_request(self, request: HttpRequest) -> None:
        """Increment the request counter stored in a file.

        Args:
            request: The Django HttpRequest instance.
        """
        with self._lock:
            try:
                with open(self.count_file, 'r') as f:
                    val = int(f.read() or '0')
            except Exception:
                val = 0
            val += 1
            with open(self.count_file, 'w') as f:
                f.write(str(val))
