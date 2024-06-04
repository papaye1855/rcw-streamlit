import streamlit as st
import snowflake.connector as sc
import pandas as pd

def main():
    st.write("Affichage des données avec le nom des colonnes")

    try:
        con = sc.connect(
            account = 'xcsrvma-te06383',
            user='papayecisse',
            password = 'MonAccesSnowflake1@'
        )
        if con is None:
            st.warning("Attention des informations sont incorrect")

        cursor = con.cursor()

        def dataPersons():
            sql = "Select * FROM rcw.persons.persons"
            cursor.execute(sql)
            columns_names = []
            for colonne in cursor.description:
                columns_names.append(colonne[0])
            data = cursor.fetchall()
            #columns_names = [colonne[0] for colonne in cursor.description]
            
            df = pd.DataFrame(data,columns=columns_names)
            return df

            
        
        donnees = dataPersons()

        st.write(donnees)
        


    except:
        st.warning("Attention des informations sont incorrect")



if __name__ == "__main__":
    main()
