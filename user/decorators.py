from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomerUser, AdministratorUser


def allowed_users(allowed_role=""):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            if allowed_role == "Admin":
                if AdministratorUser.objects.filter(user=request.user):
                    return view_func(request, *args, **kwargs)
                else:
                    return render(request, 'auth/have_not_access.html')
            else:
                return render(request, 'auth/have_not_access.html')
        return wrapper_func
    return decorator
