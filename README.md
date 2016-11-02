# python-twitch-client
[![Build Status](https://travis-ci.org/tylerbwong/python-twitch-client.svg?branch=master)](https://travis-ci.org/tylerbwong/python-twitch-client)

A command line tool for Twitch that uses the Kraken API used with livestreamer.

## Requirements

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [livestreamer](https://github.com/chrippa/livestreamer)
* [Twitch API Client ID](https://blog.twitch.tv/client-id-required-for-kraken-api-calls-afbb8e95f843#.nz4sszgsl)

## Usage

Make sure your client id is in a .txt file in the same directory.

```
python twitch.py <input file>.txt
```

## Example

```
Enter your username:
tylerbwong
Loading streams...
Choose which stream to watch:
1. esl_csgo
2. tarik
3. hiko
2
Choose the quality of the stream:
1. audio
2. mobile
3. low
4. medium
5. high
6. source
6
[cli][info] Found matching plugin twitch for URL twitch.tv/tarik
[cli][info] Available streams: audio, high, low, medium, mobile (worst), source (best)
[cli][info] Opening stream: source (hls)
[cli][info] Starting player: /Applications/VLC.app/Contents/MacOS/VLC
```
