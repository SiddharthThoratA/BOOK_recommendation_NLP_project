import streamlit as st
import pandas as pd
import pickle
import requests

def featch_poster(books_id):
    response=requests.get("https://www.googleapis.com/books/v1/volumes?q=" + books['Title'][books_id])
    data = response.json()
    link = data['items'][0].get('volumeInfo',{}).get('imageLinks',{}).get('thumbnail')
    return link


def recommend(book):
  book_index = books[books['Title'] == book].index[0]
  distances = similarity[book_index]
  books_lists = sorted(list(enumerate(distances)),reverse =True,key = lambda x:x[1])[1:6]

  recommended_books = []
  recommended_books_posters = []
  for i in books_lists:
      book_id = books.iloc[i[0]].Book_Id

      recommended_books.append(books.iloc[i[0]].Title)
      recommended_books_posters.append(featch_poster(book_id))
  return recommended_books,recommended_books_posters



books_dict = pickle.load(open('books.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

books = pd.DataFrame(books_dict)

st.title('Books Recommendation System')

selected_book_name = st.selectbox('Which Book would you like to read?', books['Title'].values)

if st.button('Recommend'):
    name, posters = recommend(selected_book_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])