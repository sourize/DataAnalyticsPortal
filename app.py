import pandas as pd 
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title='Data Analytics Portal',
    page_icon='📊'
)

st.title(':blue[📊 Data Analytics Portal]')
st.subheader(':grey[ An easy way to Analyse Data!!]', divider='green')

file = st.file_uploader('Drop csv or excel file', type=['csv', 'xlsx'])
if file:
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.dataframe(data)
    st.info('File is successfully Uploaded', icon='🚨')

    st.subheader(':blue[Basic information of the dataset]', divider='green')
    
    tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

    with tab1:
        st.write(f'There are {data.shape[0]} rows in dataset and {data.shape[1]} columns in the dataset')
        st.subheader(':gray[Statistical summary of the dataset]')
        st.dataframe(data.describe())
    
    with tab2:
        st.subheader(':gray[Top Rows]')
        toprows = st.slider('Number of rows you want', 1, data.shape[0], key='topslider')
        st.dataframe(data.head(toprows))
        st.subheader(':gray[Bottom Rows]')
        bottomrows = st.slider('Number of rows you want', 1, data.shape[0], key='bottomslider')
        st.dataframe(data.tail(bottomrows))
    
    with tab3:
        st.subheader(':grey[Data types of column]')
        st.dataframe(data.dtypes)
    
    with tab4:
        st.subheader('Column Names in Dataset')
        st.write(list(data.columns))

    st.subheader(':blue[Column Values To Count]', divider='green')
    
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose Column name', options=list(data.columns))
        with col2:
            toprows = st.number_input('Top rows', min_value=1, step=1)
        
        count = st.button('Count')
        if count:
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualization', divider='gray')
            fig = px.bar(data_frame=result, x=column, y='count', text='count', template='plotly_white')
            st.plotly_chart(fig)
            fig = px.line(data_frame=result, x=column, y='count', text='count', template='plotly_white')
            st.plotly_chart(fig)
            fig = px.pie(data_frame=result, names=column, values='count')
            st.plotly_chart(fig)
else:
    st.warning('Please upload a CSV or Excel file to get started', icon='⚠️')