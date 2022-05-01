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


def plot_adult_hospitalizations_vaccinations(data):
    x = data["Week ending"]
    y1 = data["Rate in unvaccinated"]
    y2 = data["Rate in fully vaccinated"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', name='Rate in unvaccinated people'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name='Rate in fully vaccinated people'))
    fig.update_layout(
        title="Age-Adjusted Rates of COVID-19-Associated Hospitalizations by Vaccination Status in Adults Ages ≥18 Years",
        title_y=0.95,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.23, xanchor="left", x=0.7))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Rate per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_age_group_hospitalizations_vaccinations(data, age_group):
    data = data[data["Age group"] == age_group]
    x = data["Week ending"]
    y1 = data["Rate in unvaccinated"]
    y2 = data["Rate in fully vaccinated"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', name='Rate in unvaccinated people'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', name='Rate in fully vaccinated people'))
    fig.update_layout(
        title="Rates of COVID-19-Associated Hospitalizations by Vaccination Status for Age group: {}".format(age_group),
        title_y=0.95,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.23, xanchor="left", x=0.7))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Rate per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_booster_adult_hospitalizations_vaccinations(data):
    x = data["Week ending"]
    y1 = data["Rate in unvaccinated"]
    y2 = data["Rate in fully vaccinated without additional or booster"]
    y3 = data["Rate in fully vaccinated with additional or booster"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', line_color='#EF553B', name='Rate in unvaccinated'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', line_color='#636EFA',
                             name='Rate in fully vaccinated without additional or booster'))
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines+markers', line_color='#00CC96',
                             name='Rate in fully vaccinated with additional or booster'))

    fig.update_layout(
        title="Age-Adjusted Rates of COVID-19-Associated Hospitalizations by Vaccination Status in Adults Ages ≥18 Years",
        title_y=1,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.52))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Rate per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_booster_age_group_hospitalizations_vaccinations(data, age_group):
    data = data[data["Age group"] == age_group]
    x = data["Week ending"]
    y1 = data["Rate in unvaccinated"]
    y2 = data["Rate in fully vaccinated without additional or booster"]
    y3 = data["Rate in fully vaccinated with additional or booster"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', line_color='#EF553B', name='Rate in unvaccinated'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', line_color='#636EFA',
                             name='Rate in fully vaccinated without additional or booster'))
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines+markers', line_color='#00CC96',
                             name='Rate in fully vaccinated with additional or booster'))

    fig.update_layout(
        title="Rates of COVID-19-Associated Hospitalizations by Vaccination Status for Age group: {}".format(age_group),
        title_y=1,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.52))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Rate per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_overall_cases_vaccinations(data, title_choice):
    choice = "case" if title_choice == "Cases" else "death"
    data = data[np.logical_and(data["outcome"] == choice,
                               np.logical_and(data["age_group"] == "all_ages", data["vaccine_product"] == "all_types"))]
    x = data["date"]
    y1 = data["age_adj_unvax_ir"]
    y2 = data["age_adj_vax_ir"]
    y3 = data["age_adj_booster_ir"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', line_color='#EF553B', name='Unvaccinated'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', line_color='#636EFA',
                             name='Vaccinated with a primary series only'))
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines+markers', line_color='#00CC96',
                             name='Vaccinated with a primary series and booster dose'))

    fig.update_layout(
        title="Rates of COVID-19 {} by Vaccination Status and Booster Dose".format(title_choice),
        title_y=1,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.55))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Incidence per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_age_group_cases_vaccinations(data, title_choice, age_group):
    choice = "case" if title_choice == "Cases" else "death"
    data = data[np.logical_and(data["outcome"] == choice,
                               np.logical_and(data["age_group"] == age_group, data["vaccine_product"] == "all_types"))]
    x = data["date"]
    y1 = data["crude_unvax_ir"]
    y2 = data["crude_primary_series_only_ir"]
    y3 = data["crude_booster_ir"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', line_color='#EF553B', name='Unvaccinated'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', line_color='#636EFA',
                             name='Vaccinated with a primary series only'))
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines+markers', line_color='#00CC96',
                             name='Vaccinated with a primary series and booster dose'))

    fig.update_layout(
        title="Rates of COVID-19 {} by Vaccination Status and Booster Dose for Age Group: {}".format(title_choice,
                                                                                                     age_group),
        title_y=1,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.55))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Incidence per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)


def plot_vaccine_cases_vaccinations(data, title_choice, vaccine):
    choice = "case" if title_choice == "Cases" else "death"
    data = data[np.logical_and(data["outcome"] == choice,
                               np.logical_and(data["age_group"] == "all_ages", data["vaccine_product"] == vaccine))]
    x = data["date"]
    y1 = data["age_adj_unvax_ir"]
    y2 = data["age_adj_vax_ir"]
    y3 = data["age_adj_booster_ir"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines+markers', line_color='#EF553B', name='Unvaccinated'))
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines+markers', line_color='#636EFA',
                             name='Vaccinated with a primary series only'))
    fig.add_trace(go.Scatter(x=x, y=y3, mode='lines+markers', line_color='#00CC96',
                             name='Vaccinated with a primary series and booster dose'))

    fig.update_layout(
        title="Rates of COVID-19 {} by Vaccination Status and Booster Dose for Vaccine: {}".format(title_choice,
                                                                                                     vaccine),
        title_y=1,
        xaxis_title="Date",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="Black"
        )
    )
    fig.update_layout(legend=dict(yanchor="top", y=1.3, xanchor="left", x=0.55))
    fig.update_xaxes(title_text="Date (Weekly)", ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
    fig.update_yaxes(title_text="Incidence per 100000 populations", ticks="outside", tickwidth=2, tickcolor='crimson',
                     ticklen=10)
    st.plotly_chart(fig, use_container_width=True)