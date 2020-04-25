#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, re
from core.colors import colors
from lib.TwitterAPI import Twitter


def getTweetEmailsFromHashtag(query,limit,year,since,until):
    results = []
    tweets = Twitter.getTweets(hashtags=True,limit=limit,search=query,year=year,until=until,since=since)
    results = getEmailsFromTweets(tweets)
    return results

def getUserTweetsWithEmails(username,limit,year,since,until):
    results = []
    tweets = Twitter.getTweets(username=username,limit=limit,year=year,since=since,until=until)
    results = getEmailsFromTweets(tweets)
    return results




def getEmailsFromTweets(tweets):
    results = []

    for tweet in tweets:
        user = tweet.get("username")
        userID = str(tweet.get("user_id"))
        email = findEmail(tweet.get("tweet").split(" "))
        if email:
            results.append(json.dumps({"user":user,"userID":userID,"email":email}))
            print(colors.good + " Username: " + colors.W + user + colors.B + " UserID: " + colors.W + userID + colors.B + " Email: " + colors.W + email + colors.end)

    return results

def findEmail(tweet):
    for word in tweet:
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',word):
            return word