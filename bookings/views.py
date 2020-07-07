from .models import courtBooking
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
import datetime


class TennisListView(LoginRequiredMixin, ListView):
    model = courtBooking
    template_name = 'bookings/tennis.html'
    context_object_name = 'bookings'
    ordering = ['-courtDate', 'courtTime']


class TennisDetailView(LoginRequiredMixin, DetailView):
    model = courtBooking


class TennisCreateView(LoginRequiredMixin, CreateView):
    model = courtBooking
    fields = ['courtDate', 'courtTime', 'courtLocation', 'courtNumber', 'courtPlay',
              'player1', 'player2', 'player3', 'player4', 'comments']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sport = 'TN'
        self.object.author = self.request.user
        self.object.save()
        form.save_m2m()
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
        form.save_m2m()
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


@login_required
def tennisScheduleView(request):
    userSearch = request.GET.get('searchDate', datetime.date.today())

    if isinstance(userSearch, str) is True:
        searchDate = datetime.datetime.strptime(userSearch, '%B %d, %Y').date()
    else:
        searchDate = datetime.date.today()

    cTime = [
        ('5:40 AM'),
        ('6:00 AM'),
        ('6:20 AM'),
        ('7:00 AM'),
        ('7:40 AM'),
        ('8:00 AM'),
        ('8:20 AM'),
        ('9:00 AM'),
        ('9:40 AM'),
        ('10:00 AM'),
        ('10:20 AM'),
        ('11:00 AM'),
        ('11:40 AM'),
        ('12:00 PM'),
        ('12:15 PM'),
        ('12:20 PM'),
        ('1:00 PM'),
        ('1:15 PM'),
        ('1:40 PM'),
        ('2:00 PM'),
        ('2:15 PM'),
        ('2:20 PM'),
        ('3:00 PM'),
        ('3:30 PM'),
        ('3:40 PM'),
        ('4:00 PM'),
        ('4:20 PM'),
        ('4:30 PM'),
        ('5:00 PM'),
        ('5:30 PM'),
        ('5:40 PM'),
        ('6:00 PM'),
        ('6:20 PM'),
        ('6:30 PM'),
        ('7:00 PM'),
        ('7:30 PM'),
        ('7:40 PM'),
        ('8:00 PM'),
        ('8:20 PM'),
        ('8:30 PM'),
        ('9:00 PM'),
        ('9:30 PM'),
        ('9:40 PM'),
    ]
    bookingDict = list()

    for time in cTime:
        tDict = dict()
        tDict = {
            'courtTime': time,
        }
        bookingDict.append(tDict.copy())

    schedule = courtBooking.objects.filter(courtDate__year=searchDate.year).filter(courtDate__month=searchDate.month).filter(courtDate__day=searchDate.day)

    for sc in schedule:
        #find index if a court time is already added to the booking list
        timeVal = None
        for i, bookingIter in enumerate(bookingDict):
            for k,v in bookingIter.items():
                if sc.courtTime in str(v):
                    timeVal = i
                else:
                    continue

        #if the time is already in the booking list, update new court
        if timeVal is not None:
            dictVal = dict()
            dictVal = {
                ('id' + sc.courtNumber): sc.id,
                ('court' + sc.courtNumber): [sc.player1.all, sc.player2.all, sc.player3.all, sc.player4.all]
            }
            bookingDict[timeVal].update(dictVal)
        elif timeVal is None:
            bDict = dict()
            bDict = {
                ('id' + sc.courtNumber): sc.id,
                'courtTime': sc.courtTime,
                ('court' + sc.courtNumber): [sc.player1.all, sc.player2.all, sc.player3.all, sc.player4.all]
            }
            bookingDict.append(bDict.copy())

    context = {
        'searchDate': userSearch,
        'bookingDict': bookingDict,
    }

    return render(request, 'bookings/tennisSchedule.html', context)

#TODO: Add PK values that allow you to link to the anchor tag and click on the booking and be redirected to the update/delete page
#TODO: Currently it is not allowed to be a primary key...I think it is a string where I have specified the in the models as a string but in the urls as a <int:pk>

#TODO: Set limitations as to players can only play on 1 court at once, x amounts per day, x amounts per week, etc

