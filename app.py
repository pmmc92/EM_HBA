
import pickle
import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
from PIL import Image

pickle_in = open('regressor.pkl', 'rb') 
regression = pickle.load(pickle_in)

def predict_ARR(Idade, Sexo, tipo, Dias, EDSS, tx_ant, Surtos_base, RAM, farmaco):

       Farmaco_AG = 0
       Farmaco_DMF = 0
       Farmaco_Fingolimod = 0
       Farmaco_Interferao = 0
       Farmaco_Peginterferao = 0
       Farmaco_Teriflunomida = 0
       Tipo_EM_EMPP = 0
       Tipo_EM_EMSP = 0
       Tipo_EM_EMSR = 0
       Sexo_F = 0
       Sexo_M = 0
       RAM = 0

       if Sexo == "Masculino":
              Sexo_M = 1
       else: 
              Sexo_F = 1
       
       if tipo == "EMSR":
              Tipo_EM_EMSR = 1
       elif tipo == "EMSP":
              Tipo_EM_EMSP = 1
       else:
              Tipo_EM_EMPP = 1
       
       if farmaco == "Fingolimod":
              Farmaco_Fingolimod = 1
       elif farmaco == "Interferão":
              Farmaco_Interferao = 1
       elif farmaco == "Teriflunomida":
              Farmaco_Teriflunomida = 1
       elif farmaco == "Fumarato de Dimetilo":
              Farmaco_DMF = 1
       elif farmaco == "Acetato de Glatirâmero":
              Farmaco_AG = 1
       else:
              Farmaco_Peginterferao = 1

       if RAM == "Sim":
              RAM = 1
       
       df = pd.DataFrame({"Idade" : Idade, "Dias" : Dias, "EDSS" : EDSS, "tx_ant" : tx_ant, "Surtos_base" : Surtos_base, "RAM" : RAM, "Farmaco_AG" : Farmaco_AG,
       "Farmaco_DMF" : Farmaco_DMF, "Farmaco_Fingolimod" : Farmaco_Fingolimod, "Farmaco_Interferao" : Farmaco_Interferao,
       "Farmaco_Peginterferao" : Farmaco_Peginterferao, "Farmaco_Teriflunomida" : Farmaco_Teriflunomida, "Tipo_EM_EMPP" : Tipo_EM_EMPP,
       "Tipo_EM_EMSP" : Tipo_EM_EMSP, "Tipo_EM_EMSR" : Tipo_EM_EMSR, "Sexo_F" : Sexo_F, "Sexo_M" : Sexo_M}, index=[0])

       prediction = regression.predict(df)
       
       return prediction

def main():
       
       image = Image.open('logo.jpg')
       st.image(image)

       st.title("Previsão da Taxa Anual de Surto em doentes com EM")

       Idade = st.slider("Idade", 15,80,1)
       Sexo = st.radio("Sexo",("Masculino","Feminino"))
       tipo = st.radio("Forma da doença",("EMSR","EMSP","EMPP"))
       Dias = st.number_input("Número de Dias de Tratamento")
       EDSS = st.number_input("EDSS")
       tx_ant = st.slider("Número de terapêuticas anteriores",0,4,1)
       Surtos_base = st.slider("Número de surtos nos últimos dois anos",0,4,1)
       RAM = st.radio("Teve RAM no último tratamento?",("Sim","Não"))
       farmaco = st.selectbox("Fármaco proposto",("Fingolimod","Interferão","Teriflunomida","Fumarato de Dimetilo","Acetato de Glatirâmero"))

       if st.button("Prever ARR"): 
              result = predict_ARR(Idade, Sexo, tipo, Dias, EDSS, tx_ant, Surtos_base, RAM, farmaco) 
              st.success('A probabilidade de surto a um ano é {}'.format(result))

if __name__=='__main__': 
    main()
        

