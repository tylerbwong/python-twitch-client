import urllib2
import fileinput
import json
import sys
import os


def is_stream_live(channel, client_id):
    url = str('https://api.twitch.tv/kraken/streams/' + channel
        + '?client_id=' + client_id)
    response = urllib2.urlopen(url)
    data = json.load(response)

    return False if data['stream'] == None else True


def get_live_followed(user_name, client_id):
    url = str('https://api.twitch.tv/kraken/users/' + user_name
        + '/follows/channels' + '?client_id=' + client_id)

    try:
        response = urllib2.urlopen(url)
    except:
        return None

    streams = json.load(response)
    live = []

    for stream in streams['follows']:
        streamer = stream['channel']['name']

        if (is_stream_live(streamer, client_id)):
            live.append(streamer)

    return live


def main():
    # read client id from file
    try:
        with open(sys.argv[-1], 'r') as clientIdFile:
            client_id = clientIdFile.read().replace('\n', '')
    except:
        exit('Could not read client id. Exiting.')

    user_name = raw_input('Enter your username:\n')

    # load streams
    print 'Loading streams...'
    live = get_live_followed(user_name, client_id)
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
