from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def words(request):
    full_text=request.GET['fulltext']
    word_list=full_text.split()
    word_dictionary={}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request,'words.html',{'text':full_text,'total':len(word_list),'dictionary':word_dictionary.items()})

def letters(request):
    full_text=request.GET['fulltext']
    upper_text=full_text.upper()
    letter_dictionary={}

    withBlank=len(full_text)
    withoutBlank=0
    for letter in full_text:
        if letter!=" ":
            withoutBlank+=1

    for letter in upper_text:
        if letter!=" ":
            if letter in letter_dictionary:
                letter_dictionary[letter]+=1
            else:
                letter_dictionary[letter]=1

    return render(request,'letters.html',{'text':full_text, 'with_blank':withBlank, 'without_blank':withoutBlank, 'dictionary':letter_dictionary.items()})
    