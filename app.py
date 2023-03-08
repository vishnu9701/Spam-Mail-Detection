import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from PIL import Image


model = pickle.load(open('spam.pkl','rb'))
v=pickle.load(open('vectorizer.pkl','rb'))
def main():
	st.title("Email Spam Classification ")
	html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;"> Enter Your Message </h2>
        </div>
        """
	
	st.markdown(html_temp,unsafe_allow_html=True)
	msg=st.text_input("Enter a text")
	if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=v.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This is Not A Spam Email")
			else:
				st.error("This is A Spam Email")
	if st.button("GitHub"):
                 st.text("Vishnu Pandey")
                 st.markdown("[GitHub Repo](#section-1)")

if __name__=='__main__':
    main()
