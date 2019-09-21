import re
def parse(text):
    text = text.split('\n')
    subtitles = []

    count = 0
    for i, line in enumerate(text):
        if is_period(line):
            count += 1
            content = ""
            if i < len(text)-1 and text[i+1] != '\n':
                content = text[i+1]
            subtitles.append(Subtitle(str(count), line.strip(), content.strip()))

    return Srt(subtitles)

def is_period(text):
    time = list(map(lambda s: s.strip(), text.split('-->')))
    if len(time) != 2:
        return False
    else:
        return is_time_format(time[0]) and is_time_format(time[1])

def is_time_format(s):
    r = re.compile('^[0-9]+:[0-9]+:[0-9]+,[0-9]+$')
    if r.match(s) is not None:
        return True
    else:
        return False

class Subtitle:
    def __init__(self, serial, period, content):
        self.serial = serial
        self.period = period
        self.content = content


class Srt:
    """
        subtitle: Subtitle
        path: String
    """
    def __init__(self, subtitles):
        self.subtitles = subtitles

    def write_srt(path):
        pass


if __name__ == '__main__':
    pass
