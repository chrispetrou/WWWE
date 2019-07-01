#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = 'Christophoros Petrou (game0ver)'
__description__ = "wwwe.py: What's Wrong With my Email?"

import os
import re
import sys
import time
import warnings
import requests
from selenium import webdriver
warnings.filterwarnings("ignore")
from urllib.parse import quote_plus
from colorama import Fore,Back,Style
from argparse import ArgumentParser, ArgumentTypeError, RawTextHelpFormatter
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

B, RA, FR, IT = Style.BRIGHT, Style.RESET_ALL, Fore.RESET, '\033[3m'
G, RD, C, R, BR  = Fore.GREEN, Fore.RED, Fore.CYAN, Back.RED, Back.RESET


def console():
    parser = ArgumentParser(description="{}WWWE.py:{} What's Wrong With my Email.".format(B+G, RA),formatter_class=RawTextHelpFormatter)    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', "--email", 
                        help='Specify an email to check.', metavar='')
    group.add_argument('-f', "--file", type=ValidateFile, 
                        help='Specify a file that contains a list of emails.', metavar='')
    args = parser.parse_args()
    return args


def ret(t):
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    time.sleep(t)


def is_valid(email):
    email_ptrn = re.compile(r'[^@\s]+@[^@\s]+\.[^@\s]+')
    return True if email_ptrn.match(email) else False


def ValidateFile(file):
    if not os.path.isfile(file):
        raise ArgumentTypeError('{}[x] File does not exist{}'.format(RD,RA))
    if os.access(file, os.R_OK):
        return file
    else:
        raise ArgumentTypeError('{}[x] File is not readable{}'.format(RD,RA))


def urlencode(cmd):
    try:
        return quote_plus(cmd)
    except Exception as error:
        print('{}[x] Error:{} "{}"'.format(RD, RA, error))


def inoitsu(email):
    endpoint = 'https://www.hotsheet.com/inoitsu/'
    try:
        with requests.Session() as s:
            creds = {
                'act' : email,
                'accounthide' : 'test',
                'submit' : 'Submit'}
            r = s.post(endpoint, data=creds)
            return True if 'BREACH DETECTED!' in r.text else False
    except Exception as error:
        raise(error)


def HIBP(email):
    endpoint = 'https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(urlencode(email))
    try:
        with requests.Session() as s:
            r = s.get(endpoint)
            return True if r.status_code != 404 else False
    except Exception as error:
        raise(error)


def HIBS(email):
    endpoint = 'https://haveibeensold.app'
    try:
        os.environ['MOZ_HEADLESS'] = '1'
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        with webdriver.Firefox(capabilities=cap) as d:
            d.get(endpoint)
            elem = d.find_element_by_name("email")
            elem.send_keys(email)
            d.find_element_by_id('check').click()
            time.sleep(1)
            try:
                return False if 'Your email is not on any sold list' in d.find_element_by_id('success').text else True
            except:
                return True
    except Exception, error:
        raise(error)


def leakedsource(email):
    endpoint = 'https://leakedsource.ru/'
    try:
        with requests.Session() as s:
            creds = {
                'search' : email,
                'searchType' : '3',
                'wildcard' : 'true',
                'submit' : 'Search'}
            r = s.post(endpoint, data=creds)
            return False if 'No results found' in r.text else True
    except Exception as error:
        raise(error)


def hackcheck(email):
    found = False
    endpoint = 'https://www.avast.com/hackcheck/friends-check/' # doesn't mail us back...
    os.environ['MOZ_HEADLESS'] = '1'
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True
    try:
        with webdriver.Firefox(capabilities=cap) as d:
            d.get(endpoint)
            elem = d.find_element_by_xpath('//input[@type="email"]')
            elem.send_keys(email)
            elem.submit()
            time.sleep(1)
            return d.find_elements_by_tag_name('img')[3].get_attribute('alt') != 'Ok icon'
    except Exception as error:
        raise(error)


def dehashed(email):
    found = False
    endpoint = 'https://www.dehashed.com/search?query={}'.format(urlencode(email))
    try:
        with webdriver.PhantomJS() as d:
            d.get(endpoint)
            h5_tags = d.find_elements_by_tag_name('h5')
            for h5 in h5_tags:
                if email in h5.get_attribute('textContent'):
                    found = True
            return True if found else False
    except Exception as error:
        raise(error)


def check(email):
    results = {}
    try:
        print('{0}[*]{1} Check {2} using {0}haveibeenpwned.com{1} online service'.format(C, RA, email))
        pwned = HIBP(email)
        ret(.1)
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}haveibeenpwned.com{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['HIBP'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}haveibeenpwned.com{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['HIBP'] = "safe"

        print('{0}[*]{1} Check {2} using {0}inoitsu.com{1} online service'.format(C, RA, email))
        pwned = inoitsu(email)
        ret(.1)
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}inoitsu.com{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['inoitsu'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}inoitsu.com{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['inoitsu'] = "safe"

        print('{0}[*]{1} Check {2} using {0}leakedsource.ru{1} online service'.format(C, RA, email))
        pwned = leakedsource(email)
        ret(.1)
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}leakedsource.ru{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['leakedsource'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}leakedsource.ru{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['leakedsource'] = "safe"

        print('{0}[*]{1} Check {2} using {0}avast-hackcheck{1} online service'.format(C, RA, email))
        pwned = hackcheck(email)
        ret(.1) 
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}avast-hackcheck{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['hackcheck'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}avast-hackcheck{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['hackcheck'] = "safe"

        print('{0}[*]{1} Check {2} using {0}dehashed.com{1} online service'.format(C, RA, email))
        pwned = dehashed(email)
        ret(.1)
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}dehashed.com{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['dehashed'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}dehashed.com{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['dehashed'] = "safe"

        print('{0}[*]{1} Check {2} using {0}haveibeensold.app{1} online service'.format(C, RA, email))
        pwned = HIBS(email)
        ret(.1)
        if pwned:
            print('{0}[x]{2} Unfortunately according to {1}haveibeensold.app{2} {0}{3}{2} has leaked.'.format(RD, IT, RA, email))
            results['HIBS'] = "leaked"
        else:
            print('{0}[+]{2} Congrats! According to {1}haveibeensold.app{2} {0}{3}{2} hasn\'t appeared in any breach!'.format(G, IT, RA, email))
            results['HIBS'] = "safe"

    except KeyboardInterrupt:
        sys.exit(0)



if __name__ == '__main__':
    args = console()
    if args.email and is_valid(args.email):
        print('\n{0}[!]{2} Checking {1}{3}{2}:'.format(B, IT, RA, args.email))
        check(args.email)
    else:
        with open(args.file) as f:
            valid_emails = [x for x in f.read().splitlines() if is_valid(x)]
            for email in valid_emails:
                print('\n{0}[!]{2} Checking {1}{3}{2}:'.format(B, IT, RA, email))
                check(email)
#_EOF