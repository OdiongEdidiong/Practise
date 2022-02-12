from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
def greet(request):
    print("hello")
    return HttpResponse("Hello there")

def greetjon(request):
    return HttpResponse ("hello jon")

def greetanyone(request,name):
    return HttpResponse(f"hello {name}")

def multiply(a,b):
    return a*b
def findsqr(request,num):
    return HttpResponse(multiply(num,num))

def iseven(request,num):
    if num%2==0:
        val="even"
    else:
        val="odd"
    return render(request,"first_app/even.html",{"value":val})

    # using for loop in html

def cube(request,number):
    cubed={}
    for num in range(number+1):
        cubed[num]=num**3
    return render(request,"first_app/cubes.html",{"cubed":cubed})

    # using conditionals in html
import datetime as dt
def newyear(request):
    now = dt.datetime.now()
    return render(request,"first_app/Isitnewyear.html",{"now": now})


    # moving from one view to another via html ##
    # getting data from the front End
        #more complex method
from django import forms
class logininfo(forms.Form):
    Name=forms.CharField(max_length=79)
    email_address=forms.EmailField()
    sex=[("1","Male"),("2","Female"),("3","Custom")]
    Gender=forms.ChoiceField(choices=sex)

def getinfo(request):
    return render(request,"first_app/logininfo.html",{"form":logininfo()})

class bestteam(forms.Form):
    Do_You_love_football=forms.ChoiceField(choices=[("1","Yes"),("2","No")])
    Best_Football_Team=forms.CharField(max_length=45)
def teams(request):
    if request.method=="POST":
        print("This is a POST request")
        best=bestteam(request.POST)
        if best.is_valid():
            print(best.cleaned_data["Best_Football_Team"])
            team=best.cleaned_data["Best_Football_Team"]
            return render(request,"first_app/football.html",{"teams":bestteam(),"team":team})
    return render(request,"first_app/football.html",{"teams":bestteam()})


class SqrDet(forms.Form):
    number = forms.IntegerField(max_value=2013)

def mult(a, b):
    return a * b
def find_sqr(request):
    if request.method == 'POST':
        form = SqrDet(request.POST)
        if form.is_valid():
            num = form.cleaned_data['number']
            sqr = mult(num, num)
            return render(request, 'first_app/squarefinder.html', {"form": SqrDet(), 'sqr': sqr, "num": num})

    return render(request, 'first_app/squarefinder.html', {"form": SqrDet()})
        #simpler method
    # sessions
    # mini project -> polling unit
class voteform(forms.Form):
    name = forms.CharField(max_length=70)
    parties=[("PDP","PDP"),("APC","APC"),("ANPC","ANPC"),("LP","LP")]
    candidate=forms.ChoiceField(choices=parties)

def poll(request):
    if request.method=="POST":
        details=voteform(request.POST)
        if details.is_valid():
            name=details.cleaned_data.get("name")
            choice=details.cleaned_data["candidate"]
            print(name,choice)
            if "votes" not in request.session:
                request.session["votes"]="{}"
            votes=eval(request.session["votes"])
            if name in votes.keys():
                msg=f"{name} has already voted!"
            else:
                votes[name]=choice
                msg=f"Thanks for your contribution {name}"
            request.session["votes"]=str(votes)
            print(votes)
            return render(request,"first_app/pollingunit.html",{
        "voteform":voteform(), "msg":msg
                            })
    return render(request,"first_app/pollingunit.html",{
        "voteform":voteform()
    })
def count_votes(request):
    votes= eval(request.session.get("votes")) or {}
    counts={}
    for voter,party in votes.items():
        if party not in counts:
            counts[party]=1
        else:
            counts[party]+=1
    return counts

def maxvote(request):
    all_votes = count_votes(request)
    winner=None
    winners_votes=0
    for party,count in all_votes.items():
        if count > winners_votes:
            winner=party
            winners_votes=count
    return render(request,"first_app/results.html",{"all_votes": all_votes,"winner":winner,"winners_votes":winners_votes})

def clear_votes(request):
    request.session['votes'] = '{}'
    msg = 'Welcome to a new election process, please keep everything free and fair'
    return render(request,"first_app/pollingunit.html",{
        "voteform":voteform(), "msg":msg
                            })

class name(forms.Form):
    names= forms.CharField(max_length=70)

def tell(request):
    if request.method=="POST":
        called=name(request.POST)
        if called.is_valid():
            nam=called.cleaned_data.get("names")
            nam=nam
            if len(nam) < 5:
                msg=f"{nam} is a short word"
            elif len(nam) < 10:
                 msg=f"{nam} is a long word"
            else:
                msg=f"{nam} is a pretty long word"
            return render(request,"first_app/name.html",{"name":name(),"msg":msg})
    return render(request,"first_app/name.html",{"name":name()})