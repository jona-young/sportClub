from .models import courtBooking
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import ModelFormMixin


class TennisListView(LoginRequiredMixin, ListView):
    model = courtBooking
    template_name = 'bookings/tennis.html'
    context_object_name = 'bookings'
    ordering = ['-courtDate', 'courtTime']

class TennisDetailView(LoginRequiredMixin, DetailView):
    model = courtBooking

class TennisCreateView(LoginRequiredMixin, CreateView):
    model = courtBooking
    fields = ['courtDate', 'courtTime', 'courtLocation', 'courtNumber', 'courtPlay', 'player1', 'player2',
          'player3', 'player4', 'comments']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sport = 'TN'
        self.object.author = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class TennisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = courtBooking
    fields = ['courtDate', 'courtTime', 'courtLocation', 'courtNumber', 'courtPlay', 'player1', 'player2',
          'player3', 'player4', 'comments']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sport = 'TN'
        self.object.author = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.author:
            return True
        return False

class TennisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = courtBooking
    success_url = '/bookings/tennis/'

    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.author:
            return True
        return False

#TODO:
'''

For each sport booking page, the 'context' passed to the views template will have to pull from the court
booking database through filter of a form field for the specific sport

Tennis
Squash
Badminton & Pickleball
Platform Tennis
Table Tennis
Golf Simulator

'''

