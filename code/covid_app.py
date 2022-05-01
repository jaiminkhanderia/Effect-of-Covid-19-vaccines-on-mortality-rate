import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

from plots import plot_daily_deaths, plot_daily_vaccines, plot_daily_deaths_vaccines, plot_overall_deaths_vaccines, \
    plot_variant_daily_deaths_vaccines, plot_adult_hospitalizations_vaccinations, \
    plot_age_group_hospitalizations_vaccinations, plot_booster_adult_hospitalizations_vaccinations, \
    plot_booster_age_group_hospitalizations_vaccinations


@st.cache
def load_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/us_covid19_vaccine_cases_deaths_daily_count_variant.csv")
    data["date"] = pd.to_datetime(data["date"]).dt.date
    return data


@st.cache
def load_hospitalizations_vaccinations_data():
    data_1 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/adults_hospitalizations_vaccinations.csv",
        header=2)
    data_2 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/age_group_hospitalizations_vaccinations.csv",
        header=2
    )
    data_3 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/adults_hospitalizations_vaccinations_booster.csv",
        header=2)
    data_4 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/age_group_hospitalizations_vaccinations_booster.csv",
        header=2)
    return data_1, data_2, data_3, data_4


@st.cache
def get_all_states(df):
    return df["Province_State"].unique().tolist()


@st.cache
def get_all_variants(df):
    return df["Variant"].unique().tolist()


@st.cache
def get_all_age_groups(df):
    return df["Age group"].unique().tolist()


def main():
    st.markdown("# Covid-19 Deaths and Vaccine Data")
    st.write("This app shows different visualizations for Covid-19 deaths and vaccine data")

    option = st.sidebar.selectbox("Plots",
                                  options=["Introduction", "US States - Daily Deaths", "US States - Daily Vaccines",
                                           "US State - Daily Deaths and Vaccines",
                                           "US State - Overall Deaths and Vaccines", "US State - Variant",
                                           "US - Hospitalizations and Vaccines",
                                           "US - Hospitalizations and Vaccines (Booster)"], index=0)
    covid_data = load_data()
    all_states = get_all_states(covid_data)
    all_variants = get_all_variants(covid_data)

    hosp_vac_data_1, hosp_vac_data_2, hosp_vac_data_3, hosp_vac_data_4 = load_hospitalizations_vaccinations_data()
    age_groups = get_all_age_groups(hosp_vac_data_2)

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
        state = st.selectbox("Choose state", options=all_states, index=5, key="deaths_vaccines")
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
        variant = st.selectbox("Variant", options=all_variants, index=1)
        plot_variant_daily_deaths_vaccines(covid_data, state, variant)
    elif option == "US - Hospitalizations and Vaccines":
        option = st.radio("Choose age-adjusted or not", options=["Age adjusted", "Age group"], index=0,
                          key="hosp_vacc")
        if option == "Age adjusted":
            plot_adult_hospitalizations_vaccinations(hosp_vac_data_1)
        else:
            age_group = st.selectbox("Choose age group", options=age_groups, index=1,
                                     key="age_group_hospitalizations_vaccines")
            plot_age_group_hospitalizations_vaccinations(hosp_vac_data_2, age_group)
    elif option == "US - Hospitalizations and Vaccines (Booster)":
        option = st.radio("Choose age-adjusted or not", options=["Age adjusted", "Age group"], index=0,
                          key="hosp_vacc_booster")
        if option == "Age adjusted":
            plot_booster_adult_hospitalizations_vaccinations(hosp_vac_data_3)
        else:
            age_group = st.selectbox("Choose age group", options=age_groups, index=1,
                                     key="age_group_hospitalizations_vaccines_booster")
            plot_booster_age_group_hospitalizations_vaccinations(hosp_vac_data_4, age_group)


if __name__ == "__main__":
    main()
