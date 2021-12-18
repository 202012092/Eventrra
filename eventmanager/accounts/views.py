
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from accounts.models import EventCategories, EventHostAccounts, Events, VenueHolderAccounts, Venues

eh_current_user = None
vh_current_user = None
vhvenuelist = None
editrow = None
bookevent = None

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
            global eh_current_user
            eh_current_user = eventhost
            venuelist = Venues.objects.all()
            return render(request, 'ehlogin.html',{'eventhost':eh_current_user,'allvlist':venuelist})
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
            global vh_current_user
            vh_current_user = venueholder
            global vhvenuelist
            vhvenuelist = Venues.objects.filter(venue_holder_id = vh_current_user.venueholder_id)
            return render(request, 'vhlogin.html',{'venueholder':vh_current_user,'vlist':vhvenuelist})
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
    cats = EventCategories.objects.all()
    return render(request, 'addvenue.html',{'cats':cats})

def venueregister(request):
    if request.method == 'POST':
        venue_name = request.POST['vname']
        venue_address = request.POST['address']
        venue_description = request.POST['venuedesc']
        venue_cost = request.POST['venuecost']
        venue_capacity = request.POST['venuecap']
        venue_seating_type = request.POST['venuesit']
        venue_special_features = request.POST['venuefeat']
        category_id = request.POST['categories']
        cat = EventCategories.objects.get(category_id = category_id)
        venue_image = request.FILES['image']

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
        elif(not venue_image):
            error_message = "Venue Image required"

        if not error_message:
            venue = Venues(venue_name = venue_name,venue_address = venue_address, venue_description = venue_description, venue_cost = venue_cost, venue_capacity = venue_capacity, venue_seating_type = venue_seating_type, venue_special_features = venue_special_features, category_id = cat, venue_holder_id = vh_current_user, venue_image = venue_image)
            venue.save()

            global vhvenuelist
            vhvenuelist = Venues.objects.filter(venue_holder_id = vh_current_user.venueholder_id)
            return render(request, 'vhlogin.html',{'v_success': 'Venue Successfully Added','venueholder':vh_current_user,'vlist':vhvenuelist})
        else:
            return render(request, 'addvenue.html', {'error': error_message})
    else:
        return render(request, 'addvenue.html')

def editvenue(request, data):
    global editrow
    editrow = Venues.objects.get(venue_id = data)
    cats = EventCategories.objects.all()
    return render(request, 'editvenue.html',{'venue':editrow,'cats':cats})

def deletevenue(request, data):
    deleterow = Venues.objects.get(venue_id = data)
    deleterow.delete()
    global vhvenuelist
    vhvenuelist = Venues.objects.filter(venue_holder_id = vh_current_user.venueholder_id)
    return render(request, 'vhlogin.html',{'v_success': 'Venue Successfully Deleted','venueholder':vh_current_user,'vlist':vhvenuelist})

def venueupdate(request):
    if request.method == 'POST':
        editrow.venue_name = request.POST['vname']
        editrow.venue_address = request.POST['address']
        editrow.venue_description = request.POST['venuedesc']
        editrow.venue_cost = request.POST['venuecost']
        editrow.venue_capacity = request.POST['venuecap']
        editrow.venue_seating_type = request.POST['venuesit']
        editrow.venue_special_features = request.POST['venuefeat']
        category_id = request.POST['categories']
        cat = EventCategories.objects.get(category_id = category_id)
        editrow.category_id = cat

        if len(request.FILES) != 0:
            editrow.venue_image = request.FILES['image']
        editrow.save()
        global vhvenuelist
        vhvenuelist = Venues.objects.filter(venue_holder_id = vh_current_user.venueholder_id)
        return render(request, 'vhlogin.html',{'v_success': 'Venue Successfully Edited','venueholder':vh_current_user,'vlist':vhvenuelist})
    else:
        return render(request, 'editvenue.html')




#Venue Template

def venuedynamic(request, data):
    venue = Venues.objects.get(venue_id = data)
    global bookevent
    bookevent = venue
    category = EventCategories.objects.get(category_id = venue.category_id_id)
    venueholder = VenueHolderAccounts.objects.get(venueholder_id = venue.venue_holder_id_id)
    return render(request, 'venuedisplay.html',{'venue':venue,'category':category,'venueholder':venueholder})


#Event Booking

def eventbook(request):
    if request.method == 'POST':
        date = int(request.POST['date'])
        month = int(request.POST['month'])
        stime = int(request.POST['stime'])
        etime = int(request.POST['etime'])
        attendees = int(request.POST['attendees'])
        
        global eh_current_user
        global bookevent

        error_message = None
        if(not date):
            error_message = "Date is required"
        elif(not month):
            error_message = "Month is required"
        elif(not stime):
            error_message = "Start Time is requried"
        elif(not etime):
            error_message = "End Time is required"
        elif(not attendees):
            error_message = "Attendees is required"
        elif(date > 30 and (month == 4 or month == 6 or month == 9 or month == 11)):
            error_message = "Invalid Date"
        elif((month == 2) and date > 28):
            error_message = "Invalid Date"
        temp = Events.objects.filter(event_month = month, event_date = date, start_time = stime, end_time = etime).count()
        #temp2 = temp.filter(event_date = date)
        #temp3 = temp2.filter(start_time_lte = stime)Saving _lte for <=
        #temp4 = temp3.get(end_time_gte = etime) Saving _gte for >=
        if(temp > 0):
            error_message = "This timeslot is not available"

        if not error_message:
            event = Events(event_date=date,event_month=month,start_time=stime,end_time=etime,event_attendees=attendees,event_host=eh_current_user,venue=bookevent)
            event.save()
            return render(request,'eventbooking.html',{'success': 'Event Successfully Booked'})
        else:
            return render(request,'eventbooking.html',{'error':error_message})
    else:
        return render(request, 'venuedisplay.html')