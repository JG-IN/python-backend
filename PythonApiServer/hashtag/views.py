from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_context_data(request):
    # print('request : {}'.format(request))

    # return JsonResponse({'data':'a'})
    return render(request, '/workspace/PythonApiServer/PythonApiServer/hashtag/templates/index.html')

def room(request, room_name):
    print('request : {}'.format(request))
    # return JsonResponse({'data':'a'})
    return render(request, '/workspace/PythonApiServer/PythonApiServer/hashtag/templates/test.html', {
        'room_name': room_name
    })