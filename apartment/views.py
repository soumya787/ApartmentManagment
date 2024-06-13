from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
import random
import array
import datetime
import smtplib, ssl
import os
from email.message import EmailMessage

# Create your views here.
from apartment.models import Owner, Gender, MaritalStatus, Block, MemberType, Designation, Association, Familymember, \
    Relation, Visitor, RegularVisitor, Amenities, TimingSlot, Booking

sender = "soumyashreenidhi@gmail.com"
password = "nidhi@4792"


def generate_pswd():
    # maximum length of password needed this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    temp_pass_list = []
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    return password


def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contactus.html')


def forpswd(request):
    if request.method == 'POST':
        owner = Owner.objects.get(Q(email=request.POST['txtMail']) & Q(cell=request.POST['txtCell']))
        owner.password = generate_pswd()
        owner.save()
        return redirect('log')
    else:
        return render(request, 'forgotpassword.html')


def cancel_pswd(request):
    return redirect('log')


def logfunc(request):
    if request.method == "POST":
        x = request.POST['option']
        username = request.POST['txtname']
        pswd = request.POST['txtpswd']
        user = authenticate(request, username=username, password=pswd)
        if x == 'manager':
            if user is not None and user.is_superuser:
                return redirect('asocihome')
        elif x == 'owner' or x == 'tenant':
            getdata = Owner.objects.get(fname=username)
            request.session['Username'] = username
            request.session['id'] = getdata.id
            # print(getdata)
            return render(request, 'owner/owner_home.html', {'data': username, 'getdata': getdata.id})
    else:
        return render(request, 'login.html')


def ownerpage(request):
    return render(request, 'owner/ownerreg.html')


def ownerreg(request):
    owner = Owner()
    owner.fname = request.POST['txtfname']
    owner.lname = request.POST['txtlname']
    owner.age = int(request.POST['txtage'])
    owner.cell = int(request.POST['txtphn'])
    owner.gender = Gender.objects.get(id=request.POST['gender'])
    owner.email = request.POST['txtemail']
    owner.martial_status = MaritalStatus.objects.get(id=request.POST['marital'])
    owner.occupation = request.POST['txtocc']
    owner.company = request.POST['txtCom']
    owner.officeaddress = request.POST['addresss']
    owner.block = Block.objects.get(id=request.POST['blocks'])
    owner.flatnum = request.POST['txtflatno']
    owner.membertype = MemberType.objects.get(id=request.POST['member'])
    owner.password = generate_pswd()
    user = User.objects.create_user(email=owner.email, password=owner.password, username=owner.fname)
    user.save()
    owner.save()
    return redirect('ownerpage')


def get_ownerdata(request):
    get_data = Owner.objects.all()
    return render(request, 'owner/ownerdetails.html', {'data': get_data})


def editowner(request, id):
    ownerdata = Owner.objects.get(id=id)
    if request.method == "POST":
        ownerdata.fname = request.POST['txtfname']
        ownerdata.lname = request.POST['txtlname']
        ownerdata.age = int(request.POST['txtage'])
        ownerdata.cell = int(request.POST['txtphn'])
        ownerdata.gender = Gender.objects.get(id=request.POST['gender'])
        ownerdata.email = request.POST['txtemail']
        ownerdata.martial_status = MaritalStatus.objects.get(id=request.POST['marital'])
        ownerdata.occupation = request.POST['txtocc']
        ownerdata.company = request.POST['txtCom']
        ownerdata.officeaddress = request.POST['addresss']
        ownerdata.block = Block.objects.get(id=request.POST['blocks'])
        ownerdata.flatnum = request.POST['txtflatno']
        ownerdata.membertype = MemberType.objects.get(id=request.POST['member'])
        ownerdata.save()
        get_data = Owner.objects.all()
        return render(request, 'owner/ownerdetails.html', {'data': get_data})
    return render(request, 'owner/editowner.html', {'x': ownerdata})


def deleteowner(request, id):
    ownerdata = Owner.objects.get(id=id)
    ownerdata.delete()
    get_data = Owner.objects.all()
    return render(request, 'owner/ownerdetails.html', {'data': get_data})


# -----------------------------------------------------------------------------------------
# Association Manager Pages
# -----------------------------------------------------------------------------------------
def ass_home(request):
    return render(request, 'association/associ_manager_home.html')


