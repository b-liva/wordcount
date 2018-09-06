import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # print('this is homePage')
    return render(request, 'home.html', {'hi': 'this is me'})


def count(request):
    # return HttpResponse('eggs')
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            print('thats it')
            worddictionary[word] += 1
        else:
            #add to the dicitonary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'length': len(wordlist), 'sortedwords': sortedwords})

def aboutus(request):
    return render(request, 'aboutus.html')
