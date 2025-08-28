import streamlit as st
from LANGCHAIN_HELPER import generate_restaurant_name_and_items

st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍴")

st.title("🍴 Restaurant Name & Menu Generator")

# Sidebar for cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a cuisine",
    ("Indian", "Italian", "Mexican", "Arabian", "American", "Chinese", "Thai")
)

# Generate restaurant name + menu
if cuisine:
    response = generate_restaurant_name_and_items(cuisine)

    # Show Restaurant Name
    st.header(f"🏠 {response['restaurant_name']}")

    # Show Menu
    st.subheader("📋 Menu Items")
    for item in response['menu_items']:
        st.write(f"- {item}")
