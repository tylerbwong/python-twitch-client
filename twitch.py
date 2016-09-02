import urllib2
import json
import sys
import os


def is_stream_live(channel):
    url = str('https://api.twitch.tv/kraken/streams/' + channel)
    response = urllib2.urlopen(url)
    data = json.load(response)

    return False if data['stream'] == None else True


def get_live_followed(user_name):
    url = str('https://api.twitch.tv/kraken/users/' +
              user_name + '/follows/channels')

    try:
        response = urllib2.urlopen(url)
    except:
        return None

    streams = json.load(response)
    live = []

    for stream in streams['follows']:
        streamer = stream['channel']['name']

        if (is_stream_live(streamer)):
            live.append(streamer)

    return live


def main():
    user_name = raw_input('Enter your username:\n')

    # load streams
    print 'Loading streams...'
    live = get_live_followed(user_name)
    if live == None:
        exit('Could not find user. Exiting.')

    # choose which stream
    print 'Choose which stream to watch:'
    for index in range(len(live)):
        print str(index + 1) + '. ' + live[index]
    option = input()

    # option for quality of stream
    qualities = ['audio', 'mobile', 'low', 'medium', 'high', 'source']
    print 'Choose the quality of the stream:'
    for index in range(len(qualities)):
        print str(index + 1) + '. ' + qualities[index]
    quality = input()

    # run livestreamer with options
    try:
        os.system('livestreamer twitch.tv/' +
                  live[option - 1] + ' ' + qualities[quality - 1])
    except:
        exit('Invalid options. Exiting.')

main()
