from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from django.urls import reverse

from .models import Journey

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .calendar_API import test_calendar



# Create your views here.
def home(request):
    return render(request, 'home.html')

#calendar template
def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'demo.html', context)


def about(request):
    return render(request, 'about.html')

def journey_index(request):
    journeys = Journey.objects.filter(user=request.user)#retriveves all journey exercises
    return render(request, 'journey/index.html',{
        'journeys': journeys
    })

@login_required
def journeys_detail(request, journey_id):
    journey = Journey.objects.get(id=journey_id)
    return render(request, 'journey/detail.html', {'journey':journey})


class JourneyCreate(CreateView):
    model = Journey
    fields = '__all__'
    # success_url = '/journey'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class JourneyUpdate(UpdateView):
    model = Journey
    fields = ['workout_type','description','date']

class JourneyDelete(DeleteView):
    model = Journey
    success_url ='/journeys'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




@login_required
def add_repset(request, journey_id):
    ...

