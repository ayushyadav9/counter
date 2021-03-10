from django.shortcuts import render
from Counter.forms import WordsForm,ChangeForm,FindForm
# Create your views here.
def Counter(request):
    if request.method=="POST":
        form1=WordsForm(request.POST)
        form2=ChangeForm(request.POST)
        form3=FindForm(request.POST)

        if form1.is_valid():
            print("H1")
            method=form1.cleaned_data['method']
            if method!="":
                txt=form1.cleaned_data['text']
                num=0
                if method=="With Spaces":
                    for i in txt:num+=1
                elif method=="Without Spaces":
                    for i in txt:
                        if i!=" ":
                            num+=1

                elif method=="Characteres":
                    for i in txt:
                        if i in '<>,.?/:;{}|~!@#$%^&*()_+=-`[]':
                            num+=1

                elif method=="Words":
                    num=len(txt.split())

                elif method=="Sentences":
                    for i in txt:
                        if i==".":
                            num+=1
                form1=WordsForm(initial={'result':num,'text':txt,'method':method})
            else:
                form1=WordsForm()
        if form2.is_valid():
            print("H2")
            method2=form2.cleaned_data['method2']
            if method2!="":
                txt2=form2.cleaned_data['input']
                if method2=="All upper":
                    out2=txt2.upper()
                elif method2=="All lower":
                    out2=txt2.lower()
                elif method2=="Capitalize first only":
                    out2=txt2.title()
                form2=ChangeForm(initial={'method2':method2,'input':txt2,'output':out2})
            else:
                form2=ChangeForm()

        if form3.is_valid():
            print("H3")
            method3=form3.cleaned_data['method3']
            if method3!="":
                txt3=form3.cleaned_data['paragraph']
                wrd3=form3.cleaned_data['word_to_find']

                if method3=="Case Sensitive":
                    print("hi")
                    l=len(wrd3)
                    out3=0
                    for i in range(len(txt3)-l):
                        print(i,l)
                        if txt3[i:i+l+1]==wrd3:
                            out3+=1
                elif method3=="Case invariant":
                    dmy=txt3.lower()
                    wrd4=wrd3.lower()
                    l=len(wrd4)
                    out3=0
                    for i in rnage(len(txt3)-l):
                        if txt3[i,i+l+1]==wrd4:
                            out3+=1
                form3=FindForm(initial={'method3':method3,'word_to_find':wrd3,'paragraph':txt3,'occurances':out3})
            else:
                form3=FindForm()

        return render(request,'counter/counter.html',{"form1":form1,"form2":form2,"form3":form3})
    else:
        form1=WordsForm()
        form2=ChangeForm()
        form3=FindForm()

        return render(request,'counter/counter.html',{"form1":form1,"form2":form2,"form3":form3})
