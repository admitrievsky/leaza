
def xhr_flag(request):
    return {
        'xhr': bool(request.GET.get('xhr') or request.POST.get('xhr'))
        }