from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login,logout
# def registerUser(request):
    # if request.method=='POST':
    #     form=Userregistrationform(request.POST)
        
    # else:
    #     form=Userregistrationform()
    # return render(request,'registerUser.html',{'form':form})
    # form=Userregistrationform()

    # context={
    #     'from':form,
    # }
    # return render(request,'registerUser.html',context)

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,userloginform

def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:index')  # Redirect to a login page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registerUser.html', {'form': form})

def login(request):
    if request.method=='POST':
        # email=request.POST.get('email')
        form=userloginform(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index:index')
        else:
            error_message="invalid username or password please try again."
    else:
        form=userloginform()
        error_message=None
    return render(request,'login.html',{'form':form,'error_message': error_message})

def logout_view(request):
        logout(request)
        return redirect('sign-up:login')