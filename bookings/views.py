from .models import courtBooking
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
import datetime

class TennisDetailView(LoginRequiredMixin, DetailView):
    model = courtBooking


class TennisCreateView(LoginRequiredMixin, CreateView):
    model = courtBooking
    fields = ['courtDate', 'courtTime', 'courtLocation', 'courtNumber', 'courtPlay',
              'player1', 'player2', 'player3', 'player4', 'comments']

    def get_form_kwargs(self, **kwargs):
        context = super(TennisCreateView, self).get_form_kwargs()
        context['initial']['courtDate'] = self.kwargs['courtD']
        context['initial']['courtTime'] = self.kwargs['courtT']
        context['initial']['courtNumber'] = self.kwargs['courtN']

        print(context)
        return context

    def form_valid(self, form):
        memberCheck = courtBooking.objects.filter(
            courtDate__range=[datetime.date.today().strftime('%Y-%m-%d'),
                              (datetime.date.today() + datetime.timedelta(days=21)).strftime('%Y-%m-%d')])

        playerDict = dict()
        for iter in memberCheck:
            for player in iter.player1.all():
                if player in playerDict:
                    playerDict[player] += 1
                else:
                    playerDict[player] = 1

            for player in iter.player2.all():
                if player in playerDict:
                    playerDict[player] += 1
                else:
                    playerDict[player] = 1

            for player in iter.player3.all():
                if player in playerDict:
                    playerDict[player] += 1
                else:
                    playerDict[player] = 1

            for player in iter.player4.all():
                if player in playerDict:
                    playerDict[player] += 1
                else:
                    playerDict[player] = 1
        print('PlayerDict' + str(playerDict))
        print('PRE IF-STATEMENTS - ' + str(form.cleaned_data['player1'].all()[0]))

        try:
            counter = 0
            messageList = list()
            try:
                if playerDict[form.cleaned_data['player1'].all()[0]] >= 3:
                    mess1 = messages.warning(self.request,
                                     '{} has the maximum number of court bookings (3)'.format(form.cleaned_data['player1'].all()[0]))
                    messageList.append(mess1)
                    counter += 1
            except:
                print('Player 1 Error')

            try:
                if playerDict[form.cleaned_data['player2'].all()[0]] >= 3:
                    mess2 = messages.warning(self.request,
                                     '{} has the maximum number of court bookings (3)'.format(form.cleaned_data['player2'].all()[0]))
                    messageList.append(mess2)
                    counter += 1
            except:
                print('Player 2 Error')

            try:
                if playerDict[form.cleaned_data['player3'].all()[0]] >= 3:
                    mess3 = messages.warning(self.request,
                                     '{} has the maximum number of court bookings (3)'.format(form.cleaned_data['player3'].all()[0]))
                    messageList.append(mess3)
                    counter += 1
            except:
                print('Player 3 Error')
            try:
                if playerDict[form.cleaned_data['player4'].all()[0]] >= 3:
                    mess4 = messages.warning(self.request,
                                     '{} has the maximum number of court bookings (3)'.format(form.cleaned_data['player4'].all()[0]))
                    messageList.append(mess4)
                    counter += 1
            except:
                print('Player 4 Error')

            print('Counter check - ', counter)
            if counter > 0:
                print('Number of players overbooked -', counter)
                return super(TennisCreateView, self).form_invalid(form)
            else:
                self.object = form.save(commit=False)
                self.object.sport = 'TN'
                self.object.author = self.request.user
                self.object.save()
                form.save_m2m()
                return super(ModelFormMixin, self).form_valid(form)
        except:
            print('Error, skips check')
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

    xTime = list()
    for iter in courtBooking.cTime:
        xTime.append(iter[0])
    bookingDict = list()

    for time in xTime:
        tDict = dict()
        tDict = {
            'courtTime': time,
            'courtDate': searchDate.strftime('%Y-%m-%d')
        }
        bookingDict.append(tDict.copy())

    schedule = courtBooking.objects.filter(courtDate__year=searchDate.year).filter(
        courtDate__month=searchDate.month).filter(courtDate__day=searchDate.day)

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
            print('ERROR: The court time in the models.py does not match any court time in this views cTime variable')

    context = {
        'searchDate': userSearch,
        'bookingDict': bookingDict,
    }

    return render(request, 'bookings/tennisSchedule.html', context)

#TODO: Clarify if current booking system is 3 bookings total or over X period of days?..currently players stopped
#TODO: for courts ahead of 21 day limitation because check only counts within 21 days

#TODO: Make it so each member can only fill one of player1,player2, player3, player4

#TODO: Move overbooking check system to a utils py file

#TODO: ALSO, make warning messages for Singles/Doubles and amount of player1/2/3/4 chosen

#TODO: Display list of bookings in the member profile or a member-specific page

#TODO: Copy the CreateView overbookings checks to updateview

#TODO: Set admin priviliges to override overbookings