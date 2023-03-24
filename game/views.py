from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from .models import Member, Tournament, Match, Scoreboard, TournamentScoreboard
from django.forms import inlineformset_factory
# Create your views here.
from datetime import datetime, timedelta
from django.utils import timezone
from string import ascii_uppercase
from django.contrib.auth.decorators import permission_required
from django.utils.http import urlencode
from django.db.models import Count

from django.shortcuts import get_object_or_404


class HomeView(generic.base.TemplateView):
    template_name = 'game/home.html'

    def get_context_data(self):
        if Tournament.objects.all().count() > 1:
            active_tournament=Tournament.objects.filter(ended=False).first()
        else:
            active_tournament = Tournament.objects.all().first()
        context = super().get_context_data()
        context['latest_tournament'] = active_tournament
        if Tournament.objects.last():
            context['date'] = Tournament.objects.first().launch_date.strftime("%Y-%m-%d")
            active_week = (timezone.now() - active_tournament.launch_date).days // 7
            context['active_week'] = active_week
        return context


class MatchListView(generic.ListView):
    model = Match
    if Tournament.objects.filter(ended=False).filter(launch_date__lte=timezone.now()).first():
        paginate_by = Tournament.objects.filter(ended=False).filter(launch_date__lte=timezone.now()).first().players.all().count()//4
    template_name = 'game/match.html'
    context_object_name = 'ongoing_tournament_match_list'


    def get_queryset(self):
        tour = Tournament.objects.filter(ended=False).filter(launch_date__lte=timezone.now())
        return Match.objects.filter(tournament__in=tour)
'''from django.db.models import Count
result = (Match.objects.filter(tournament__id__in=Tournament.objects.filter(ended=False)).values('tournament')).annotate(dcount=Count('tournament')).order_by()
Tournament.objects.get(id=result[0]["tournament"]).players.count()'''
class DailyMatchScoreView(generic.ListView):
    model = Scoreboard
    template_name = 'game/daily.html'
    context_object_name = 'scoreboard_list'

    def get_queryset(self):
        
        q1 = Match.objects.filter(play_date__year__lte=self.kwargs['year'],
                                  play_date__month__lte=self.kwargs['month'],
                                  play_date__day__lte=self.kwargs['day'])
        if q1:
            q2 = Match.objects.filter(play_date=q1.last().play_date)#.day,play_date__month=q1.last().play_date.month)
            # q2 = q1.play_date
            # q3 = Match.objects.filter(play_date=q2)
            # return Scoreboard.objects.filter(match_id__in=q3)
            return Scoreboard.objects.filter(match_id__in=q2)


class WeeklyMatchScoreView(generic.dates.WeekArchiveView):

    queryset = Match.objects.all()
    template_name = 'game/weekly.html'
    date_field = "play_date"
    week_format = "%W"
    allow_future = True


class MemberListView(generic.ListView):

    model = Member
    template_name = 'game/member.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return Member.objects.all()


class RankingView(generic.ListView):
    model = Member
    template_name = 'game/result.html'

    def get_queryset(self):
        return Member.objects.all()

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournament_list'] = TournamentScoreboard.objects.values('tournament').distinct()
        return context'''


class DetailView(generic.ListView):

    model = Scoreboard
    template_name = 'game/daily.html'
    context_object_name = 'scoreboard_list'

    def get_queryset(self):
        #q1 = Match.objects.get(id=self.kwargs['pk'])
        #q2 = q1.play_date
        #q3 = Match.objects.filter(play_date=q2)
        #return Scoreboard.objects.filter(match_id__in=q3)
        return Scoreboard.objects.filter(match_id=self.kwargs['pk'])



@permission_required('game.add_scoreboard')
def entre_score(request, match_id, page_number):

    match = Match.objects.get(pk=match_id)
    ScoreInlineFormSet = inlineformset_factory(Match, Scoreboard, fields=('member', 'score',), extra=0)
    if request.method == "POST":
        formset = ScoreInlineFormSet(request.POST, instance=match)
        if formset.is_valid():
            iter_num = int(request.POST.get('scoreboard_set-INITIAL_FORMS'))
            for i in range(iter_num):
                key = 'scoreboard_set-'+str(i)+'-member'
                identity = int(request.POST.get(key))
                member = Member.objects.get(id=identity)
                key = 'scoreboard_set-'+str(i)+'-score'
                point = int(request.POST.get(key))
                score = Scoreboard.objects.get(member=member, match=match)
                ts_obj = TournamentScoreboard.objects.get(tournament=match.tournament, member=member)
                if score.score > 0:
                    ts_obj.tournament_score -= score.score
                    ts_obj.save()
                    member.total_points -= score.score
                    member.save()
                ts_obj.tournament_score += point
                ts_obj.save()
                member.total_points += point
                member.save()
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(reverse('game:match') + '?' + urlencode({'page': page_number}))

    else:
        formset = ScoreInlineFormSet(instance=match)
    return render(request, 'game/entry.html', {'formset': formset})


'''def match(request):

    number_of_participants = Member.objects.count()
    number_of_five = number_of_participants % 4
    number_of_elements = number_of_participants // 4
    group_list = [0]
    n = 0
    while len(group_list) <= number_of_elements:
        n += 1
        try:
            c = group_list[-1]
        except:
            c = 0
        if n <= number_of_five:
            group_list.append(c+5)
        else:
            group_list.append(c+4)
        group_names = ascii_uppercase
    for i in range(len(group_list)-1):
        Match.objects.create(group=group_names[i])
        match_instance = Match.objects.all()[i]
        match_instance.participants.set(Member.objects.all()[group_list[i]:group_list[i+1]])'''

