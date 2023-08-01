#!/usr/bin/env python3
""" This file is for blah blah blah """
import argparse
from tokenize import String
import requests

def request(url, options):
    """ This file is for blah blah blah """
    retries = 0
    while retries <= options.retries:
        res = session.get(url, timeout=60)

        if res.status_code != 504:
            break

        if options.verbose and res.status_code != 504:
            print(f"Call to {url} failed with {res.status_code}. Retrying...")

        retries += 1
    return res


parser = argparse.ArgumentParser(description="This is Darkweb Crawler")

parser.add_argument("-p", "--proxy", type=str, default="socks5h://localhost:9050" ,help="Proxy running tor")
parser.add_argument("-r", "--retries", type=int, default=5 ,help="Retries if a request fails")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

session = requests.session()
session.proxies = {
    'http': args.proxy,
    'https': args.proxy
}

out = request('http://httpbin.org/ip', args)

print(out)
print(out.text)
print(out.status_code)

out = request('http://facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion', args)

print(out)
print(out.text)
print(out.status_code)
