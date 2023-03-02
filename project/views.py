from django.http import HttpResponse,JsonResponse

def novin_test(request):
    return HttpResponse('<h1> hi novin </h1>')

def json_test(request):
    return JsonResponse({'name':'novin'})
