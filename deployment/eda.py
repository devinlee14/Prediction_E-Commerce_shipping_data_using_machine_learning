"""
Milestone 2
Nama: Devin Yaung Lee
Batch: HCK-009
// eda.py //
program ini untuk mendeploy model EDA interface.
"""

import streamlit as st
import pandas as pd

# Function to run in app.py
def run():
    st.title("Explatoratory Data Analysis")

    df = pd.read_csv("../Train.csv")

    # The first 5 data
    st.header("The first 5 data entry")
    st.table(df.head(5))

    # The last 5 data
    st.header("The last 5 data entry")
    st.table(df.tail(5))

    # Heatmap correlation
    st.header("Correlation heatmap")
    st.image("heatmap.png", caption="Figure 1")
    with st.expander("Explanation"):
        st.caption("Berdasarkan dari hasil ini dapat dikatakan ada beberapa column yang memiliki korelasi. Ada beberapa column yang memiliki korelasi sampai 30% - 40%, dan ada juga korelasi minus yang dapat dikatakan bahwa column tersebut tidak memiliki atau hampir tidak memiliki korelasi satu sama lain")

    # Histogram Distribution of Customer Rating
    st.header("Histogram Distribution of Customer Rating")
    st.image("histogram_customer_rating.png", caption="Figure 2")
    with st.expander("Explanation"):
        st.caption("Berdasarkan dari hasil data histogram, didapatkan bahwa persebaran nilai customer rating memiliki persebaran yang relatif sama besar. Hal ini ada beberapa kemungkinan data ini terbagi rata untuk pada saat data entry. Dan jika dilihat secara detail, didapatkan nilai tertinggi persebaran/distribusinya adalah rating 1 dan rating 3. Besar kemungkinan pada proses shipping ini sering terjadi problem yang membuat customer tidak merasa puas dengan pelayanan shippingnya.")

    # Distribution of Cost of the Product
    st.header("Distribution of Cost of the Product")
    st.image("distribution_.cost.png", caption="Figure 4")
    with st.expander("Explanation"):
        st.caption("> Berdasarkan dari hasil diatas didapatkan bahwa distribusi untuk cost of the product rata-rata berada dikisaran harga $250, hal ini dapat dikatakan bahwa besarnya biaya per product ini dapat dikarenakan biaya pengiriman yang mahal ataupun jarak tempuh pengiriman")