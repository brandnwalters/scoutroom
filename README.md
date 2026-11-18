This is my project scoutroom. A tool to scout players using AI agents. 

How it works:
The project uses synthetic data in the form of a csv of players and news articles produced for the agents to use.
When the user gives a brief to the system (something like "ball-playing center-back under 23 and under 30 million),
the head scout agent first looks at the players in the csv and returns the top 5 players that fit this brief to the player. 
The data analyst agent then takes those names and, without looking at the head scouts reasoning, looks at the stats of each player to return a top recommendation
to move forward with. Then the recommendation goes to the news analyst, an agent that scans through the synthetic news data trying to find any articles or information
that could affect whether the team wants to buy the player. The recommendation then goes to the sporting director who looks at the budget of the team, 
the players' market value and whether the player is overvalued or undervalued.
Finally, the recommendation goes to the recruitment director, who takes all the reports from the other agents and provides the user with a final recomendation.


What it uses:
It uses the Anthropic API and python libraries. There is currently no front end, it is run using the terminal.

What I'd like to add:
Ideally I would like to further optimize the token usage of each agent and make the project work with real data.
