from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    final_reversed_text = user_text[::-1]
    len_words = len(words)
    return render(request, 'reverse.html', {'usertext': user_text,
            'reversedtext': final_reversed_text, 'lenwords': len_words})


