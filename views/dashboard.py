import streamlit as st
from forms.del_form import del_form
from Database.Db import load_data
import plotly.express as px

#Session state
if 'df' not in st.session_state:
    st.session_state.df = None

st.set_page_config(page_title="HR Dashboard", layout="wide")
st.title("HR Dashboard")


#Load data
if st.session_state.df is None:
    with st.spinner("Loading Data please wait !!"):
        load_data()


#Count
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Employees", st.session_state.df.shape[0])
with col2:
    st.metric("Departments",st.session_state.df['DEPARTMENT'].nunique() )
with col3:
    st.metric("Avg. Experience","hello1") #add some other metric


# Department distribution
fig = px.pie(st.session_state.df, names='DEPARTMENT', title='Employee Distribution by Department')
st.plotly_chart(fig, use_container_width=True)
    
# # Experience distribution
#     fig = px.histogram(st.session_state.employees, x='Years of Experience', title='Distribution of Experience')
#     st.plotly_chart(fig, use_container_width=True)


#Table
st.dataframe(st.session_state.df,use_container_width=True,)

#Delete function
# #Buttons
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     @st.dialog("DELETE Entry")
#     def show_del_form():
#         del_form()

#     if st.button("Delete Entry",use_container_width=True):
#         show_del_form()