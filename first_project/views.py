from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     #return HttpResponse("Hello")
#     #return HttpResponse("<h1>Hello!</h1>")
#     return HttpResponse('''<a href="https://www.whatsapp.com">Visit Whatsapp</a><br> 
#     <a href="https://www.youtube.com">Visit Youtube</a><br>
#     <a href="https://www.instagram.com">Visit Instagram</a>''')

# def removepunc(request):
#     text = request.GET.get('textarea', 'default')
#     print(text)
#     return HttpResponse("remove punctuation")

def analyze(request):
    text = request.POST.get('textarea','def')
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    lower = request.POST.get('lower', 'off')
    linemerge = request.POST.get('linemerge', 'off')
    remove_space = request.POST.get('remove_space', 'off')
    #print(text)
    
    if removepunc == 'on':
        punctuation = '''.,/?";':!@#$%^&*(){}[]-_'''
        analyzed = ""
        for i in text:
            if i not in punctuation:
                analyzed = analyzed + i
        param = {'purpose' : 'Remove Puncuation', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', param) 

    elif caps == 'on':
        analyzed = ""
        for i in text:
            analyzed = analyzed + i.upper()
        param = {'purpose' : 'Upper case', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', param) 

    elif lower == 'on':
        analyzed = ""
        for i in text:
            analyzed = analyzed + i.lower()
        param = {'purpose' : 'Lower case', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', param) 

    elif linemerge == 'on':
        analyzed = ""
        for i in text:
            if i != "\n" and i != "\r":
                analyzed = analyzed + i
        param = {'purpose' : 'Merge line', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', param)    

    elif remove_space == 'on':
        analysed = ""
        def remove(string):
            return string.replace(" ", "")
        for i in text:
            analyzed = analyzed + i
        param = {'purpose' : 'Merge line', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', param)    





    else:
        return HttpResponse("Error! Choose the checkbox")

def files(request):
    var = {'name' : 'Pushti', 'city' : 'Patna' }
    return render(request, 'index.html',var)

# def upper(request):
#     return HttpResponse("upper case")

# def lower(request):
#     return HttpResponse("lower case")

# def removespace(request):
#     return HttpResponse("remove space")

# def readfile(request):
#     with open('./text.txt','r') as f:
#         v = f.read()
#     return HttpResponse(v)