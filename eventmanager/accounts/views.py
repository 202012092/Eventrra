
from django.http.response import HttpResponse
from django.shortcuts import render

from accounts.models import EventHostAccounts, VenueHolderAccounts, Venues

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

# Account Registrations

def ehregister(request):
    return render(request,'eventhostregister.html')

def vhregister(request):
    return render(request,'venueholderregister.html')

def ehaccount(request):

    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['emailid']
        passwrd = request.POST['password']
        cpasswrd = request.POST['conpassword']

        error_message = None
        if(not firstname):
            error_message = "First Name required"
        elif(not lastname):
            error_message = "Last Name required"
        elif(not email):
            error_message = "Email required"
        elif(not passwrd):
            error_message = "Password required"
        elif len(passwrd) < 3:
            error_message = "Password should be 4 or more characters long"
        elif(not cpasswrd):
            error_message = "Confirm Password required"
        elif passwrd != cpasswrd:
            error_message = "Passwords does not match"
        elif EventHostAccounts.objects.filter(email = email).exists():
            error_message = "Email already exists"
        
        if not error_message:
            eventhost = EventHostAccounts(first_name = firstname,last_name = lastname,email = email,password = passwrd)
            eventhost.save()

            return render(request, 'homepage.html',{'eh_success': 'Successfully Registered. Now you can login'})
        else:
            return render(request, 'eventhostregister.html', {'error': error_message})
    else:
        return render(request, 'eventhostregister.html')

def vhaccount(request):

    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['emailid']
        passwrd = request.POST['password']
        cpasswrd = request.POST['conpassword']

        error_message = None
        if(not firstname):
            error_message = "First Name required"
        elif(not lastname):
            error_message = "Last Name required"
        elif(not email):
            error_message = "Email required"
        elif(not passwrd):
            error_message = "Password required"
        elif len(passwrd) < 3:
            error_message = "Password should be 4 or more characters long"
        elif(not cpasswrd):
            error_message = "Confirm Password required"
        elif passwrd != cpasswrd:
            error_message = "Passwords does not match"
        elif VenueHolderAccounts.objects.filter(email = email).exists():
            error_message = "Email already exists"
        
        if not error_message:
            venueholder = VenueHolderAccounts(first_name = firstname,last_name = lastname,email = email,password = passwrd)
            venueholder.save()

            return render(request, 'homepage.html',{'vh_success': 'Successfully Registered. Now you can login'})
        else:
            return render(request, 'venueholderregister.html', {'error': error_message})
    else:
        return render(request, 'venueholderregister.html')

#Login

def ehlogin(request):

    if request.method == 'POST':
        email = request.POST['emailid']
        password = request.POST['password']

        error_message = None
        if(not email):
            error_message = "Email required"
        elif(not password):
            error_message = "Password required"
        elif not EventHostAccounts.objects.filter(email = email).exists():
            error_message = "Wrong Email"
        elif not EventHostAccounts.objects.filter(password = password).exists():
            error_message = "Wrong Password"
        
        if not error_message:
            eventhost = EventHostAccounts.objects.get(email = email)
            return render(request, 'ehlogin.html',{'eventhost':eventhost})
        else:
            return render(request, 'homepage.html', {'eh_error': error_message})
    else:
        return render(request, 'homepage.html')

def vhlogin(request):

    if request.method == 'POST':
        email = request.POST['emailid']
        password = request.POST['password']

        error_message = None
        if(not email):
            error_message = "Email required"
        elif(not password):
            error_message = "Password required"
        elif not VenueHolderAccounts.objects.filter(email = email).exists():
            error_message = "Wrong Email"
        elif not VenueHolderAccounts.objects.filter(password = password).exists():
            error_message = "Wrong Password"
        
        if not error_message:
            venueholder = VenueHolderAccounts.objects.get(email = email)
            return render(request, 'vhlogin.html',{'venueholder':venueholder})
        else:
            return render(request, 'homepage.html', {'vh_error': error_message})
    else:
        return render(request, 'homepage.html')

#Logout

def ehlogout(request):
    return render(request, 'homepage.html')

def vhlogout(request):
    return render(request, 'homepage.html')


#Venues

def addvenue(request):
    return render(request, 'addvenue.html')

def venueregister(request):
    if request.method == 'POST':
        venue_name = request.POST['vname']
        venue_address = request.POST['address']
        venue_description = request.POST['venuedesc']
        venue_cost = request.POST['venuecost']
        venue_capacity = request.POST['venuecap']
        venue_seating_type = request.POST['venuesit']
        venue_special_features = request.POST['venuefeat']

        error_message = None
        if(not venue_name):
            error_message = "Venue Name required"
        elif(not venue_address):
            error_message = "Address required"
        elif(not venue_description):
            error_message = "Description required"
        elif(not venue_cost):
            error_message = "Cost required"
        elif(not venue_capacity):
            error_message = "Capacity required"
        elif(not venue_seating_type):
            error_message = "Seating Type required"
        elif(not venue_special_features):
            error_message = "Special Features required"

        if not error_message:
            venueholder = Venues()
            venueholder.save()

            return render(request, 'vhlogin.html',{'v_success': 'Venue Successfully Added'})
        else:
            return render(request, 'addvenue.html', {'error': error_message})
    else:
        return render(request, 'vhlogin.html')