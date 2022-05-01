import pandas as pd
import streamlit as st

from plots import plot_daily_deaths, plot_daily_vaccines, plot_daily_deaths_vaccines, plot_overall_deaths_vaccines, \
    plot_variant_daily_deaths_vaccines


@st.cache
def load_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/us_covid19_vaccine_cases_deaths_daily_count_variant.csv")
    data["date"] = pd.to_datetime(data["date"]).dt.date
    return data


@st.cache
def get_all_states(df):
    return df["Province_State"].unique().tolist()


@st.cache
def get_all_variants(df):
    return df["Variant"].unique().tolist()


def main():
    st.markdown("# Covid-19 Deaths and Vaccine Data")
    st.write("This app shows different visualizations for Covid-19 deaths and vaccine data")

    option = st.sidebar.selectbox("Plots",
                                  options=["Introduction", "US States - Daily Deaths", "US States - Daily Vaccines",
                                           "US State - Daily Deaths and Vaccines",
                                           "US State - Overall Deaths and Vaccines", "US State - Variant"], index=0)
    covid_data = load_data()
    all_states = get_all_states(covid_data)
    all_variants = get_all_variants(covid_data)

    if option == "Introduction":
        st.write(covid_data.head(10))
    elif option == "US States - Daily Deaths":
        states = st.multiselect("Choose state/s", options=all_states, default=["California", "New York"], key="deaths")
        start_date, end_date = st.slider("Date", value=(covid_data["date"][0], covid_data["date"][len(covid_data) - 1]),
                                         key="deaths")
        plot_daily_deaths(covid_data, start_date, end_date, states)
    elif option == "US States - Daily Vaccines":
        states = st.multiselect("Choose state/s", options=all_states, default=["California", "New York"],
                                key="vaccines")
        start_date, end_date = st.slider("Date", value=(covid_data["date"][0], covid_data["date"][len(covid_data) - 1]),
                                         key="vaccines")
        plot_daily_vaccines(covid_data, start_date, end_date, states)
    elif option == "US State - Daily Deaths and Vaccines":
        min_date, max_date = covid_data["date"][0], covid_data["date"][len(covid_data) - 1]
        state = st.selectbox("Choose state", options=all_states, index=0, key="deaths_vaccines")
        start_date, end_date = st.slider("Dates", min_value=min_date, max_value=max_date, value=(min_date, max_date),
                                         key="deaths_vaccines")
        plot_daily_deaths_vaccines(covid_data, start_date, end_date, state)
    elif option == "US State - Overall Deaths and Vaccines":
        min_date, max_date = covid_data["date"][0], covid_data["date"][len(covid_data) - 1]
        state = st.selectbox("Choose state", options=all_states, index=0, key="overall_deaths_vaccines")
        start_date, end_date = st.slider("Dates", min_value=min_date, max_value=max_date, value=(min_date, max_date),
                                         key="overall_deaths_vaccines")
        plot_overall_deaths_vaccines(covid_data, start_date, end_date, state)
    elif option == "US State - Variant":
        state = st.selectbox("Choose state", options=all_states, index=5)
        variant = st.selectbox("Variant", options=all_variants, index=2)
        plot_variant_daily_deaths_vaccines(covid_data, state, variant)


if __name__ == "__main__":
    main()
