import streamlit as st
from pandas import Series
from numpy.random import randn
pg = st.navigation([st.Page("pag_1.py", icon=":material/dashboard:"),
                    st.Page("pag_2.py", icon=":material/dashboard:"),
                    st.Page("pag_3.py", icon=":material/dashboard:"),
                    st.Page("pag_4.py", icon=":material/dashboard:"),
                    st.Page("pag_5.py", icon=":material/dashboard:")                    
                    
                    ])
pg.run()