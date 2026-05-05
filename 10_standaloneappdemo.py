import streamlit as st
import pandas as pd

pop = pd.read_csv("pop.csv")

st.sidebar.header("Options")

region = st.sidebar.selectbox(
    "Choose region",
    options=pop["區域別"].unique()
)

metric = st.sidebar.selectbox(
    "Choose metric",
    ["人口數", "遷入人數", "遷出人數", "出生人數", "死亡人數"]
)

graph_type = st.sidebar.radio(
    "Choose graph type",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

st.header(f"{region} Dashboard")

filtered_pop = pop[pop["區域別"] == region]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average", int(filtered_pop[metric].mean()))

with col2:
    st.metric("Maximum", int(filtered_pop[metric].max()))

with col3:
    st.metric("Minimum", int(filtered_pop[metric].min()))

st.subheader(f"{metric} trend in {region}")

chart_data = filtered_pop.groupby("年月")[metric].mean()

if graph_type == "Line Chart":
    st.line_chart(chart_data)

elif graph_type == "Bar Chart":
    st.bar_chart(chart_data)

elif graph_type == "Area Chart":
    st.area_chart(chart_data)

with st.expander("Show filtered data"):
    st.dataframe(filtered_pop)

csv = filtered_pop.to_csv(index=False)

st.download_button(
    label="Download filtered data",
    data=csv,
    file_name=f"{region}_{metric}_data.csv",
    mime="text/csv"
)