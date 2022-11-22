from django.shortcuts import render
from myapp.forms import ProfileForm
from myapp.models import Profile

# Create your views here.
def SaveProfile(request):
    saved = False

    if request.method == "POST":
        MyProfileform = ProfileForm(request.POST,request.FILES)
        if MyProfileform.is_valid():
            profile = Profile()
            profile.name = MyProfileform.cleaned_data["name"]
            profile.picture = MyProfileform.cleaned_data["picture"]
            profile.save()
            saved = True
        else:
            MyProfileform = ProfileForm()
        print(locals())
        return render(request, 'saved.html', locals())

def profile_create(request):
    return render(request,'profile.html')            

