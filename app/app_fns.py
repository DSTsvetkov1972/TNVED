import pandas as pd
from datetime import datetime
from colorama import Fore
import streamlit as st

def data_parcer(data_str):
    try:
        return datetime.strptime(data_str, '%d.%m.%Y')
    except:
        return None

def tnved_1():
    df = pd.read_csv('TNVED1.TXT',
                     encoding = 'cp866',
                     sep='|', usecols=[0, 1, 2, 3],
                     names=['id1', 'name1', 'rem1', 'date'],
                     skiprows=1,
                     dtype='str')
    df = df.fillna("")    

    df['date'] = df['date'].apply(data_parcer)
    ids1 = sorted(list(set(df['id1'])))

    res = {}
    for id1 in ids1:
        id1_df = df[(df['id1']==id1)]
        id1_df = id1_df[(id1_df['date']==max(id1_df['date']))]
        res[id1] = dict(id1_df[['name1','rem1']].iloc[0])
    return res

def tnved_2(id1='01'):
    df = pd.read_csv('TNVED2.TXT',
                     encoding = 'cp866',
                     sep='|',
                     usecols=[0, 1, 2, 3, 4],
                     names=['id1', 'id2', 'name2', 'rem2', 'date'],
                     skiprows=1,
                     dtype='str')
    df = df.fillna("")
    df['date'] = df['date'].apply(data_parcer)
    id1_df = df[df['id1']==id1]

    ids2 = sorted(list(set(id1_df['id2'])))

    res = {}
    for id2 in ids2:
        id2_df = id1_df[id1_df['id2']==id2]
        id2_df = id2_df[id2_df['date']==max(id2_df['date'])]
        res[id2] = dict(id2_df[['name2', 'rem2']].iloc[0])
    return res

def tnved_3(id2='01'):
    df = pd.read_csv('TNVED3.TXT',
                     encoding = 'cp866',
                     sep='|',
                     usecols=[0, 1, 2, 3],
                     names=['id2', 'id3', 'name3', 'date'],
                     skiprows=1,
                     dtype='str')
    df = df.fillna("")
    df['date'] = df['date'].apply(data_parcer)

    id2_df = df[df['id2']==id2]
    
    ids3 = sorted(list(set(id2_df['id3'])))

    res = {}
    for id3 in ids3:
        id3_df = id2_df[id2_df['id3']==id3]
        id3_df = id3_df[id3_df['date']==max(id3_df['date'])]
        res[id3] = dict(id3_df[['name3']].iloc[0])
    return res

def tnved_4(id2='01', id3='01'):
    df = pd.read_csv('TNVED4.TXT',
                     encoding = 'cp866',
                     sep='|',
                     usecols=[0, 1, 2, 3, 4],
                     names=['id2', 'id3', 'id4', 'name4', 'date'],
                     skiprows=1,
                     dtype='str') 
    df = df.fillna("")    
    df['date'] = df['date'].apply(data_parcer)
    id23_df = df[(df['id2']==id2) & (df['id3']==id3)]
    ids4 = sorted(list(set(id23_df['id4'])))

    res = {}
    for id4 in ids4:
        id4_df = id23_df[id23_df['id4']==id4]
        id4_df = id4_df[id4_df['date']==max(id4_df['date'])]
        res[id4] = dict(id4_df[['name4']].iloc[0])
        
    return res

def change_label_style(label, font_size='12px', font_color='black', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)

if __name__ == '__main__':
    print(Fore.YELLOW, tnved_1(), Fore.WHITE)
    print(Fore.CYAN, tnved_2('01'), Fore.WHITE)
    print(Fore.MAGENTA, tnved_3('02'), Fore.WHITE)
    for k, v in tnved_4('02', '03').items():
        print(Fore.BLUE, k,v, Fore.WHITE)
