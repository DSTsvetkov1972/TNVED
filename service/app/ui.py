import streamlit as st
from app_fns import (get_tnved_1_df, get_tnved_2_df, get_tnved_3_df, get_tnved_4_df,
                     tnved_1, tnved_2, tnved_3, tnved_4,
                     change_button_status)
from colorama import Fore

if 'tnved_1_df' not in st.session_state:
    st.session_state.tnved_1_df = get_tnved_1_df()
if 'tnved_2_df' not in st.session_state:
    st.session_state.tnved_2_df = get_tnved_2_df()
if 'tnved_3_df' not in st.session_state:
    st.session_state.tnved_3_df = get_tnved_3_df()
if 'tnved_4_df' not in st.session_state:
    st.session_state.tnved_4_df = get_tnved_4_df()

st.markdown('<h1 style="color:darkred; font-weight:bold; text-align:center">'
            'Товарная номенклатура внешнеэкономической деятельности (ТНВЭД)</h1>', unsafe_allow_html=True)  
st.markdown('<p style="color:darkred; text-align:center">'
            'По данным сайта <a href="https://www.nalog.gov.ru/rn77/program/5961290/">'
            'www.nalog.gov.ru</a> опубликованным 17-10-2024',
            unsafe_allow_html=True)

ids1 = tnved_1(st.session_state.tnved_1_df)
for id1, d1 in ids1.items():
    if f'{id1}_state' not in st.session_state:
        st.session_state[f'{id1}_state'] = False
    show_1 = st.button(f"**{id1}. {d1['name1']}**",
                       key=id1,
                       type='primary',
                       on_click=change_button_status,
                       args = [st.session_state, f'{id1}_state'],
                       use_container_width=True)

    if st.session_state[f'{id1}_state']:
        if d1['rem1'] and d1['rem1']!=' ':
            if f'{id1}_rem_state' not in st.session_state:
                st.session_state[f'{id1}_rem_state'] = False
            show_1_rem = st.button(f'**Примечание к {id1}**',
                                   on_click=change_button_status,
                                   args = [st.session_state, f'{id1}_rem_state'], type='primary')

            if st.session_state[f'{id1}_rem_state']:
                height = 500 if len(d1["rem1"])>1880 else None    
                with st.container(height=height):    
                    st.markdown(f'<p style="color:firebrick;">'
                                f'{d1["rem1"]}</p>',
                                unsafe_allow_html=True)
        ids2 = tnved_2(st.session_state.tnved_2_df, id1)
        for id2, d2 in ids2.items():
            ids3 = tnved_3(st.session_state.tnved_3_df, id2)

            with st.expander(f"**{id1} {id2}. {d2['name2']}**"):
                if True:
                    if d2['rem2']:
                        if f'{id1}_{id2}_rem_state' not in st.session_state:
                            st.session_state[f'{id1}_{id2}_rem_state'] = False
                        show_2_rem = st.button(f'**Примечание к {id1} {id2}**',
                                            key=id1+id2,
                                            on_click=change_button_status,
                                            args=[st.session_state,
                                                    f'{id1}_{id2}_rem_state'])

                        if st.session_state[f'{id1}_{id2}_rem_state' ]: 
                            height = 500 if len(d2["rem2"])>1880 else None    
                            with st.container(height=height):       
                                st.write(f">{d2['rem2']}")

                for id3, d3 in ids3.items():
                    if f'{id1}_{id2}_{id3}_state' not in st.session_state:
                        st.session_state[f'{id1}_{id2}_{id3}_state'] = False
    
                    show_4 = st.button(f"{id1} {id2} {id3}. {d3['name3']}",
                                       key = id1+id2+id3,
                                       on_click=change_button_status,
                                       args=[st.session_state, f'{id1}_{id2}_{id3}_state'],
                                       use_container_width=True)

                    if st.session_state[f'{id1}_{id2}_{id3}_state']:    
                        ids4 = tnved_4(st.session_state.tnved_4_df, id2, id3)
                        height = 500 if len(ids4.items()) > 10 else None
                        with st.container(height=height): #, border=True):
                            for id4, d4 in ids4.items():
                                string = f" - _{id1} {id2} {id3} {id4}. {d4['name4']}_"
                                st.markdown(f'<p style="margin-left:30px;">'
                                            f'<span style="font-size:13px; font-weight: bold; font-style:italic;">'
                                            f'{id1} {id2} {id3} {id4}. </span>'
                                            f'<span style="font-size:13px; font-style:italic;">'
                                            f'{d4["name4"]}</span></p>', unsafe_allow_html=True)
