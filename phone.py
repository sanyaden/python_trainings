#!/usr/bin/env python3
# encoding utf-8

phone_db = (["name","phone"])
print ("Please, enter name and phone:")
def check_contact(cont):
    return True

def enter_contact():
    cont = {}
    name = input("enter name: ")
    cont[name] = input("enter phone: ")
    return cont

def enter_name():
    name = input("enter name: ")
    return name

def create_contact(scontact):
    scontact = enter_contact()
    if check_contact(scontact):
       print ("created contact: ",scontact)#,"phone",cont1[0][0])
    return scontact



def search_contact(sname, scontact):
    sname = enter_name()
    print ("sname=", sname)
    print("contact=", scontact)
    if sname in scontact:
       print ("search OK")
    else:
        print ("search NOK")
    pass

def contact_oper(comm,contact):
    if comm=="c":
        contact=create_contact(contact)
    elif comm=="r":
        name = ""
        search_contact(name, contact)
    return

contact = {}
while True:
    oper = input("Please, enter your operation (c,r,u,d):")
    if oper is not None:
        contact_oper(oper,contact)
