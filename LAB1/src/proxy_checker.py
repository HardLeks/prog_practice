import requests


def check_proxy(url, proxy):
    with requests.Session() as s:
        try:
            s.get(url, proxies={'https': 'https://'+proxy}, timeout=5)
            print('Success connection! prms=', url, proxy)
            s.close()
            return True
        except requests.exceptions.ProxyError:
            print('End with ProxyError prms=', url, proxy)

        except requests.exceptions.ConnectTimeout:
            print('End with ConnectTimeout prms=', url, proxy)

        except ValueError:
            print('End with ValueError prms=', url, proxy)

        s.close()
        return False


def check_proxy_from_file(url_list, file_path):
    result_list = []
    file = open(file_path)

    for url in url_list:
        for proxy in file:
            proxy = proxy[:len(proxy) - 1]

            print('Check ', proxy, ' for ', url)
            result = check_proxy(url, proxy)
            if result:
                result_list.append(proxy)

    file.close()
    return result_list
