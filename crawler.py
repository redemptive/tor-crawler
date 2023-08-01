#!/usr/bin/env python3
import argparse
import requests

def request(url, args):
    retries = 0
    while retries <= args.retries:
        res = session.get(url, timeout=60)

        if res.status_code != 504:
            break
        elif args.verbose:
            print(f"Call to {url} failed with {res.status_code}. Retrying...")

        retries += 1
    return res


parser = argparse.ArgumentParser(description="This is Darkweb Crawler")

parser.add_argument("-r", "--retries", type=int, default=5 ,help="How many retries if a request fails")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

session = requests.session()
session.proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

res = request('http://httpbin.org/ip', args)

print(res)
print(res.text)
print(res.status_code)

res = request('http://facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion', args)

print(res)
print(res.text)
print(res.status_code)