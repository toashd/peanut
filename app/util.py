#!/usr/bin/env python

from functools import wraps
from flask import request, redirect, current_app

def requires_ssl(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("SSL"):
            if request.is_secure:
                return fn(*args, **kwargs)
            else:
                print(' * Secure redirect')
                return redirect(request.url.replace("http://", "https://"))

        return fn(*args, **kwargs)

    return decorated_view

