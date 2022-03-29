#!/bin/env python3

import configparser

def parseConfig(iniFile, section):
    config = configparser.ConfigParser()
    config.read(iniFile)
    if section == 'WRITE':
        sectionItems = dict(config.items('Master'))
    elif section == 'READ':
        sectionItems = dict(config.items('Master'))
        sectionItems.update(dict(config.items('Slaves')))
    else:
        return None            
    return sectionItems

def parseRequest(request):
    print("Parsing -----------")
    print(request)