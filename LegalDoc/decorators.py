from django.http import HttpResponseForbidden
from django.shortcuts import render


def group_required(groups_list):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user_groups = request.user.groups.values_list('name', flat=True)
            if any(group_name in user_groups for group_name in groups_list):
                return view_func(request, *args, **kwargs)
            else:

                #return HttpResponseForbidden('You do not have permission to access this page.')
                return HttpResponseForbidden(render(request, '403.html'))

        return wrapper

    return decorator
