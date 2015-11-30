#! /usr/bin/env python
# coding:utf-8

#############################################################################################
## bridge.py
## kovlive bridge for ATOK
## Copyright (c) 2014 mohemohe
##
## this code licensed under the WTFPL .
## please visit ' https://github.com/mohemohe/kovlive-bridge-for-ATOK/blob/master/LICENSE '.
#############################################################################################


import io
import os
import platform
import subprocess
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))


def atok_plugin_run_process(request_data):
    result_data = {} 
    candidate_array = []
    
    kv_JP = kovlive(request_data['composition_string'])
    candidate_array.append( {'hyoki' : kv_JP} )
    result_data['candidate'] = candidate_array
    
    return result_data


def kovlive(ja_JP):
    python_path = 'python3'
    kovlive_path = os.path.join(BASEDIR, './kovlive/kovlive.py')
    os_name = platform.system()
    
    p = subprocess.Popen([python_path, kovlive_path], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    if(os_name == 'Windows'):
        p.stdin.write(ja_JP.encode('cp932'))
    else:
        # 自信ない
        p.stdin.write(ja_JP.encode('utf-8'))
    kv_JP = p.communicate()[0]
    
    if(os_name == 'Windows'):
        kv_JP = kv_JP.decode('cp932')
    else:
        # 自信ない
        kv_JP = kv_JP.decode('utf-8')
    return kv_JP.strip()
