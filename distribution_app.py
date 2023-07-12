import yfinance as yf
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


st.write("### Quick app for visualization of distributions")
st.write("")
st.write("")
st.write("")
st.write("")

st.sidebar.header('Input Parameters')
st.sidebar.write(f'Choose type of distribution, for example "Normal"')
distribution_type = st.sidebar.selectbox('Type of distribution',('Normal', 'Exponential', 'Poisson'))
st.sidebar.write(f'Specify inputs for distrubution')

if distribution_type == 'Normal':
    mu = st.sidebar.slider('Mean', 0.0, 10.0, 5.0)
    sigma = st.sidebar.slider('Standard deviation', 0.0, 10.0, 2.0)
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    
    st.write(f'###### Normal distribution with mean = {mu} and sigma = {sigma}')
    st.write("")
    # st.line_chart(tickerDf.Close)
    plt.plot(x, y)
    st.pyplot()

elif distribution_type == 'Exponential':
    lambd = st.sidebar.slider('Parameter λ', 0.0, 10.0, 1.0)
    x = np.linspace(0, 10, 100)
    y = lambd * np.exp(-lambd * x)
    st.write(f'###### Exponerrential distribution with lambda = {lambd}')
    st.write("")
    plt.plot(x, y)
    st.pyplot()
    
elif distribution_type == 'Poisson':
    lam = st.sidebar.slider('Parameter λ', 0.0, 10.0, 2.0)
    x = np.arange(0, 10)
    y = stats.poisson.pmf(x, lam)
    st.write(f'###### Poisson distribution with lambda = {lam}')
    st.write("")
    plt.plot(x, y)
    st.pyplot()

# ticker = yf.Ticker(ticker_input)
# company_name = ticker.info["longName"]
# st.sidebar.write(f'You chose ticker of {company_name}')
# period_select = st.sidebar.selectbox('Period for fin data aproximation',('1d', '1wk', '1mo', '3mo'))
# period = str(period_select)
# default_start = datetime.date(2010, 1, 1)
# default_end = datetime.date.today()
# start = st.sidebar.date_input(label='Start date of analysis', value=default_start)
# end = st.sidebar.date_input(label='End date of analysis', value=default_end)
