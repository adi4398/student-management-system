from django. urls import path
from .views import(
                    event_list,
                    event_registration,
                    event_create,
                    event_update,
                    event_details,
                )

urlpatterns =  [
path('', event_list, name='event-list'),
path('register/<int:id>/', event_registration, name='event-registration'),
path('create/', event_create, name='event-create'),
path('update/<int:id>/', event_update, name='event-update'),
path('details/<int:id>/', event_details, name='event-details'),
]