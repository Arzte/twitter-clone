from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from notification.models import Notification


@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user)
    renderer = render(request, 'notifications.html', {
        'notifications': notifications
    })
    notifications.delete()

    return renderer
