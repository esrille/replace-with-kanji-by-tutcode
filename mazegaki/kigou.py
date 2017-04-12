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

# 記号やギリシア文字をつかっている語をリストアップします。

import re
import sys

re_kigou = re.compile(r"[〇〻\u0370-\u03FF¬°∃∧◇∨≪∪∩〓△▲▽▼■∀≒◆◇≫※□⇔≡⇒∈⊆⊇⊂⊃○●◎〒∵√]")

re_kana = re.compile(r"[ぁ-んァ-ヶー]")

re_non_regular_yomi = re.compile(r"[^ぁ-んァ-ヶー]")

def is_inflectable(kana):
    return l[0][-1] == "―";

#
# main
#
if __name__ == "__main__":
    for line in sys.stdin:
        l = line.split(" ", 1)
        kana = l[0]
        if re_non_regular_yomi.search(kana):
            continue;
        kanji = l[1].strip(" \n/").split("/")
        for cand in kanji[:]:
            if not re_kigou.search(cand):
                kanji.remove(cand)
                continue
            if re_kana.search(cand):
                kanji.remove(cand)
                continue
        if kanji:
            print(kana, " /", '/'.join(kanji), "/", sep='')
