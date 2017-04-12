#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2017 Esrille Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 常用漢字表内の訓よみの熟語(1文字の漢字をのぞく)をリストアップします。

import itertools
import re
import sys

re_on = re.compile(r"[^ぁ-ん\-]")

def gokan(kana):
    pos = kana.find('-')
    if pos == -1:
        return kana
    return kana[0:pos]

def to_seion(s):
    dakuon = "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽっ"
    seion = "かきくけこさしすせそたちつてとはひふへほはひふへほつ"
    t = ''
    for c in s:
        i = dakuon.find(c)
        if i == -1:
            t += c
        else:
            t += seion[i]
    return t;

dict = {}

def kunyomi(kana, cand):
    global dict
    if len(cand) == 1:
        if not cand in dict:
            return 0
        return 0 # kana in dict[cand]
    c = cand[0];
    if not c in dict:
        return 0;
    s = dict[c];
    for c in cand[1:]:
        if not c in dict:
            return 0;
        t = set(itertools.product(s, dict[c]))
        s = set()
        for y in t:
            s.add(to_seion(''.join(y)))
            if 2 <= len(y[0]) and 0 <= "きく".find(y[0][-1]) and 0 <= "かきくけこ".find(y[1][0]):
                s.add(to_seion(y[0][0:-1] + "つ" + y[1]))
    if to_seion(kana) in s:
        return 1
    return 0

#
# main
#
if __name__ == "__main__":
    regular = open("zyouyou-kanji.csv", 'r')
    for line in regular:
        l = line.strip(" \n/").split(",")
        kanji = l[0]
        l.remove(kanji)
        s = set()
        for cand in l[:]:
            cand = cand.strip("（）")
            if re_on.search(cand):
                continue
            s.add(gokan(cand))
        if s:
            dict[kanji] = s
    for line in sys.stdin:
        if line[0] == ';':
            continue;
        l = line.split(" ", 1)
        kana = l[0]
        kanji = l[1].strip(" \n/").split("/")
        for cand in kanji[:]:
            if kunyomi(kana, cand):
                print(kana, " /", cand, "/", sep='')
