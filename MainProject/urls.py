from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .api import *
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',getUserData,name='mydata'),
    path('setting/',Setting,name='settings_add_edit'),
    path('get-setting/',getBescData,name='getBescData'),
    path('create/organize/',create_organizers,name='create.organizer'),
    path('get/organize/',get_organizers,name='get.organizers'),
    path('get/organize/<int:id>',get_organizer,name='get.organizer'),
    path('update/organize/<int:id>',update_organizers,name='update.organizer'),
    path('delete/organizer/<int:id>',delete_organizer,name='delete.organizer'),
    #======================================#
    path('create/shepherds/',create_shepherds,name='create.shepherds'),
    path('get/shepherds/',get_shepherds,name='get.shepherds'),
    path('get/shepherd/<int:id>',get_shepherd,name='get.shepherd'),
    path('update/shepherds/<int:id>',update_shepherds,name='update.shepherds'),
    path('delete/shepherds/<int:id>',delete_shepherds,name='delete.shepherds'),
    #======================================#
    path('create/schedule/',create_schedule,name='create.schedule'),
    path('get/schedule/',get_schedule,name='get.schedule'),
    # path('get/shepherd/<int:id>',get_shepherd,name='get.shepherd'),
    # path('update/shepherds/<int:id>',update_shepherds,name='update.shepherds'),
    path('delete/schedule/<int:id>',delete_schedule,name='delete.schedule'),
     #======================================#
    path('create/Speakers/',create_Speakers,name='create.Speakers'),
    path('get/Speakers/',get_Speakers,name='get.Speakers'),
    path('get/shepherd/<int:id>',get_shepherd,name='get.shepherd'),
    path('update/Speakers/<int:id>',update_Speakers,name='update.Speakers'),
    path('delete/Speakers/<int:id>',delete_Speakers,name='delete.Speakers'),
    #======================================#
    path('get-all',all_data,name='all_data')
]
