# This file is created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # check={'name':'Rohit Kashyap','place':'Pluto'}
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': "Remove Punctuations", 'analyzed_text': analyzed}
        # analyze the text
        # return render(request,'analyze.html',params)
        djtext = analyzed
    if fullcaps == "on":
        analyzed = djtext.upper()
        params = {'purpose': "Captialize the text", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': "Remove the New Liner", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    '''if extraspaceremover== "on":
        analyzed=""
        for i,char in enumerate(djtext):
            if djtext[i]==" " and djtext[i+1]=="  ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': "Remove the Extra space", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if charcount== "on":

        analyzed = "the no of charcter is"+len(djtext)
        count = 0
        for char in djtext:
            if char !='\n':
            #if char in ['a-z']:
                count = count + 1
            else:
                pass

        params = {'purpose': "Count the number of character", 'analyzed_text': count}
        #return "No of character count is :{}".format(count)'''


    if removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Please select any operation")
    
    return render(request, 'analyze.html', params)


def capfirst(request):
    return HttpResponse("Hello Wolrd! THis is capiatalizefirst Page")


def newlineremove(request):
    return HttpResponse("Hello Wolrd! THis is newlineremove Page")


def spaceremove(request):
    return HttpResponse("Hello Wolrd! THis is spaceremove Page")


def charcount(request):
    return HttpResponse("Hello Wolrd! THis is charcount Page")
