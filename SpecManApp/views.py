from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from SpecManApp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import  login_required

# Create your views here.
#Index Page=> Home Page

#index=home
def index(request) :
    return render(request, 'SpecManApp/index.html')

def about(request):
    return render(request, 'SpecManApp/about.html')
    
    
"""def  register(request) :
    registered = False
    
    
    #HTTP Post
    if request.method == 'POST' :
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data = request.POST)
        
        #Valid forms?
        if user_form.is_valid() and profile_form.is_valid() :
            #save user info on the DB
            user = user_form.save()
            
            #Hashing the Password
            user.set_password(user.password)
            user.save()
            
        #User Profile Instance
            profile = profile_form.save(commit =False)
            profile.user = user
            
            if 'picture' in request.FILES :
                profile.picture = request.FILES['picture']
                
            #Save the UserProfile
            profile.save()
                
            #Registration Complete => Update Flag
            registered = True
            
            #Invalid Form 
        else :
            print(user_form.errors, profile_form.errors)
    else :
        user_form =UserForm()
        profile_form = UserProfileForm()
    #Render Registration Template
    return render(request,
            'SpecManApp/register.html',
            #'SpecManApp/templates/registration/registration_form.html',
            {'user_form': user_form, 'profile_form':profile_form, 'registered':registered})  
 """               

"""def user_login(request):
    #Get info => HTTP Post
    if request.method =='POST' :
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #Authenticating the User
        
        user = authenticate(username=username, password=password)
        
        if user :
             
             if user.is_active :
                 login(request,user)
                 return HttpResponseRedirect('/SpecManApp/')
                
             else :
                 #Inactive Account : 
                 return HttpResponse("Account Disabled")
        else :
            print("Invalid Login Credentials: {0},{1}".format(username, password))
            return HttpResponse("Invalid login Details Supplied")
    else :
        return render(request, 'SpecManApp/login.html', {})
        #return render(request,'/SpecManApp/templates/registration/login.html',{})
        
 """       
        
"""@login_required       
def user_logout(request) :
    logout(request)
    
    return HttpResponseRedirect('/SpecManApp/')
    """
    
  
  