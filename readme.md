## Geeking out on Board Games ##

In this project, I scraped BoardGameGeeks.com, a prominent UGC board game community, to determine what features make the best board games. To access the data, I used a combination of Selenium to create a webdriver and Scrapy to scrape the data loaded from that webdriver, since most of the data was loaded client-side. 

In all, I scraped around 12k top and bottom rated board games for features such as released year, MSRP price, eBay price, game mechanics, theme, game time, complexity score (1-5 based off of user rating), and overall rating (1-10). 

I was able to determine that we're in a Renaissance of board games right now. Not only are 2/3 of the board games produced made from 2000s onwards, over 1/3 of games were made in the last 7 years. I hypothesize that there's greater demand for board games than ever before and the barriers to entry are lower due to crowdfunding services like Kickstarter seeding capital investment for production.  

In addition, 95% of the top quartile of rated games were produced from 2000 onwards, with 70% produced in the last 7 years. While some recency bias may come into play, I hypothesize that better games are being designed due to the historical learnings of older games and as a response to the increased demand. 

I processed the data by converting categorical variables to dummy variables and binning the released year into 5 year intervals for simplicity. In addition, I adjusted the MSRP price for inflation with data pulled in through the Bureau of Labor Statistics. I normalized all of the data and optimized the model through Lasso Regression and cross-validation. 

In the end, I got an R^2 rating of .595 with a MSE of .25 for my regression. It overpredicted the rating for the worst games, likely due to the lower sample size or dearth of information for poor games vs good games (ex. no price since it's not in circulation). 

I was able to determine that complexity, recency, and retail price were the best determinants of a board game rating. Games with mechanics such as Hand management (games that reward players for playing cards in certain sequences or groups ex. poker), Set Collection (players optimize combinations of items, such as three-of-a-kind that yield higher rewards when turned in together ex. Risk), or Line Drawing (players draw lines to connect or isolate objects ex. Snake or Cranium) are correlated with the best rated games. 

Games with too many mechanics or that take too long are rated the worst. 

In short, make a game that leverages a rewarding system for set optimization that people have to connect via lines. Don’t make it too long, but do make it elegantly complex. Charge a lot, and people will love it. 

