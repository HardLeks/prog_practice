import unittest
import time

from LAB1.src.proxy_checker import check_proxy_from_file


# @unittest.skip
class TestProxyChecker(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def test(self):
        site_list = [
            'http://omgtu.ru/',
            'http://www.google.com/',
            'http://www.yandex.com/',
            'http://www.vk.com/'
        ]

        proxy_path = 'D:\\Works\\MAG\\PROG\\Python\\prog_practice\\LAB1\\tests\\proxy.txt'

        self.res = check_proxy_from_file(site_list, proxy_path, 1)
        self.assertEqual(len(self.res), len(self.res))

    def tearDown(self):
        duration = time.time() - self.start_time
        print(f"{self.id}: End with {len(self.res)} proxy in {duration} seconds")

