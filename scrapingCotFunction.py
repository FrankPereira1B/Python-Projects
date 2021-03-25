#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


def scraping (data):
    
    #Selecting the data
    
    str1 = data.loc[136]
    str2 = data.loc[140]
    str3 = data.loc[142]
    str4 = data.loc[152]
    str5 = data.loc[156]
    str6 = data.loc[158]
    str7 = data.loc[168]
    str8 = data.loc[172]
    str9 = data.loc[174]
    str10 = data.loc[184]
    str11 = data.loc[188]
    str12 = data.loc[190]
    str13 = data.loc[200]
    str14 = data.loc[204]
    str15 = data.loc[206]
    str16 = data.loc[216]
    str17 = data.loc[220]
    str18 = data.loc[222]
    str19 = data.loc[232]
    str20 = data.loc[236]
    str21 = data.loc[238]
    str22 = data.loc[248]
    str23 = data.loc[252]
    str24 = data.loc[254]
    str25 = data.loc[264]
    str26 = data.loc[268]
    str27 = data.loc[270]
    str28 = data.loc[280]
    str29 = data.loc[284]
    str30 = data.loc[286]
    str31 = data.loc[296]
    str32 = data.loc[300]
    str33 = data.loc[302]
    str34 = data.loc[312]
    str35 = data.loc[316]
    str36 = data.loc[318]
    str37 = data.loc[328]
    str38 = data.loc[332]
    str39 = data.loc[334]
    str40 = data.loc[600]
    str41 = data.loc[604]
    str42 = data.loc[606]
    
    #converting the data series to dataframe
    
    RUBLETP = str1.to_frame()
    RUBLEOI = str2.to_frame()
    RUBLETO = str3.to_frame()
    CADTP = str4.to_frame()
    CADOI = str5.to_frame()
    CADTO = str6.to_frame()
    CHFTP = str7.to_frame()
    CHFOI = str8.to_frame()
    CHFTO = str9.to_frame()
    PESOTP = str10.to_frame()
    PESOOI = str11.to_frame()
    PESOTO = str12.to_frame()
    GBPTP = str13.to_frame()
    GBPOI = str14.to_frame()
    GBPTO = str15.to_frame()
    JPYTP = str16.to_frame()
    JPYOI = str17.to_frame()
    JPYTO = str18.to_frame()
    EURFXTP = str19.to_frame()
    EURFXOI = str20.to_frame()
    EURFXTO = str21.to_frame()
    EURFXGBPTP = str22.to_frame()
    EURFXGBPOI = str23.to_frame()
    EURFXGBPTO = str24.to_frame()
    EURFXJPYTP = str25.to_frame()
    EURFXJPYOI = str26.to_frame()
    EURFXJPYTO = str27.to_frame()
    BRLTP = str28.to_frame()
    BRLOI = str29.to_frame()
    BRLTO = str30.to_frame()
    NZDTP = str31.to_frame()
    NZDOI = str32.to_frame()
    NZDTO = str33.to_frame()
    ZARTP = str34.to_frame()
    ZAROI = str35.to_frame()
    ZARTO = str36.to_frame()
    THREEMONTHEURUSDTP = str37.to_frame()
    THREEMONTHEURUSDOI = str38.to_frame()
    THREEMONTHEURUSDTO = str39.to_frame()
    AUDTP = str40.to_frame()
    AUDOI = str41.to_frame()
    AUDTO = str42.to_frame()
    
    #Renaming columns
    
    RUBLETP = RUBLETP.rename(columns = {136 : "Values"})
    RUBLEOI = RUBLEOI.rename(columns = {140 : "Values"})
    RUBLETO = RUBLETO.rename(columns = {142 : "Values"})
    CADTP = CADTP.rename(columns = {152 : "Values"})
    CADOI = CADOI.rename(columns = {156 : "Values"})
    CADTO = CADTO.rename(columns = {158 : "Values"})
    CHFTP = CHFTP.rename(columns = {168 : "Values"})
    CHFOI = CHFOI.rename(columns = {172 : "Values"})
    CHFTO = CHFTO.rename(columns = {174 : "Values"})
    PESOTP = PESOTP.rename(columns = {184 : "Values"})
    PESOOI = PESOOI.rename(columns = {188 : "Values"})
    PESOTO = PESOTO.rename(columns = {190 : "Values"})
    GBPTP = GBPTP.rename(columns = {200 : "Values"})
    GBPOI = GBPOI.rename(columns = {204 : "Values"})
    GBPTO = GBPTO.rename(columns = {206 : "Values"})
    JPYTP = JPYTP.rename(columns = {216 : "Values"})
    JPYOI = JPYOI.rename(columns = {220 : "Values"})
    JPYTO = JPYTO.rename(columns = {222 : "Values"})
    EURFXTP = EURFXTP.rename(columns = {232 : "Values"})
    EURFXOI = EURFXOI.rename(columns = {236 : "Values"})
    EURFXTO = EURFXTO.rename(columns = {238 : "Values"})
    EURFXGBPTP = EURFXGBPTP.rename(columns = {248 : "Values"})
    EURFXGBPOI = EURFXGBPOI.rename(columns = {252 : "Values"})
    EURFXGBPTO = EURFXGBPTO.rename(columns = {254 : "Values"})
    EURFXJPYTP = EURFXJPYTP.rename(columns = {264 : "Values"})
    EURFXJPYOI = EURFXJPYOI.rename(columns = {268 : "Values"})
    EURFXJPYTO = EURFXJPYTO.rename(columns = {270 : "Values"})
    BRLTP = BRLTP.rename(columns = {280 : "Values"})
    BRLOI = BRLOI.rename(columns = {284 : "Values"})
    BRLTO = BRLTO.rename(columns = {286 : "Values"})
    NZDTP = NZDTP.rename(columns = {296 : "Values"})
    NZDOI = NZDOI.rename(columns = {300 : "Values"})
    NZDTO = NZDTO.rename(columns = {302 : "Values"})
    ZARTP = ZARTP.rename(columns = {312 : "Values"})
    ZAROI = ZAROI.rename(columns = {316 : "Values"})
    ZARTO = ZARTO.rename(columns = {318 : "Values"})
    THREEMONTHEURUSDTP = THREEMONTHEURUSDTP.rename(columns = {328 : "Values"})
    THREEMONTHEURUSDOI = THREEMONTHEURUSDOI.rename(columns = {332 : "Values"})
    THREEMONTHEURUSDTO = THREEMONTHEURUSDTO.rename(columns = {334 : "Values"})
    AUDTP = AUDTP.rename(columns = {600 : "Values"})
    AUDOI = AUDOI.rename(columns = {604 : "Values"})
    AUDTO = AUDTO.rename(columns = {606 : "Values"})
    
    #Splitting the single column into multiple columns
    
    RUBLETP = pd.DataFrame(RUBLETP['Values'].str.split(' ').tolist())
    RUBLEOI = pd.DataFrame(RUBLEOI['Values'].str.split(' ').tolist())
    RUBLETO = pd.DataFrame(RUBLETO['Values'].str.split(' ').tolist())
    CADTP = pd.DataFrame(CADTP['Values'].str.split(' ').tolist())
    CADOI = pd.DataFrame(CADOI['Values'].str.split(' ').tolist())
    CADTO = pd.DataFrame(CADTO['Values'].str.split(' ').tolist())
    CHFTP = pd.DataFrame(CHFTP['Values'].str.split(' ').tolist())
    CHFOI = pd.DataFrame(CHFOI['Values'].str.split(' ').tolist())
    CHFTO = pd.DataFrame(CHFTO['Values'].str.split(' ').tolist())
    PESOTP = pd.DataFrame(PESOTP['Values'].str.split(' ').tolist())
    PESOOI = pd.DataFrame(PESOOI['Values'].str.split(' ').tolist())
    PESOTO = pd.DataFrame(PESOTO['Values'].str.split(' ').tolist())
    GBPTP = pd.DataFrame(GBPTP['Values'].str.split(' ').tolist())
    GBPOI = pd.DataFrame(GBPOI['Values'].str.split(' ').tolist())
    GBPTO = pd.DataFrame(GBPTO['Values'].str.split(' ').tolist())
    JPYTP = pd.DataFrame(JPYTP['Values'].str.split(' ').tolist())
    JPYOI = pd.DataFrame(JPYOI['Values'].str.split(' ').tolist())
    JPYTO = pd.DataFrame(JPYTO['Values'].str.split(' ').tolist())
    EURFXTP = pd.DataFrame(EURFXTP['Values'].str.split(' ').tolist())
    EURFXOI = pd.DataFrame(EURFXOI['Values'].str.split(' ').tolist())
    EURFXTO = pd.DataFrame(EURFXTO['Values'].str.split(' ').tolist())
    EURFXGBPTP = pd.DataFrame(EURFXGBPTP['Values'].str.split(' ').tolist())
    EURFXGBPOI = pd.DataFrame(EURFXGBPOI['Values'].str.split(' ').tolist())
    EURFXGBPTO = pd.DataFrame(EURFXGBPTO['Values'].str.split(' ').tolist())
    EURFXJPYTP = pd.DataFrame(EURFXJPYTP['Values'].str.split(' ').tolist())
    EURFXJPYOI = pd.DataFrame(EURFXJPYOI['Values'].str.split(' ').tolist())
    EURFXJPYTO = pd.DataFrame(EURFXJPYTO['Values'].str.split(' ').tolist())
    BRLTP = pd.DataFrame(BRLTP['Values'].str.split(' ').tolist())
    BRLOI = pd.DataFrame(BRLOI['Values'].str.split(' ').tolist())
    BRLTO = pd.DataFrame(BRLTO['Values'].str.split(' ').tolist())
    NZDTP = pd.DataFrame(NZDTP['Values'].str.split(' ').tolist())
    NZDOI = pd.DataFrame(NZDOI['Values'].str.split(' ').tolist())
    NZDTO = pd.DataFrame(NZDTO['Values'].str.split(' ').tolist())
    ZARTP = pd.DataFrame(ZARTP['Values'].str.split(' ').tolist())
    ZAROI = pd.DataFrame(ZAROI['Values'].str.split(' ').tolist())
    ZARTO = pd.DataFrame(ZARTO['Values'].str.split(' ').tolist())
    THREEMONTHEURUSDTP = pd.DataFrame(THREEMONTHEURUSDTP['Values'].str.split(' ').tolist())
    THREEMONTHEURUSDOI = pd.DataFrame(THREEMONTHEURUSDOI['Values'].str.split(' ').tolist())
    THREEMONTHEURUSDTO = pd.DataFrame(THREEMONTHEURUSDTO['Values'].str.split(' ').tolist())
    AUDTP = pd.DataFrame(AUDTP['Values'].str.split(' ').tolist())
    AUDOI = pd.DataFrame(AUDOI['Values'].str.split(' ').tolist())
    AUDTO = pd.DataFrame(AUDTO['Values'].str.split(' ').tolist())
    
    #Replacing whitespaces into np.nan values
    
    RUBLETP = RUBLETP.replace(r'^\s*$', np.nan, regex=True)
    RUBLEOI = RUBLEOI.replace(r'^\s*$', np.nan, regex=True)
    RUBLETO = RUBLETO.replace(r'^\s*$', np.nan, regex=True)
    CADTP = CADTP.replace(r'^\s*$', np.nan, regex=True)
    CADOI = CADOI.replace(r'^\s*$', np.nan, regex=True)
    CADTO = CADTO.replace(r'^\s*$', np.nan, regex=True)
    CHFTP = CHFTP.replace(r'^\s*$', np.nan, regex=True)
    CHFOI = CHFOI.replace(r'^\s*$', np.nan, regex=True)
    CHFTO = CHFTO.replace(r'^\s*$', np.nan, regex=True)
    PESOTP = PESOTP.replace(r'^\s*$', np.nan, regex=True)
    PESOOI = PESOOI.replace(r'^\s*$', np.nan, regex=True)
    PESOTO = PESOTO.replace(r'^\s*$', np.nan, regex=True)
    GBPTP = GBPTP.replace(r'^\s*$', np.nan, regex=True)
    GBPOI = GBPOI.replace(r'^\s*$', np.nan, regex=True)
    GBPTO = GBPTO.replace(r'^\s*$', np.nan, regex=True)
    JPYTP = JPYTP.replace(r'^\s*$', np.nan, regex=True)
    JPYOI = JPYOI.replace(r'^\s*$', np.nan, regex=True)
    JPYTO = JPYTO.replace(r'^\s*$', np.nan, regex=True)
    EURFXTP = EURFXTP.replace(r'^\s*$', np.nan, regex=True)
    EURFXOI = EURFXOI.replace(r'^\s*$', np.nan, regex=True)
    EURFXTO = EURFXTO.replace(r'^\s*$', np.nan, regex=True)
    EURFXGBPTP = EURFXGBPTP.replace(r'^\s*$', np.nan, regex=True)
    EURFXGBPOI = EURFXGBPOI.replace(r'^\s*$', np.nan, regex=True)
    EURFXGBPTO = EURFXGBPTO.replace(r'^\s*$', np.nan, regex=True)
    EURFXJPYTP = EURFXJPYTP.replace(r'^\s*$', np.nan, regex=True)
    EURFXJPYOI = EURFXJPYOI.replace(r'^\s*$', np.nan, regex=True)
    EURFXJPYTO = EURFXJPYTO.replace(r'^\s*$', np.nan, regex=True)
    BRLTP = BRLTP.replace(r'^\s*$', np.nan, regex=True)
    BRLOI = BRLOI.replace(r'^\s*$', np.nan, regex=True)
    BRLTO = BRLTO.replace(r'^\s*$', np.nan, regex=True)
    NZDTP = NZDTP.replace(r'^\s*$', np.nan, regex=True)
    NZDOI = NZDOI.replace(r'^\s*$', np.nan, regex=True)
    NZDTO = NZDTO.replace(r'^\s*$', np.nan, regex=True)
    ZARTP = ZARTP.replace(r'^\s*$', np.nan, regex=True)
    ZAROI = ZAROI.replace(r'^\s*$', np.nan, regex=True)
    ZARTO = ZARTO.replace(r'^\s*$', np.nan, regex=True)
    THREEMONTHEURUSDTP = THREEMONTHEURUSDTP.replace(r'^\s*$', np.nan, regex=True)
    THREEMONTHEURUSDOI = THREEMONTHEURUSDOI.replace(r'^\s*$', np.nan, regex=True)
    THREEMONTHEURUSDTO = THREEMONTHEURUSDTO.replace(r'^\s*$', np.nan, regex=True)
    AUDTP = AUDTP.replace(r'^\s*$', np.nan, regex=True)
    AUDOI = AUDOI.replace(r'^\s*$', np.nan, regex=True)
    AUDTO = AUDTO.replace(r'^\s*$', np.nan, regex=True)
    
    #Dropping nan columns
    
    RUBLETP = RUBLETP.dropna(axis = 'columns')
    RUBLEOI = RUBLEOI.dropna(axis = 'columns')
    RUBLETO = RUBLETO.dropna(axis = 'columns')
    CADTP = CADTP.dropna(axis = 'columns')
    CADOI = CADOI.dropna(axis = 'columns')
    CADTO = CADTO.dropna(axis = 'columns')
    CHFTP = CHFTP.dropna(axis = 'columns')
    CHFOI = CHFOI.dropna(axis = 'columns')
    CHFTO = CHFTO.dropna(axis = 'columns')
    PESOTP = PESOTP.dropna(axis = 'columns')
    PESOOI = PESOOI.dropna(axis = 'columns')
    PESOTO = PESOTO.dropna(axis = 'columns')
    GBPTP = GBPTP.dropna(axis = 'columns')
    GBPOI = GBPOI.dropna(axis = 'columns')
    GBPTO = GBPTO.dropna(axis = 'columns')
    JPYTP = JPYTP.dropna(axis = 'columns')
    JPYOI = JPYOI.dropna(axis = 'columns')
    JPYTO = JPYTO.dropna(axis = 'columns')
    EURFXTP = EURFXTP.dropna(axis = 'columns')
    EURFXOI = EURFXOI.dropna(axis = 'columns')
    EURFXTO = EURFXTO.dropna(axis = 'columns')
    EURFXGBPTP = EURFXGBPTP.dropna(axis = 'columns')
    EURFXGBPOI = EURFXGBPOI.dropna(axis = 'columns')
    EURFXGBPTO = EURFXGBPTO.dropna(axis = 'columns')
    EURFXJPYTP = EURFXJPYTP.dropna(axis = 'columns')
    EURFXJPYOI = EURFXJPYOI.dropna(axis = 'columns')
    EURFXJPYTO = EURFXJPYTO.dropna(axis = 'columns')
    BRLTP = BRLTP.dropna(axis = 'columns')
    BRLOI = BRLOI.dropna(axis = 'columns')
    BRLTO = BRLTO.dropna(axis = 'columns')
    NZDTP = NZDTP.dropna(axis = 'columns')
    NZDOI = NZDOI.dropna(axis = 'columns')
    NZDTO = NZDTO.dropna(axis = 'columns')
    ZARTP = ZARTP.dropna(axis = 'columns')
    ZAROI = ZAROI.dropna(axis = 'columns')
    ZARTO = ZARTO.dropna(axis = 'columns')
    THREEMONTHEURUSDTP = THREEMONTHEURUSDTP.dropna(axis = 'columns')
    THREEMONTHEURUSDOI = THREEMONTHEURUSDOI.dropna(axis = 'columns')
    THREEMONTHEURUSDTO = THREEMONTHEURUSDTO.dropna(axis = 'columns')
    AUDTP = AUDTP.dropna(axis = 'columns')
    AUDOI = AUDOI.dropna(axis = 'columns')
    AUDTO = AUDTO.dropna(axis = 'columns')
    
    #Renaming Columns
    
    RUBLETP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    RUBLEOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    RUBLETO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    CADTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    CADOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    CADTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    CHFTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    CHFOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    CHFTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    PESOTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    PESOOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    PESOTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    GBPTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    GBPOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    GBPTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    JPYTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    JPYOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    JPYTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    EURFXTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    EURFXGBPTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXGBPOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXGBPTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    EURFXJPYTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXJPYOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    EURFXJPYTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    BRLTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    BRLOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    BRLTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    NZDTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    NZDOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    NZDTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    ZARTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    ZAROI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    ZARTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    THREEMONTHEURUSDTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    THREEMONTHEURUSDOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    THREEMONTHEURUSDTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    AUDTP.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    AUDOI.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort','NRLong','NRShort']
    AUDTO.columns = ['NCLong','NCShort','NCSpreads','CLong','CShort','TLong','TShort']
    
    # Appending datasets
    
    Combined = RUBLETP.append([RUBLEOI, RUBLETO, CADTP, CADOI, CADTO, CHFTP, CHFOI, CHFTO, PESOTP, PESOOI, PESOTO, GBPTP, GBPOI,
    GBPTO,JPYTP,JPYOI, JPYTO, EURFXTP, EURFXOI, EURFXTO, EURFXGBPTP, EURFXGBPOI, EURFXGBPTO, EURFXJPYTP, 
    EURFXJPYOI, EURFXJPYTO, BRLTP, BRLOI, BRLTO, NZDTP, NZDOI, NZDTO, ZARTP, ZAROI, ZARTO,
    THREEMONTHEURUSDTP, THREEMONTHEURUSDOI,THREEMONTHEURUSDTO, AUDTP, AUDOI, AUDTO])
    
    #Renaming row names and filling nan values with 0
    
    Combined['No'] = np.arange(len(Combined))
    Combined = Combined.set_index('No')
    
    #Renaming row names and filling nan values with 0
    
    Combined = Combined.rename(index = {0 : 'RUBLETP', 1: 'RUBLEOI', 2: 'RUBLETO',
                                       3 : 'CADTP', 4: 'CADOI', 5: 'CADTO',
                                       6 : 'CHFTP', 7: 'CHFOI', 8: 'CHFTO',
                                       9 : 'PESOTP', 10: 'PESOOI', 11: 'PESOTO', 
                                       12 : 'GBPTP', 13: 'GBPOI', 14: 'GBPTO', 
                                       15 : 'JPYTP', 16: 'JPYOI', 17: 'JPYTO', 
                                       18 : 'EURFXTP', 19: 'EURFXOI', 20: 'EURFXTO', 
                                       21 : 'EURFXGBPTP', 22: 'EURFXGBPOI', 23: 'EURFXGBPTO', 
                                       24 : 'EURFXJPYTP', 25: 'EURFXJPYOI', 26: 'EURFXJPYTO', 
                                       27 : 'BRLTP', 28: 'BRLOI', 29: 'BRLTO', 
                                       30 : 'NZDTP', 31: 'NZDOI', 32: 'NZDTO', 
                                       33 : 'ZARTP', 34: 'ZAROI', 35: 'ZARTO', 
                                       36 : 'THREEMONTHEURUSDTP', 37: 'THREEMONTHEURUSDOI', 38: 'THREEMONTHEURUSDTO', 
                                       39 : 'AUDTP', 40: 'AUDOI', 41: 'AUDTO'})
    Combined = Combined.fillna(0)
    
    return (Combined)

