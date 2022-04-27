import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots


@st.cache
def load_data():
    data = pd.read_csv("data/us_covid19_vaccine_cases_deaths_daily_count_variant.csv")
    data["date"] = pd.to_datetime(data["date"]).dt.date
    return data


@st.cache
def get_all_states(df):
    return df["Province_State"].unique().tolist()


@st.cache
def get_all_variants(df):
    return df["Variant"].unique().tolist()


def plot_daily_deaths(data, start_date, end_date, states):
    data = data[np.logical_and(data["date"] >= start_date, data["date"] <= end_date)]
    fig = go.Figure()
    for state in states:
        state_data = data[data["Province_State"] == state]
        x = state_data["date"]
        y = state_data["daily_deaths"]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name=state))
    fig.update_layout(
        title="US States - Daily Deaths",
        xaxis_title="Date",
        yaxis_title="Daily death count",
        legend_title="State",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.8))
    st.plotly_chart(fig, use_container_width=True)


def plot_daily_vaccines(data, start_date, end_date, states):
    data = data[np.logical_and(data["date"] >= start_date, data["date"] <= end_date)]
    fig = go.Figure()
    for state in states:
        state_data = data[data["Province_State"] == state]
        x = state_data["date"]
        y = state_data["daily_fully_vaccinated"]
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name=state))
    fig.update_layout(
        title="US States - Daily Vaccines",
        xaxis_title="Date",
        yaxis_title="Daily fully vaccinated count",
        legend_title="State",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.8))
    st.plotly_chart(fig, use_container_width=True)


def plot_daily_deaths_vaccines(data, start_date, end_date, state):
    data = data[np.logical_and(data["date"] >= start_date, data["date"] <= end_date)]
    state_data = data[data["Province_State"] == state]
    x = state_data["date"]
    y1 = state_data["daily_deaths"]
    y2 = state_data["daily_fully_vaccinated"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', name="Deaths"), secondary_y=False)
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name="Fully Vaccinated"), secondary_y=True)
    fig.update_layout(
        title="US States - Daily Deaths and Vaccines",
        xaxis_title="Date",
        legend_title=state,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.8))
    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1)
    fig.update_yaxes(title_text="Daily death count", secondary_y=False)
    fig.update_yaxes(title_text="Daily fully vaccinated count", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)


def plot_variant_daily_deaths_vaccines(data, state, variant):
    state_data = data[np.logical_and(data["Province_State"] == state, data["Variant"] == variant)]
    x = state_data["date"]
    y1 = state_data["daily_deaths"]
    y2 = state_data["daily_fully_vaccinated"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', name="Deaths"), secondary_y=False)
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name="Fully Vaccinated"), secondary_y=True)
    fig.update_layout(
        title="US States - Variant Analysis",
        xaxis_title="Date",
        legend_title=state,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.8))
    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1)
    fig.update_yaxes(title_text="Daily death count", secondary_y=False)
    fig.update_yaxes(title_text="Daily fully vaccinated count", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)


def main():
    st.markdown("# Covid-19 Deaths and Vaccine Data")
    st.write("This app shows different visualizations for Covid-19 deaths and vaccine data")

    option = st.sidebar.selectbox("Plots", options=["Introduction", "US States - Deaths", "US States - Vaccines",
                                                    "US State - Deaths and Vaccines", "US State - Variant"], index=0)
    covid_data = load_data()
    all_states = get_all_states(covid_data)
    all_variants = get_all_variants(covid_data)

    if option == "Introduction":
        st.write(covid_data.head(10))
    elif option == "US States - Deaths":
        states = st.multiselect("Choose state/s", options=all_states, default=["California", "New York"])
        start_date, end_date = st.slider("Date", value=(covid_data["date"][0], covid_data["date"][len(covid_data) - 1]))
        plot_daily_deaths(covid_data, start_date, end_date, states)
    elif option == "US States - Vaccines":
        states = st.multiselect("Choose state/s", options=all_states, default=["California", "New York"])
        start_date, end_date = st.slider("Date", value=(covid_data["date"][0], covid_data["date"][len(covid_data) - 1]))
        plot_daily_vaccines(covid_data, start_date, end_date, states)
    elif option == "US State - Deaths and Vaccines":
        min_date, max_date = covid_data["date"][0], covid_data["date"][len(covid_data) - 1]
        state = st.selectbox("Choose state", options=all_states, index=0)
        start_date, end_date = st.slider("Dates", min_value=min_date, max_value=max_date, value=(min_date, max_date))
        plot_daily_deaths_vaccines(covid_data, start_date, end_date, state)
    elif option == "US State - Variant":
        state = st.selectbox("Choose state", options=all_states, index=5)
        variant = st.selectbox("Variant", options=all_variants, index=2)
        plot_variant_daily_deaths_vaccines(covid_data, state, variant)


if __name__ == "__main__":
    main()
