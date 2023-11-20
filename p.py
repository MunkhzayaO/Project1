import pandas as pd
import streamlit as st 
import plotly.express as px

def load_data():
    #Function for loading data
    df = pd.read_csv("banks.csv", index_col="date")
    
    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns
    
    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns
    
    stock_column = df['name']
    
    unique_stocks = stock_column.unique()
    
     # Create a dictionary to store news for each stock
    news_dict = {
        'TDB': "IPO price is **33'000** tukrig and Current price is **25'980** tukrig",
        'XAC': "IPO price is **677** tukrig and Current price is **579** tukrig",
        'GLMT': "IPO price is **1'285** tukrig and Current price is **875** tukrig",
        'SBM': "IPO price is **590** tukrig and Current price is **451** tukrig",
        'KHAN': "IPO price is **959** tukrig and Current price is **1'054** tukrig",
        
        # Add more news for other stocks as needed
    }
    
    return df, numeric_cols, text_cols, unique_stocks, news_dict


df, numeric_cols, text_cols, unique_stocks, news_dict = load_data() 



#Title of dashboard
st.title("Stock Dashboard")


   #Let's show the dataset

#Give sidebar a title
st.sidebar.title("Settings")
st.sidebar.subheader("Timeseries settings")
feature_selection = st.sidebar.multiselect(label="Features to plot",
                                           options=numeric_cols)

stock_dropdown = st.sidebar.selectbox(label="Stock Ticker",
                                      options=unique_stocks)


print(feature_selection)

df = df[df['name']==stock_dropdown]
df_features = df[feature_selection]

plotly_figure = px.line(data_frame=df_features,
                        x=df_features.index,y=feature_selection,
                        title=(str(stock_dropdown) + ' ' +'timeline')
                       )


st.plotly_chart(plotly_figure)

# Display news based on the selected stock
selected_stock_news = news_dict.get(stock_dropdown, "No news available for this stock.")
st.write(f"News for {stock_dropdown}:", selected_stock_news)

# Create a sidebar with tabs
#selected_tab = st.sidebar.radio("Select Tab", ["News", "Other"])

# Display content based on the selected tab
#if selected_tab == "News":
    #st.write("News content goes here")
