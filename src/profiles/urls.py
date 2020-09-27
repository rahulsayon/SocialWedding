
from django.contrib import admin
from django.urls import path
from .views import ( get_my_profile,invites_received_view,my_profile_view,
                 ProfileListView ,accept_invatation ,reject_invatation,invite_profiles_list_view
                ,ProfileDetailView,send_invatation,remove_from_friendss  )

app_name = 'profiles'

urlpatterns = [
    path('my-invites/acctept/', accept_invatation, name='accept-invite'),
    path('remove-friend/', remove_from_friendss, name='remove-friend'),
    path('send-invite/', send_invatation, name='send-invite'),
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),


]
