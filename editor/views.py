from django.shortcuts import render, HttpResponse
from editor.helper import compileAndRun
import json 

# Create your views here.
def Edit(request):
    return render(request, 'editor/editor.html', {})

def Run(request):

    if request.method == "POST":
        request_getdata = request.POST.get('params', None) 
        object_getdata = json.loads(request_getdata)
        output = compileAndRun(object_getdata["source"], object_getdata["lang"], object_getdata["input"])
        return HttpResponse(json.dumps({'output': output}), content_type="application/json")