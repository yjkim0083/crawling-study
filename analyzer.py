# -*- coding: utf8 -*-

import pandas as pd

data = pd.read_csv('./ddanzi.tsv', encoding='utf-8', sep='\t\t', header=None, engine='python')
print(data[2])