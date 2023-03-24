import datetime
from itertools import permutations
from random import choice

from django.contrib import admin
from .models import Member, Tournament, Match, Scoreboard, TournamentScoreboard
from string import ascii_uppercase
from django.utils import timezone
import datetime
from .util import create_random_groups, create_group_list
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'first_name', 'last_name', 'subs_date']}),
        ]

    list_display = ('username', 'first_name', 'last_name', 'subs_date',)
    list_filter = ['subs_date']
    search_fields = ['username']


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'length_of_tournament', 'launch_date', 'ended', 'players',]}),
        ]

    list_display = ('name', 'length_of_tournament', 'launch_date', 'ended', )
    list_filter = ['ended']
    search_fields = ['launch_date']
    filter_horizontal = ['players']

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)
        form.save_m2m()
        if not obj.ended:
            group_names = ascii_uppercase
            number_of_participants = obj.players.all().count()
            group_list = create_group_list(number_of_participants)
            for week in range(obj.length_of_tournament):
                for day in range(5):
                    match_group_index_list = create_random_groups(group_list, number_of_participants)
                    for i in range(len(group_list) - 1):
                        Match.objects.create(tournament=obj, group=group_names[i], week=week+1, play_date=obj.launch_date+datetime.timedelta(days=week*7+day), weekday=(obj.launch_date+datetime.timedelta(days=week*7+day)).strftime("%A"))
                        match_instance = Match.objects.all().last()
                        for ind in match_group_index_list[i]:
                            Scoreboard.objects.create(member=obj.players.all()[ind], match=match_instance, score=0)
            for member in Member.objects.all():
                TournamentScoreboard.objects.create(tournament=obj, member=member)

            #uncomment this part to generate scores
            '''for match in Match.objects.filter(tournament=obj):
                score_list = choice(list(permutations(list(range(2, 6)), 4)))
                i = 0
                for player in match.participants.all():
                    if i < 4:
                        score = score_list[i]
                    else:
                        score = 1
                    ts_obj = TournamentScoreboard.objects.get(tournament=obj, member=player)
                    ts_obj.tournament_score += score
                    ts_obj.save()
                    sb_instance = Scoreboard.objects.get(match=match, member=player)
                    sb_instance.score = score
                    sb_instance.save()
                    player.total_points += score
                    player.save()

                    i += 1'''

    def delete_model(self, request, obj):
        tournamentscoreboards = TournamentScoreboard.objects.filter(tournament=obj)
        for tournamentscoreboard in tournamentscoreboards:
            member = Member.objects.get(username=tournamentscoreboard.member)
            point = tournamentscoreboard.tournament_score
            member.total_points -= point
            member.save()
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            tournamentscoreboards = TournamentScoreboard.objects.filter(tournament=obj)
            for tournamentscoreboard in tournamentscoreboards:
                #member = Member.objects.get(username=tournamentscoreboard.member)
                member = tournamentscoreboard.member
                point = tournamentscoreboard.tournament_score
                member.total_points -= point
                member.save()
        for obj in queryset:
            obj.delete()


class MatchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tournament', 'week', 'play_date', 'weekday', 'group']}),
        ]

    list_display = ('tournament', 'week', 'play_date', 'weekday', 'group')
    list_filter = ['week']
    search_fields = ['group']


class ScoreboardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['member', 'match', 'score']}),
        ]

    list_display = ('member', 'match', 'score')
    list_filter = ['match']
    search_fields = ['member']


admin.site.register(Member, MemberAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Scoreboard, ScoreboardAdmin)


