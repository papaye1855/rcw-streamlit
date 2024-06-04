import streamlit as st
import pandas as pd
import snowflake.connector as sc

def main():
    st.write("Demo de la connexion à snowflake depuis streamlit")

    con = sc.connect(
        account = 'xcsrvma-te06383',
        user='papayecisse',
        password = 'MonAccesSnowflake1@'
    )

    cursor = con.cursor()

    def dataPersons():
        sql = "Select * FROM rcw.persons.persons"
        df  = cursor.execute(sql).fetchall()

        return pd.DataFrame(df)
    

    donnees = dataPersons()
    st.write(donnees)
    

    









if __name__ == "__main__":
    main()