import json
from django.shortcuts import render, HttpResponse
from editor.helper import compileAndRun
from .models import InterviewRoom
from .utilities import RoomIdCheck, RoomTimeCheck, userCheck, freezeRoom, checkRoomState, checkLang, changeLang
from django.shortcuts import render, redirect


# Create your views here.
def Edit(request, roomId):
    
    room = RoomIdCheck(roomId)

    if room.pk:
        time_check = RoomTimeCheck(room)
        if time_check:
            if 'email' in request.session:
                freeze_valid = False
                user_check = userCheck(room, request.session['email'])
                if request.session['user_type'] == "Interviewer":
                    freeze_valid = True
                if user_check: 
                    return render(request, 'editor/editor.html',
                                  {'question': room.question, 'freeze': room.freeze, 'lang': room.lang, 'freeze_valid': freeze_valid})
    
    return redirect('Login:home')


def Run(request):

    if request.method == "POST":
        request_getdata = request.POST.get('params', None) 
        object_getdata = json.loads(request_getdata)
        output = compileAndRun(object_getdata["source"], object_getdata["lang"], object_getdata["input"])
        return HttpResponse(json.dumps({'output': output}), content_type="application/json")

def Freeze(request, roomId):

    freezeRoom(roomId)
    return redirect('editor:editor', roomId = roomId)

def Check(request, roomId):

    state = checkRoomState(roomId)
    return HttpResponse(json.dumps({'state': state}), content_type="application/json")

def langchange(request, roomId):
    request_getdata = request.POST.get('params', None)
    lang = json.loads(request_getdata)
    changeLang(roomId, lang)
    return redirect('editor:editor', roomId=roomId)

def langcheck(request,roomId):
    language = checkLang(roomId)
    return HttpResponse(json.dumps({'language': language}), content_type='application/json')