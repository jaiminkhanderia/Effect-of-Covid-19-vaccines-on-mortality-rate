import numpy as np
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots


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
    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
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
    fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
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


def plot_overall_deaths_vaccines(data, start_date, end_date, state):
    data = data[np.logical_and(data["date"] >= start_date, data["date"] <= end_date)]
    state_data = data[data["Province_State"] == state]
    x = state_data["date"]
    y1 = state_data["Deaths"]
    y2 = state_data["People_Fully_Vaccinated"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', name="Deaths"), secondary_y=False)
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name="Fully Vaccinated"), secondary_y=True)
    fig.update_layout(
        title="US States - Overall Deaths and Vaccines",
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
    fig.update_yaxes(title_text="Overall death count", secondary_y=False)
    fig.update_yaxes(title_text="Overall fully vaccinated count", secondary_y=True)
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
