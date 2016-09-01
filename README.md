# python-twitch-client
A command line tool used with livestreamer.

## Requirements

* Python 2.7
* livestreamer [install](https://github.com/chrippa/livestreamer)

## Usage

```
python twitch.py
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
