#!/usr/bin/python3

abbrs = {
    "lol": "laugh out loud",
    "omg": "oh my gosh",
    "rofl": "rolling on the floor laughing",
    "nn": "neural network; night nigh",
    "roflol": "rolling on the floor laughing out loud",
    "brb": "be right back",
    "bbif": "be back in a few",
    "bbf": "be back in a few",
    "kk": "ok",
    "pls": "please",
    "plz": "please",
    "witw": "what in the world",
    "nvm": "never mind",
    "idk": "i don't know",
    "asap": "as soon as possible",
    "btw": "by the way",
    "gtg": "got to go",
    "pm": "private message",
    "dm": "direct message",
    "jk": "just kidding",
    "np": "no problem",
    "msg": "message",
    "thx": "thanks",
    "ty": "thank you",
    "nty": "no thank you",
    "fyi": "for your information"
}

def abbr(phenny, input):
    '''.abbr <abbreviation> - search for meaning of abbreviation '''
    if len(input.group().split(' ', 1)) < 2:
        phenny.say('usage: .abbr <query>')
        return 0

    text = input.group().split(' ', 1)[1]

    try:
        phenny.say('{} means "{}"'.format(text, abbrs[text]))
    except KeyError as e:
        phenny.say("I'm not sure what {} means.".format(text))

abbr.commands = ['abbr']
abbr.priority = 'medium'
abbr.example = '.abbr lol'