def associ_logout(request):
    return redirect('home')


def associmember(request):
    associ_data = Association.objects.all()
    return render(request, 'association/asoci_member.html', {'data': associ_data})


def addmem(request):
    get_data = Owner.objects.all()
    return render(request, 'association/add_asssociation.html', {'data': get_data})


def add_association_mem(request):
    get_data = Owner.objects.get(fname=request.POST['txtfname'])
    associ = Association()
    if request.POST['txtfname'] == get_data.fname:
        associ.fname = request.POST['txtfname']
        associ.lname = get_data.lname
        associ.age = get_data.age
        associ.cell = get_data.cell
        associ.gender = Gender.objects.get(id=get_data.gender_id)
        associ.email = get_data.email
        associ.block = Block.objects.get(id=get_data.block_id)
        associ.flatnum = get_data.flatnum
        associ.desig_name = Designation.objects.get(id=request.POST['desig'])
        associ.save()
        associ_data = Association.objects.all()
        return render(request, 'association/asoci_member.html', {'data': associ_data})
    return render(request, 'association/add_asssocition.html')


def delete_association_mem(request, id):
    get_data = Association.objects.get(id=id)
    get_data.delete()
    return redirect('associmember')


def update_association_mem(request, id):
    associ = Association.objects.get(id=id)
    get_data = Owner.objects.all()
    # associ = Association()
    if request.method == 'POST':
        get_data = Owner.objects.get(fname=request.POST['txtfname'])
        if request.POST['txtfname'] == get_data.fname:
            associ.fname = request.POST['txtfname']
            associ.lname = get_data.lname
            associ.age = get_data.age
            associ.cell = get_data.cell
            associ.gender = Gender.objects.get(id=get_data.gender_id)
            associ.email = get_data.email
            associ.block = Block.objects.get(id=get_data.block_id)
            associ.flatnum = get_data.flatnum
            associ.desig_name = Designation.objects.get(id=request.POST['desig'])
            associ.save()
            associ_data = Association.objects.all()
            return render(request, 'association/asoci_member.html', {'data': associ_data})
    return render(request, 'association/edit_association.html', {'data': associ, 'get_owner': get_data})


# ------------------------------------------------------------------------------
# Owner Pages ----------------------------------------------------------------
# --------------------------------------------------------------------------------


def ownerTenant(request):
    return render(request, 'owner/owner_home.html',
                  {'data': request.session['Username'], 'getdata': request.session['id']})


def view_owner_tenant_family(request, id):
    getdata = Owner.objects.get(id=id)
    alldata = Familymember.objects.filter(memberid=id)
    return render(request, 'owner/FamilyMemberPage/view_family.html', {'x': getdata.id, 'y': alldata})


def addownerfamily(request, id):
    getdata = Owner.objects.get(id=id)
    if request.method == 'POST':
        family = Familymember()
        family.name = request.POST['txtName']
        family.age = request.POST['txtAge']
        family.cell = request.POST['txtCell']
        family.gender = Gender.objects.get(id=request.POST['gender'])
        family.relation = Relation.objects.get(relation_type=request.POST['ddlRelation'])
        family.memberid = Owner.objects.get(id=id)
        family.save()
        getall = Familymember.objects.filter(memberid=id)
        return render(request, 'owner/FamilyMemberPage/view_family.html', {'x': getdata.id, 'y': getall})
    alldata = Familymember.objects.filter(memberid=id)
    return render(request, 'owner/FamilyMemberPage/owner_tenant_family.html', {'x': getdata.id, 'y': alldata})


def edit_owner(request, id):
    get_data = Familymember.objects.get(id=id)
    if request.method == 'POST':
        get_data.name = request.POST['txtName']
        get_data.age = request.POST['txtAge']
        get_data.cell = request.POST['txtCell']
        get_data.gender = Gender.objects.get(id=request.POST['gender'])
        get_data.relation = Relation.objects.get(relation_type=request.POST['ddlRelation'])
        get_data.memberid = Owner.objects.get(id=request.POST['txtid'])
        get_data.save()
        getall = Familymember.objects.filter(memberid=Owner.objects.get(id=request.POST['txtid']))
        get = Owner.objects.get(id=request.POST['txtid'])
        return render(request, 'owner/FamilyMemberPage/view_family.html', {'x': get.id, 'y': getall})
    return render(request, 'owner/FamilyMemberPage/edit_family_owner.html', {'data': get_data})


