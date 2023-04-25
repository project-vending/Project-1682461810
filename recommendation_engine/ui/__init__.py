python
import streamlit as st
import pandas as pd
from src.recommender import Recommender

def main():
    st.title("Recommended Items")

    # Load user data
    user_data_file = "data/user_data.csv"
    user_data = pd.read_csv(user_data_file)

    # Load item data
    item_data_file = "data/item_data.csv"
    item_data = pd.read_csv(item_data_file)

    # Create an instance of the recommender
    recommender = Recommender(user_data, item_data)

    # Get recommendations for the current user
    current_user = 123
    recommendations = recommender.get_recommendations(current_user)

    # Display the recommendations
    st.write(recommendations)

if __name__ == "__main__":
    main()
