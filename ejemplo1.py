# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:08:56 2023

@author: Jesus
"""

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
#import datetime

st.title('Mi primer proyecto')
st.write('Hola **como** estas')


df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
st.dataframe(df.head(15))
st.map(df)