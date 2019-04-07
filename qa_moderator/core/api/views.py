from django.http import JsonResponse

import qa_moderator


def app_info(request):
    app_info = dict()
    app_info['version'] = qa_moderator.__version__
    return JsonResponse(app_info)
