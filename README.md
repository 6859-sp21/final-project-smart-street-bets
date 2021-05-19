# final-project-starter-code

## Project title
Smart Street Bets

## Team member
* Eric Hong
* Veerapatr Yotamornsunthorn (Vic)

## Overview of development process

The work is split equally. Here are the lists of tasks that each member contributed to:

Eric: Data formatting, Graph Implementation, Functionalities on graph

Vic: Scrape articles and reddit posts, Calendar Implementation, Articles Implementation, Tooltip 

Work was mostly done independently through pushing code to either the main branch or a side branch and merged via a pull request. We had meetings at least twice a week to 1) catch up and update each other on one another’s progress and 2) see if either one of us were having difficulty with a certain feature or had a bug they could not solve quickly. If this was the case, we both spent time looking at the code base to see if either one of us could spot the bug/figure out how to implement the feature together.

## Warning

Please use Google Chrome to access the website: <https://6859-sp21.github.io/final-project-smart-street-bets/visualization.html>.

## Abstract

The purpose of the visualization is to aid people when attempting to trade Bitcoin by giving them access to both quantitative insight to previous historic trades and sentimental analysis for any day within a given range of dates by being able to read and analyze social media posts and threads from Reddit and news articles from various media outlets. Having access to both allows people to be more flexible and thorough with planning and following through with their personalized trading strategy. Although just because something has happened in the past and that does not mean does not mean people cannot gain insight from studying the past and looking for key catalysts from multiple angles for why major events occurred.

## Summary image
[chart]: https://github.com/6859-sp21/final-project-smart-street-bets/blob/main/chart.png
[articles]: https://github.com/6859-sp21/final-project-smart-street-bets/blob/main/articles.png
[calendar]: https://github.com/6859-sp21/final-project-smart-street-bets/blob/main/calendar.png

![alt text][calendar]

The users have to pick the date and time on the calendar once they access the website.

![alt text][articles]
After a user pick a date and time on the calendar, the articles of the day before up to the selected date and time will be loaded. For example, if the user pick 16:00 01/01/2021 on the calendar, articles on 12/31/2020 and articles on 01/01/2021 before 16:00 will be loaded and shown to the user. The users could click the left and right arrow to change pages. They can also click the arrows at the top right corner to switch back and forth between articles and reddit posts.

![alt text][chart]
Also, the chart will be updated once the user selects date and time. There are two buttons on top-left corner. The 1D mode will show 15-minute data in the span of 12 hours, and the 3M mode will show one-day data in the span of 3 months. 

## Paper link

## Video link

## Instructions

* Select the date and time on the calendar. After that you will see the data on the graph, and articles about bitcoin on that day and the day before.

* You could hover your mouse over a candlestick, and you will see the date and prices (open, close, low, high) of that data point.

* You could change the mode, which is the period between data points. There are two modes: every 15 minutes (1D), and every day (3M).

* If you are in the 1D mode, the new data point will come in as 15 minutes pass.



