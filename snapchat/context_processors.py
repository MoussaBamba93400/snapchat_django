from django.conf import settings

def navigation_menu(request):
    return {
        'navigation_menu': getattr(settings, 'NAVIGATION_MENU', {})
    }
