import streamlit as st
from app_fns import tnved_1, tnved_2, tnved_3, tnved_4

def change_label_style(label, font_size='12px', font_color='dark-grey', font_family='sans-serif'):
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

st.markdown('<h1 style="color:darkred; font-weight:bold; font-size:48px; text-align:center">Товарная номенклатура внешнеэкономической деятельности (ТНВЭД)</h1>', unsafe_allow_html=True)  
st.markdown('<p style="color:darkred; text-align:center">'
            'По данным сайта <a href="(https://www.nalog.gov.ru/rn77/program/5961290/">www.nalog.gov.ru</a> опубликованным 17-10-2024', unsafe_allow_html=True)

ids1 = tnved_1()
for id1, d1 in ids1.items():
    if f'{id1}_state' not in st.session_state:
        st.session_state[f'{id1}_state'] = False
    show_1 = st.button(f"**{id1}. {d1['name1']}**", key=id1, type='primary', use_container_width=True)
    if show_1:
        if st.session_state[f'{id1}_state']:
            st.session_state[f'{id1}_state'] = False
        else:
            st.session_state[f'{id1}_state'] = True



    if st.session_state[f'{id1}_state']:
        if d1['rem1']:
            if f'{id1}_rem_state' not in st.session_state:
                st.session_state[f'{id1}_rem_state'] = False
            show_1_rem = st.button(f'**Примечание к {id1}**', type='primary')
            if show_1_rem:
                if st.session_state[f'{id1}_rem_state']:
                    st.session_state[f'{id1}_rem_state'] = False
                else:
                    st.session_state[f'{id1}_rem_state'] = True
            if st.session_state[f'{id1}_rem_state']:        
                st.markdown(f'<p style="color:firebrick;">{d1["rem1"]}</p>', unsafe_allow_html=True)
        ids2 = tnved_2(id1)
        for id2, d2 in ids2.items():
            ids3 = tnved_3(id2)

            with st.expander(f"**{id1} {id2}. {d2['name2']}**"):
                if d2['rem2']:
                    if f'{id1}_{id2}_rem_state' not in st.session_state:
                        st.session_state[f'{id1}_{id2}_rem_state' ] = False
                    show_2_rem = st.button(f'**Примечание к {id1} {id2}**', key=id1+id2)#, use_container_width=True)
                    if show_2_rem:
                        if st.session_state[f'{id1}_{id2}_rem_state' ]:
                            st.session_state[f'{id1}_{id2}_rem_state'] = False
                        else:
                            st.session_state[f'{id1}_{id2}_rem_state' ] = True
                    if st.session_state[f'{id1}_{id2}_rem_state' ]:        
                        st.write(f">{d2['rem2']}")

                for id3, d3 in ids3.items():
                    if f'{id1}_{id2}_{id3}_state' not in st.session_state:
                        st.session_state[f'{id1}_{id2}_{id3}_state'] = False
    
                    show_4 = st.button(f"{id1} {id2} {id3}. {d3['name3']}", key = id1+id2+id3, use_container_width=True)

                    if show_4:
                        if st.session_state[f'{id1}_{id2}_{id3}_state']:
                            st.session_state[f'{id1}_{id2}_{id3}_state'] = False
                        else:
                            st.session_state[f'{id1}_{id2}_{id3}_state'] = True

                    if st.session_state[f'{id1}_{id2}_{id3}_state']:    
                        ids4 = tnved_4(id2, id3)
                        for id4, d4 in ids4.items():
                            string = f" - _{id1} {id2} {id3} {id4}. {d4['name4']}_"
                            #change_label_style(string, font_size='8px', font_color='red', font_family='sans-serif')
                            #st.write(string)
                            st.markdown(f'<p style="margin-left:30px;">'
                                        f'<span style="font-size:13px; font-weight: bold; font-style:italic;">'
                                        f'{id1} {id2} {id3} {id4}. </span>'
                                        f'<span style="font-size:13px; font-style:italic;">'
                                        f'{d4["name4"]}</span></p>', unsafe_allow_html=True)
