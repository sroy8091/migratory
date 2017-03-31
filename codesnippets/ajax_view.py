@login_required
@require_POST
def upload(request):
    image_id = request.POST.get('id')
    # action = request.POST.get('action')
    if image_id=="12":
        try:
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})