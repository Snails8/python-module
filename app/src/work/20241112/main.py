import os
from dataclasses import dataclass

"""
要件:
1. レスポンスタイム(ms)が1000ms以上のリクエストを抽出
2. ステータスコード別のリクエスト数をカウント
3. 最もアクセスの多いIPアドレスを特定
4. /api/で始まるエンドポイントへのリクエストのみを抽出
"""


# 2024-01-01 00:01:23 192.168.1.100 GET /index.html 200 1500ms
# 2024-01-01 00:01:23 / 192.168.1.100 / GET / index.html /200/ 1500ms


@dataclass
class Log:
    datetime: str
    ip: str
    method: str
    path: str
    status: int
    response_time: int


def parse_log(dir_path: str) -> list[Log]:
    with open(dir_path) as f:
        log_list = []
        for line in f:
            s = line.split(" ")
            log = Log(
                datetime=s[0] + " " + s[1],
                ip=s[2],
                method=s[3],
                path=s[4],
                status=int(s[5]),
                response_time=int(s[6].replace("ms", "")),
            )
            log_list.append(log)
        return log_list

class LogAnalyzer:
    def __init__(self, log_list: list[Log]):
      self.log_list = log_list
    
    def get_slow_response(self) -> list[Log]:
      return [log for log in self.log_list if log.response_time >= 1000]

    def count_status_code(self) -> dict[int, int]:
      status_code_count = {}
      for log in self.log_list:
        if log.status in status_code_count:
          status_code_count[log.status] += 1
        else:
          status_code_count[log.status] = 1
      return status_code_count
    
    def get_most_access_ip(self) -> str:
      ip_count = {}
      for log in self.log_list:
        if log.ip in ip_count:
          ip_count[log.ip] += 1
        else:
          ip_count[log.ip] = 1
      ip_count_sorted = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
      return ip_count_sorted[0]
    
    def get_api_request(self) -> list[Log]:
      return [log for log in self.log_list if log.path.startswith("/api/")]

def main():
    dir_path = os.path.dirname(p=os.path.abspath(__file__)) + "/access.log"
    log_list = parse_log(dir_path)
    print(log_list)
    
    analyzer = LogAnalyzer(log_list)
    result_1 = analyzer.get_slow_response()
    result_2 = analyzer.count_status_code()
    result_3 = analyzer.get_most_access_ip()
    result_4 = analyzer.get_api_request()
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)

if __name__ == "__main__":
    main()
