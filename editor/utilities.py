from .models import InterviewRoom
from django.utils import timezone

def RoomIdCheck(roomId):

    try:
        room = InterviewRoom.objects.get(token = roomId)
        return room

    except InterviewRoom.DoesNotExist:
        return InterviewRoom()

def RoomTimeCheck(room):

    print (room.startTime)
    print (room.endTime)
    current_time = timezone.now()

    if current_time >= room.startTime and current_time <= room.endTime:
        return True
    return False

def userCheck(room, id):

    if room.interviewee.email == id or room.interviewer.pk == id:
        return True
    return False
    
def freezeRoom(roomId):
    room = InterviewRoom.objects.get(token = roomId)
    room.freeze = True
    room.save()

def checkRoomState(roomId):
    room = InterviewRoom.objects.get(token = roomId)
    return room.freeze

def changeLang(roomId,Lang):
    room = InterviewRoom.objects.get(token=roomId)
    room.lang = Lang
    room.save()

def checkLang(roomId):
    room = InterviewRoom.objects.get(token = roomId)
    return room.lang

