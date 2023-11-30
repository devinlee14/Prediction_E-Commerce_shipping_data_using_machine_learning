"""
Milestone 2
Nama: Devin Yaung Lee
Batch: HCK-009
program ini untuk mendeploy model
"""

import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label="Select Page:", options=["Home Page", "Exploratory Data Analysis", "Predict On Time"])

if page == "Home Page":
    st.title("Home Page")
    st.write('')
    st.write("Milestone 2")
    st.write("Name  : Devin Yaung Lee")
    st.write("Batch : HCK-009")
    st.write("Aplikasi ini memiliki tujuan utama  untuk menampilkan hasil untuk memprediksi apakah pengiriman product berdasarkan parameter-parameter tententu, pengiriman on time atau tidak.")
    st.write('')
    st.write('')
    st.write('')

    with st.expander("Background Information"):
        st.caption("Dataset ini membahas tentang E-Commerce Shipping Data. Dimana data ini membahas tentang bagaimana proses pegiriman data yang berbeda-beda, dimana ada jalur darat, jalur laut, dan jalur udara. Dari ketiga hal ini akan dilihat juga bagaimana rating dari tiap-tiap proses jalur, dan tujuan utama pembuatan model ini adalah untuk mengetahui apakah dari parameter-parameter column ini, pengiriman on time atau tidak.")
    with st.expander("Conclusion"):
        st.caption("""
        - Didapatkan bahwa pada saat melalakukan pengecheckan nilai skewness, column prior_purchases dan discount_offered didapatkan bahwa nilai skewness pada column tersebut mengalami skew, hal ini kemungkinan dikarenakan terdapat outliers pada kedua columns tersebut. Maka perlu dilakukan handling outliers. Pada kasus ini jika tidak ingin menghilangkan data, maka handling outliers yang paling cocok adalah dengan menggunakan winsorizer yang nanti akan dilakukan di proses selanjutnya.
        -  Berdasarkan dari hasil visualisasi didapatkan bahwa ada keterdapatan outliers pada beberapa column tertentu, dan dilakukan handling outliers menggunakan winsorizer
        - Berdasarkan dari analisa model, dari baseline model, hyperparameter tuning, dan boosting, didapatkan bahwa model terbaik adalah menggunakan model SVM.
        """)

elif page == "Exploratory Data Analysis":
    eda.run() # Calls the run function from eda

else:
    model.run() # Calls the run function from model