from django.urls import path

from apartment import views

urlpatterns = [
    path('',views.home,name='home') ,      # redirect to home.html page
    path('aboutus',views.aboutus,name='aboutus'),   # redirect to aboutus.html
    path('contact',views.contact,name='contact'),  # redirect to contact.html

    path('forpswd',views.forpswd,name='forpswd'),   # redirect to forgotpassword.html
    path('cancel',views.cancel_pswd),

    path('log',views.logfunc,name="log"),    # redirect to login.html and read the data and redirect to association_manager_home.html
    path('asocihome',views.ass_home,name='asocihome'),  # redirect to association manager.html page

    path('ownerpage',views.ownerpage,name='ownerpage'),  # redirect to ownerreg.html page
    path('ownerreg',views.ownerreg),    # storing data inside owner table
    path('getowner',views.get_ownerdata,name='getowner'),  # display the owner details
    path('editowner/<int:id>',views.editowner,name='editowner'), # update the data of owner
    path('deleteowner/<int:id>',views.deleteowner,name='deleteowner'), # delete the owner data

    path('associlogout',views.associ_logout,name='associlogout'),  # logout from association manager page
    path('associ_member',views.associmember,name='associmember'),  # get all the association member list
    path('addmem',views.addmem,name='addmem'),  #redirect to add_asssociation.html page
    path('addasoci',views.add_association_mem), # adding member to association
    path('deleteassoci/<int:id>',views.delete_association_mem,name='deleteassoci'),  # deleting association member
    path('updateasssoci/<int:id>',views.update_association_mem,name='updateasssoci'), #updating association member data

    path('owner_Tenant',views.ownerTenant,name='ownerTenant'),  # redirect to owner_home.html
    path('viewfamily/<int:id>',views.view_owner_tenant_family,name='viewfamily'),   # redirect to owner_tenant_family.html
    path('addfamily/<int:id>',views.addownerfamily,name='addfamily'),
    path('edit_owner/<int:id>',views.edit_owner,name='edit_owner'),   # redirect to edit_family_owner page
    path('delete_owner/<int:id>',views.delete_owner,name='delete_owner'),

    path('addvisitor',views.addvisitor_fun,name='visitor'),  # adding visitor
    path('updatevisitor/<int:id>',views.updatevisitor_fun,name='updatevisitor'),  # update the visitor
    path('deletevisitor/<int:id>',views.deletevisitor_fun,name='deletevisitor'), #delete visitor

    path('get_tenant',views.get_tenant_data,name='gettenant'),   # getting tenant details only

    path('bookAmenities',views.bookAmenities_fun,name='bookAmenities'),    # booking amenite
    path('manageamenities',views.manageamenities_fun,name='manageamenities'),  # manger will see amenities
    path('upamenite/<int:id>',views.upamenite_fun,name='upamenite'),  # manager will update the amenite status
    path('seeamenite',views.see_amenite_fun,name='seeamenite') # owner will see all amenitie



]