import json
from django.shortcuts import render, HttpResponse
from editor.helper import compileAndRun
from .models import InterviewRoom
from .utilities import RoomIdCheck, RoomTimeCheck, userCheck
from django.shortcuts import render, redirect


# Create your views here.
def Edit(request, roomId):
    
    print (roomId)
    room = RoomIdCheck(roomId)

    if room.pk:
        time_check = RoomTimeCheck(room)
        if time_check:
            if 'email' in request.session:
                user_check = userCheck(room, request.session['email'])
                if user_check: 
                    print (room.question)
                    return render(request, 'editor/editor.html', {'question': room.question})
    
    return redirect('Login:home')


def Run(request):

    if request.method == "POST":
        request_getdata = request.POST.get('params', None) 
        object_getdata = json.loads(request_getdata)
        output = compileAndRun(object_getdata["source"], object_getdata["lang"], object_getdata["input"])
        return HttpResponse(json.dumps({'output': output}), content_type="application/json")