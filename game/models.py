from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

from . import util


# Create your models here.


class Member(models.Model):
    username = models.CharField('username', max_length=10)
    first_name = models.CharField('first name', max_length=10)
    last_name = models.CharField('last name', max_length=10)
    subs_date = models.DateTimeField('Subscription date', default=timezone.now)
    total_points = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-total_points', 'first_name']

    def __str__(self):
        return self.username


class Tournament(models.Model):
    name = models.CharField('Tournament name', max_length=24, default=util.create_name())
    length_of_tournament = models.PositiveSmallIntegerField('Length of Tournament', blank=True, null=True)
    launch_date = models.DateTimeField('Tournament launch Date', default=timezone.now)
    ended = models.BooleanField('Tournament ended', default=False)
    players = models.ManyToManyField(Member)

    class Meta:
        ordering = ['launch_date']

    def __str__(self):
        return self.name

    def tournament_finished(self):
        self.ended = True
        return self.ended


class TournamentScoreboard(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tournament_score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['tournament', '-tournament_score']


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    week = models.PositiveSmallIntegerField('Match week', default=1)
    play_date = models.DateTimeField('Match date', default=timezone.now)
    weekday = models.CharField('Match day', max_length=10, default=timezone.now().strftime("%A"))
    group = models.CharField('Match Group', max_length=1)
    participants = models.ManyToManyField(Member, through='Scoreboard')

    class Meta:
        ordering = ['play_date', 'group', ]

    def __str__(self):
        return self.group

    def get_page(self):
        num = self.id
        first_num = Match.objects.filter(tournament=Tournament.objects.last()).first().id - 1
        return (num - first_num) // 5

    def get_absolute_url(self):
        return reverse('game:match', kwargs={'page_number': self.get_page()})

    def delete(self, *args, **kwargs):
        for score_obj in self.scoreboard_set.all():
            player = score_obj.member
            point = score_obj.point
            member = Member.objects.get(username=player)
            member.tournament_score -= point
            member.save()
        super().delete(*args, **kwargs)  # Call the "real" save() method.


class Scoreboard(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        match = str(self.match)
        score = str(self.score)
        member = str(self.member)
        return member + ' ' + match + ' ' + score