def delete_owner(request, id):
    getdata = Familymember.objects.get(id=id)
    getdata.delete()
    # getall = Owner.objects.get(id = current_user)
    if request.user.is_authenticated:
        return redirect("log")


def get_tenant_data(request):
    owner_id = Owner.objects.get(id=request.session['id'])
    data = Owner.objects.filter(
        Q(block=Block.objects.get(block=owner_id.block)) & Q(membertype=MemberType.objects.get(member_type='Tenant')))
    return render(request, 'owner/tenant_details.html', {'getdata': data})


# -----------------------------------------------------------------------
# Adding Regular Visitors
# ------------------------------------------------------------------
def addvisitor_fun(request):
    if request.method == 'POST':
        v1 = RegularVisitor()
        v1.name = request.POST['txtName']
        v1.age = request.POST['txtAge']
        v1.cell = request.POST['txtCell']
        v1.addresss = request.POST['txtAddress']
        v1.gender = Gender.objects.get(id=request.POST['gender'])
        v1.relation = Relation.objects.get(relation_type=request.POST['ddlRelation'])
        v1.memberid = Owner.objects.get(id=request.session['id'])
        v1.save()
        return redirect('visitor')
    else:
        m1 = Relation.objects.all()
        r1 = RegularVisitor.objects.all()
        return render(request, 'owner/visitorPage/addvisitor.html', {'relation': m1, 'visitor': r1})


def updatevisitor_fun(request, id):
    m1 = Relation.objects.all()
    v1 = RegularVisitor.objects.get(id=id)
    if request.method == 'POST':
        v1.name = request.POST['txtName']
        v1.age = request.POST['txtAge']
        v1.cell = request.POST['txtCell']
        v1.addresss = request.POST['txtAddress']
        v1.gender = Gender.objects.get(id=request.POST['gender'])
        v1.relation = Relation.objects.get(relation_type=request.POST['ddlRelation'])
        v1.memberid = Owner.objects.get(id=request.session['id'])
        v1.save()
        return redirect('visitor')
    return render(request, 'owner/visitorPage/updatevisitor.html', {'relation': m1, 'visitor': v1})


def deletevisitor_fun(request, id):
    v1 = RegularVisitor.objects.get(id=id)
    v1.delete()
    return redirect('visitor')


#-----------------------------------
# owner or tenant book amenities and see all the booked amenites
#---------------------------------
def bookAmenities_fun(request):
    if request.method == 'POST':
        b1 = Booking()
        b1.memberid = Owner.objects.get(id=request.session['id'])
        b1.bookedforid = Amenities.objects.get(bookedfor=request.POST['ddlAmenite'])
        b1.ondate = request.POST['txtDate']
        b1.ontimeid = TimingSlot.objects.get(ontime=request.POST['ddlTime'])
        b1.status = 'pending'
        b1.save()
        return redirect('bookAmenities')
    else:
        owner = Owner.objects.get(id=request.session['id'])
        amenite = Amenities.objects.all()
        timeslot = TimingSlot.objects.all()
        return render(request, 'owner/bookamenities.html',
                      {
                          'owner': owner, 'amenite': amenite, 'time': timeslot
                      })



#---------------------------------------
# association manager will see the booked amenities
#---------------------------
def manageamenities_fun(request):
    b2 = Booking.objects.all()
    # owner = Owner.objects.get(id=b2.memberid)
    return render(request, 'association/manageamenitie.html', {'booking': b2})


def upamenite_fun(request, id):
    b1 = Booking.objects.get(id=id)
    b1.memberid = Owner.objects.get(fname=b1.memberid)
    b1.bookedforid = Amenities.objects.get(bookedfor=request.POST['txtBookFor'])

    date = request.POST['txtDate']
    # format = '%y-%m-%d'
    # d = datetime.datetime.strptime(date, format)
    # b1.ondate = d.date()
    b1.ondate = date
    b1.ontimeid = TimingSlot.objects.get(ontime=request.POST['txtTime'])
    b1.status = request.POST['ddlstatus']
    b1.save()
    return redirect('manageamenities')


def see_amenite_fun(request):
    b2 = Booking.objects.filter(memberid=Owner.objects.get(id=request.session['id']))
    return render(request,'owner/seeamenite.html',{'book':b2})