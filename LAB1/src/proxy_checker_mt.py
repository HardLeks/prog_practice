from concurrent.futures import ThreadPoolExecutor
import requests


def check_proxy(url, proxy, result, delay=3, debug=False):
    print('Check', proxy, 'for', url)
    with requests.Session() as s:
        try:
            s.get(url, proxies={'http': 'http://'+proxy}, timeout=delay)
            print('\tSuccess connection!')
            s.close()
            result.add(proxy)
        except requests.RequestException as err:
            if debug:
                print('End with ', err)
        except ValueError:
            if debug:
                print('End with ValueError')

        print('\tFail connection! prms=', proxy, url)
        s.close()


def check_proxy_from_file(url_list, file_path, delay=3, debug=False):
    proxy_list = set()
    result_list = set()

    file = open(file_path)
    for line in file:
        proxy_list.add(line[:len(line)-1])
    file.close()

    print('Check', len(proxy_list), 'proxy for', len(url_list), 'urls')
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in url_list:
            for proxy in proxy_list:
                executor.submit(check_proxy, url=url, proxy=proxy, result=result_list)

        return result_list
