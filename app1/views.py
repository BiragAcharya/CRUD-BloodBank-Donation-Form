from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Register
from .forms import donateBlood_edit


@login_required(login_url='login')


def AdminDashBoardPage(request):
    return render(request,'adminDashboard.html')
    # Renders the admin dashboard page

def DonorDashBoardPage(request):
    return render(request, 'donorDashboard.html')

def DonorHomePage(request):
    registers = Register.objects.all()
    # Retrieves all registers (donation records) from the database
    total_pending_requests = sum(register.unit for register in registers)
    # Calculates total pending requests by summing up the unit for each register
    return render(request, 'donorHome.html', {'total_pending_requests': total_pending_requests})
    # Renders the donor home page with total_pending_requests as context

def DonateBloodPage(request):
    return render(request, 'donateBlood.html', {})

@login_required(login_url='login')
def DonationHistoryPage(request):
    registers = Register.objects.all()
    # Retrieves all registers (donation records) from the database
    return render(request, 'donationHistory.html', {'registers': registers})
    # Renders the donation history page with registers as context

# def DonateBloodEditPage(request):
#     registers = Register.objects.all()
#     return render(request, 'donateBlood_edit.html', {})

# @login_required(login_url='login')
def DonateBloodEditPage(request,pk):
    item = Register.objects.get(id=pk)
    # Retrieves a specific register (donation record) by its primary key
    if request.method == 'POST':    
        # Binds the form with POST data and the retrieved instance
        form = donateBlood_edit(request.POST, instance = item)
        if form.is_valid():
            # Saves the form data if it is valid
            form.save()
            return redirect('donationHistory')
    else:
        form = donateBlood_edit( instance = item)
        # If it's a GET request, initializes the form with the retrieved instance
    
    context={
        'form':form,
        
    }
    return render(request, 'donateblood_edit.html', context)


def SignupPage(request):
    if request.method=='POST':
        # Extracts user information from the POST request
        user_type = request.POST.get('userType')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        age=request.POST.get('age')
        bloodgroup=request.POST.get('bloodGroup')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneNo')
        print(user_type)
        my_user=User.objects.create_user(username=username,password=password)
        # Creates a new user object
        my_user.save()
        # Redirects to the login page after successful signup
        print(username)
        print(password)
   # Save the user
        my_user.save()

        return redirect('login')

    return render(request,'signup.html')



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        password = request.POST.get('password')
        user_type = request.POST.get('userType')  # Get the selected user type
        print(user_type)
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Logs in the user and redirects to the donor dashboard
            return redirect('donorDashboard')

        #     # Redirect users to different home pages based on their roles
        #     if user_type == 'admin':
        #         return redirect('admin_home')  # Replace 'admin_home' with your admin home URL name
        #     # elif user_type == 'user':
        #     #     return redirect('userHome')   # Replace 'user_home' with your user home URL name
        #     elif user_type == 'donor':
        #         return redirect('donorHome')  # Replace 'donor_home' with your donor home URL name
        # else:
        #     return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    # Logs out the user and redirects to the login page
    return redirect('login')


def DonateBloodPage(request):
    if request.method == 'POST':
        # Extracts donation information from the POST request
        donorname = request.POST.get('donorName')
        bloodgroup = request.POST.get('bloodGroup')
        unit = request.POST.get('unit')
        age = request.POST.get('age')
        
        # Save the form data to the database
        donation_record = Register.objects.create(
            donorname=donorname,
            blood_group=bloodgroup,
            unit=unit,
            age=age
        )
        donation_record.save()

        return redirect('donorHome')
        # Redirects to the donor home page after successful donation

    return render(request, 'donateBlood.html')
    # Renders the donate blood page

def donateBlood_delete(request,id):
    blood =  Register.objects.filter(id=id)
    blood.delete()
    # Deletes a donation record based on its id
    return redirect('donationHistory')
    # Redirects to the donation history page after deletion

# from django.shortcuts import render, HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate


# def AdminDashBoardPage(request):
#     return render(request,'adminDashboard.html')

# def SignupPage(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         age = request.POST.get('age')
#         bloodgroup = request.POST.get('bloodGroup')
#         address = request.POST.get('address')
#         phoneno = request.POST.get('phoneNo')

#         try:
#             # Create the user
#             my_user = User.objects.create_user(username=username, password=password)
#             my_user.save()
#             return HttpResponse("User has been created successfully!")
#         except Exception as e:
#             # Handle any errors
#             return HttpResponse(f"Error occurred: {e}")

#         print(firstname, lastname, username, password, age, bloodgroup, address, phoneno)

#     return render(request, 'signup.html')

# def LoginPage(request):
#     return render(request,'login.html')
