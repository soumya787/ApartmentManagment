from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender

class Block(models.Model):
    block = models.CharField(max_length=50)

    def __str__(self):
        return self.block

class MaritalStatus(models.Model):
    marital = models.CharField(max_length=50)

    def __str__(self):
        return self.marital

class MemberType(models.Model):
    member_type = models.CharField(max_length=50)

    def __str__(self):
        return self.member_type

class Relation(models.Model):
    relation_type=models.CharField(max_length=50)

    def __str__(self):
        return self.relation_type

class Designation(models.Model):
    desig_name = models.CharField(max_length=50)

    def __str__(self):
        return self.desig_name

class Complain(models.Model):
    complaintype = models.CharField(max_length=150)

    def __str__(self):
        return self.complaintype

class Owner(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.ForeignKey('Gender',on_delete=CASCADE)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    cell = models.BigIntegerField()
    martial_status = models.ForeignKey('MaritalStatus',on_delete=CASCADE)
    email = models.EmailField(max_length=50)
    occupation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    officeaddress = models.CharField(max_length=200)
    ondate = models.DateTimeField(default=datetime.now)
    block = models.ForeignKey('Block',on_delete=CASCADE)
    flatnum = models.CharField(max_length=50)
    membertype = models.ForeignKey('MemberType',on_delete=CASCADE)

    def __str__(self):
        return self.fname

class Association(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.ForeignKey('Gender',on_delete=CASCADE)
    cell = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    block = models.ForeignKey('Block', on_delete=CASCADE)
    flatnum = models.CharField(max_length=50)
    desig_name = models.ForeignKey('Designation',on_delete=CASCADE)

class Familymember(models.Model):
    name= models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.ForeignKey('Gender', on_delete=CASCADE)
    cell = models.BigIntegerField()
    relation = models.ForeignKey('Relation',on_delete=CASCADE)
    memberid = models.ForeignKey('Owner',on_delete=CASCADE)

class RegularVisitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.ForeignKey('Gender', on_delete=CASCADE)
    cell = models.BigIntegerField()
    relation = models.ForeignKey('Relation', on_delete=CASCADE)
    addresss = models.CharField(max_length=150)
    memberid = models.ForeignKey('Owner', on_delete=CASCADE)

class ComplainRequest(models.Model):
    name = models.CharField(max_length=50)
    blockid = models.ForeignKey('Block',on_delete=CASCADE)
    flatno = models.IntegerField()
    complaintype =models.ForeignKey('Complain',on_delete=CASCADE)
    complaintdesc = models.CharField(max_length=50)
    serviceprovider = models.CharField(max_length=50)

class Visitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.ForeignKey('Gender', on_delete=CASCADE)
    cell = models.BigIntegerField()
    relation = models.ForeignKey('Relation', on_delete=CASCADE)
    addresss = models.CharField(max_length=150)
    datetimein = models.DateTimeField(default=datetime.now)
    datetimeout = models.DateTimeField(default=datetime.now())
    memberid = models.ForeignKey('Owner', on_delete=CASCADE)

class Amenities(models.Model):
    bookedfor = models.CharField(max_length=50)

    def __str__(self):
        return self.bookedfor

class TimingSlot(models.Model):
    ontime = models.CharField(max_length=50)

    def __str__(self):
        return  self.ontime

class Booking(models.Model):
    memberid = models.ForeignKey('Owner', on_delete=CASCADE)
    bookedforid = models.ForeignKey('Amenities',on_delete=CASCADE)
    ondate = models.DateField()
    ontimeid = models.ForeignKey('TimingSlot',on_delete=CASCADE)
    status = models.CharField(max_length=50)
