#!/usr/bin/env python2
#coding:utf-8


import os


def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)
    
    