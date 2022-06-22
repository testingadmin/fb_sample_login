from django.shortcuts import render, HttpResponseRedirect
from facebookpage.forms import UserRegistrationForm
from facebookpage.models import UserPerson


def add_show(request):
    if request.method == "POST":
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
        fm = UserRegistrationForm()
        # stud = User.objects.all()
        # print(fm)
    else:
        fm = UserRegistrationForm()
    stud = UserPerson.objects.all()
        # print(stud)
    return render(request, 'facebookpage/HtmlDemo.html', {"form": fm, "stu": stud})

