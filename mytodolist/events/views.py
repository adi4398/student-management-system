from django. shortcuts import redirect, render
from .models import Event, Registration

# Create your views here.

def event_list(request) :
    events = Event.objects.all()
    return render(request, 'events/all-events.html', {'events' : events} )

def event_registration(request, id):
    event = Event.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        registraion = Registration(event = event, name=name, email=email, phone=phone)
        registraion.save()
        
        return redirect('event-details',event.id)
    return render(request, 'events/event-registration.html',{'event':event})

def event_update(request, id):
    return render(request, 'events/update-events.html')

def event_details(request, id):
    event = Event.objects.get(id=id)
    registrations = Registration.objects.filter(event = event)
    return render(request, 'events/view-details.html',{'event':event, 'registrations':registrations})

def event_create(request):
    if request.method == 'POST':
        event_title = request.POST.get('event-title')
        event_description = request.POST.get('event-description')
        event_start_date = request.POST.get('start-date')
        event_end_date = request.POST.get('end-date')
        event_poster = request.FILES.get('event-poster')
        event_brochure = request.FILES.get('event-brochure')

        event = Event(
            title=event_title,
            description=event_description,
            start_date=event_start_date,
            end_date=event_end_date,
            poster=event_poster,
            brochure=event_brochure
        )
        event.save()
        return redirect('event-list')

    return render(request, 'events/new-event.html')
