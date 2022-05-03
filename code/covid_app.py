import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

from plots import plot_daily_deaths, plot_daily_vaccines, plot_daily_deaths_vaccines, plot_overall_deaths_vaccines, \
    plot_variant_daily_deaths_vaccines, plot_adult_hospitalizations_vaccinations, \
    plot_age_group_hospitalizations_vaccinations, plot_booster_adult_hospitalizations_vaccinations, \
    plot_booster_age_group_hospitalizations_vaccinations, plot_overall_cases_vaccinations, \
    plot_age_group_cases_vaccinations, plot_vaccine_cases_vaccinations, plot_overall_cases_vaccinations_booster, \
    plot_age_group_cases_vaccinations_booster, plot_vaccine_cases_vaccinations_booster


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
def load_cases_deaths_vaccinations_data():
    data_1 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/cases_deaths_vaccinations.csv")
    data_1["Age group"] = data_1["Age group"].replace({"Dec-17": "12-17", "05-Nov": "05-11"})
    data_1["date"] = pd.to_datetime(data_1["date"]).dt.date

    data_2 = pd.read_csv(
        "https://raw.githubusercontent.com/aanchal22/DAVH_Covid-19/main/data/cases_deaths_vaccinations_booster.csv")
    data_2["age_group"] = data_2["age_group"].replace({"Dec-17": "12-17"})
    data_2["date"] = pd.to_datetime(data_2["date"]).dt.date
    return data_1, data_2


@st.cache
def get_all_states(df):
    return df["Province_State"].unique().tolist()


@st.cache
def get_all_variants(df):
    return df["Variant"].unique().tolist()


@st.cache
def get_all_age_groups_hospitalizations(df):
    return df["Age group"].unique().tolist()


@st.cache
def get_all_age_groups_cdv(df):
    return sorted(df["Age group"].unique().tolist()[:-1])[:-1]


@st.cache
def get_all_age_groups_cdvb(df):
    return sorted(df["age_group"].unique().tolist()[:-1])[:-1]


@st.cache
def get_all_vaccine_types():
    return ["Janssen", "Moderna", "Pfizer"]


def main():
    st.markdown("# Covid-19 Deaths and Vaccine Data")
    st.write("This applications shows different visualizations for Covid-19 deaths and vaccine data")

    option = st.sidebar.selectbox("Plots",
                                  options=["Introduction", "US - Cases, Deaths and Vaccines",
                                           "US - Cases, Deaths and Vaccines (Booster)",
                                           "US - Hospitalizations and Vaccines",
                                           "US - Hospitalizations and Vaccines (Booster)",
                                           "US States - Daily Deaths", "US States - Daily Vaccines",
                                           "US State - Daily Deaths and Vaccines",
                                           "US State - Overall Deaths and Vaccines", "US State - Variant",
                                           "Thank you!"
                                           ], index=0)
    covid_data = load_data()
    all_states = get_all_states(covid_data)
    all_variants = get_all_variants(covid_data)

    cas_dth_vac_data_1, cas_dth_vac_data_2 = load_cases_deaths_vaccinations_data()
    age_groups_cdv = get_all_age_groups_cdv(cas_dth_vac_data_1)
    age_groups_cdvb = get_all_age_groups_cdvb(cas_dth_vac_data_2)
    vacc_types = get_all_vaccine_types()

    hosp_vac_data_1, hosp_vac_data_2, hosp_vac_data_3, hosp_vac_data_4 = load_hospitalizations_vaccinations_data()
    age_groups_hosp = get_all_age_groups_hospitalizations(hosp_vac_data_2)

    if option == "Introduction":
        st.write("")
        st.write("")
        st.write("The following are the visualizations that are present in the application:")
        st.write("- Cases and Deaths w.r.t vaccinations across the US (country level)")
        st.write("- Hospitalizations w.r.t vaccinations across the US (country level)")
        st.write("- Cases and Deaths w.r.t vaccinations for all states in the US")
        st.write("- Cases and Deaths w.r.t vaccinations during different variants of COVID-19 for all states in the US")
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
        choice = st.radio("Choose age-adjusted or not", options=["Age adjusted", "Age group"], index=0,
                          key="hosp_vacc")
        if choice == "Age adjusted":
            plot_adult_hospitalizations_vaccinations(hosp_vac_data_1)
        else:
            age_group = st.selectbox("Choose age group", options=age_groups_hosp, index=1,
                                     key="age_group_hospitalizations_vaccines")
            plot_age_group_hospitalizations_vaccinations(hosp_vac_data_2, age_group)
    elif option == "US - Hospitalizations and Vaccines (Booster)":
        choice = st.radio("Choose age-adjusted or not", options=["Age adjusted", "Age group"], index=0,
                          key="hosp_vacc_booster")
        if choice == "Age adjusted":
            plot_booster_adult_hospitalizations_vaccinations(hosp_vac_data_3)
        else:
            age_group = st.selectbox("Choose age group", options=age_groups_hosp, index=1,
                                     key="age_group_hospitalizations_vaccines_booster")
            plot_booster_age_group_hospitalizations_vaccinations(hosp_vac_data_4, age_group)
    elif option == "US - Cases, Deaths and Vaccines":
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            main_choice = st.radio("Plot", options=["Overall", "Age group", "Vaccine type"], index=0, key="cdvb_choice")
        with col2:
            cd_choice = st.radio("Cases/Deaths", options=["Cases", "Deaths"], index=0,
                                 key="age_group_cases_deaths_vaccines")

        if main_choice == "Overall":
            plot_overall_cases_vaccinations(cas_dth_vac_data_1, cd_choice)
        elif main_choice == "Age group":
            age_group = st.selectbox("Choose age group", options=age_groups_cdv, index=2,
                                     key="age_group_cases_deaths_vaccines_booster")
            plot_age_group_cases_vaccinations(cas_dth_vac_data_1, cd_choice, age_group)
        elif main_choice == "Vaccine type":
            plot_vaccine_cases_vaccinations(cas_dth_vac_data_1, cd_choice)
    elif option == "US - Cases, Deaths and Vaccines (Booster)":
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            main_choice = st.radio("Plot", options=["Overall", "Age group", "Vaccine type"], index=0, key="cdvb_choice")
        with col2:
            cd_choice = st.radio("Cases/Deaths", options=["Cases", "Deaths"], index=0,
                                 key="age_group_cases_deaths_vaccines")

        if main_choice == "Overall":
            plot_overall_cases_vaccinations_booster(cas_dth_vac_data_2, cd_choice)
        elif main_choice == "Age group":
            age_group = st.selectbox("Choose age group", options=age_groups_cdvb, index=2,
                                     key="age_group_cases_deaths_vaccines_booster")
            plot_age_group_cases_vaccinations_booster(cas_dth_vac_data_2, cd_choice, age_group)
        elif main_choice == "Vaccine type":
            vaccine = st.selectbox("Choose vaccine type", options=vacc_types, index=2,
                                   key="vac_cases_deaths_vaccines_booster")
            plot_vaccine_cases_vaccinations_booster(cas_dth_vac_data_2, cd_choice, vaccine)
    elif option == "Thank you!":
        st.write("")
        st.markdown("<h1 style='text-align: center; color: #636EFA;'>Thank you!</h1>", unsafe_allow_html=True)
        st.snow()
        st.balloons()


if __name__ == "__main__":
    main()
