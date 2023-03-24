# BBO_Tournement
The project is a web application to create bridge tournements and to follow up the scores of these tournaments 


OBJECTIVE:
The main objective of this app is to follow-up bridge tournaments.

HOW IT WORKS:
I arbitrarily choose django admin site for staff interface.
At the very beginning a very simple page is displayed with an information saying that No Tournament Launched Yet.

First the admin has to create members. Members are fellows who have registered to BBO app. Fields to be documented
are: First name, Last name, Username(username of BBO app)

Next step is to create a Tournament with tournament name, tournament duration, kick off date, hour and participants.

Ones these steps are accomplished, it will randomly create a match per day per player and its associated scoreboard,
player tournament scoreboard. Home Page will display information about the tournament and 6 navigation bars:
    Home
    Match List
    Daily Scoreboard
    Weekly Scoreboard
    Members
    Ranking

If someone sign up via admin page, matches on Match List has an anchor element with a link of Scoarboard formset.
The admin has to enter match scores via this link.

At the end of each tournament the admin has to enter ended on admin page of tournament.
