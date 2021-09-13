import requests


def get_proxy():
    return 0


def check_proxy():
    url = 'http://www.google.com'
    file = open('D:\\Works\\MAG\\PROG\\Python\\prog_practice\\LAB1\\src\\proxy.txt')

    for proxy in file:
        proxy = proxy[:len(proxy)-2]
        print(proxy)
        try:
            requests.get(url, proxies={'http': proxy}, timeout=5)
            print('Success!')
        except requests.exceptions.ProxyError:
            print('End with error: ProxyError')
        except requests.exceptions.ConnectTimeout:
            print('End with error: ConnectTimeout')

    return 0


if __name__ == "__main__":
    check_proxy()
