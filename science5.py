import re

class LogEntry:
    LOG_PATTERN = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) .*? '
        r'"(?:GET|POST|PUT|DELETE|HEAD) (?P<url>[^ ]+) .*?" '
        r'\d+ \d+ '
        r'"[^"]*" '
        r'"(?P<user_agent>[^"]+)"'
    )
    def __init__(self, raw_line: str):
        self.raw_line = raw_line
        self._parse()
    def _parse(self):
        match = self.LOG_PATTERN.search(self.raw_line)
        if not match:
            raise ValueError("Lign de log invalid ")
        self._ip = match.group('ip')
        self._url = match.group('url')
        self._user_agent = match.group('user_agent')
    @property
    def ip(self):
        return self._ip
    
    @property
    def url(self):
        return self._url
    
    @property
    def user_agent(self):
        return self._user_agent
        

line = (
    '180.222.224.52 - - [09/05/2019:15:16:31 +0200] '
    '"GET /?CSCZWOWW=VIX HTTP/1.1" 200 4328 '
    '"http://192.168.2.4/MEUKGWMAYT" '
    '"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1)"'
)

entry = LogEntry(line)

print(entry.ip)
print(entry.url)
print(entry.user_agent)
