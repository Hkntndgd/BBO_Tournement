from django.urls import path, re_path
from . import views
from datetime import datetime

today = datetime.today()

app_name = 'game'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'^match/(?:page=(?P<page_number>[0-9]+)/)?$', views.MatchListView.as_view(), name='match'),
    path('daily/<int:year>/<int:month>/<int:day>', views.DailyMatchScoreView.as_view(), name='daily'),
    path('<int:year>/week/<int:week>/', views.WeeklyMatchScoreView.as_view(), name='weekly'),
    path('member', views.MemberListView.as_view(), name='member'),
    path('ranking', views.RankingView.as_view(), name='ranking'),
    path('entry/<int:match_id>/<int:page_number>', views.entre_score, name='entry'),
    path('daily_all', views.DetailView.as_view(), name='daily_all'),
]
