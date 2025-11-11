import pandas as pd
import streamlit as st
import joblib
import random
import os

# --- 1. Load the Pre-trained Model ---
@st.cache_resource
def load_model():
    try:
        return joblib.load('decision_tree_model.pkl')
    except FileNotFoundError:
        st.error("Model file not found. Make sure 'decision_tree_model.pkl' is in the same folder.")
        return None

# --- 2. Load Ingredient Data ---
@st.cache_data
def load_ingredient_data():
    for filename in os.listdir():
        if filename.startswith("ingredients") and filename.endswith(".csv"):
            try:
                df = pd.read_csv(filename)
                df.columns = ['IngredientName', 'Is_Carb', 'Is_Protein', 'Is_Veg']
                return df
            except Exception as e:
                st.error(f"Error loading '{filename}': {e}")
                return None
    st.error("No valid 'ingredients.csv' file found.")
    return None

# --- 3. Streamlit Interface ---
st.set_page_config(page_title="Affordable Nutrition AI", layout="wide")
st.title("🥗 Affordable Nutrition AI Classifier")
st.markdown("Empowering Kenyan households to build balanced meals using local ingredients.")

model = load_model()
df_ingredients = load_ingredient_data()

if model is not None and df_ingredients is not None:
    st.header("1️⃣ Classify Your Meal")
    ingredient_list = df_ingredients['IngredientName'].tolist()
    selected_ingredients = st.multiselect("Select your meal ingredients:", options=ingredient_list)

    if st.button("Classify Meal"):
        if not selected_ingredients:
            st.warning("Please select at least one ingredient.")
        else:
            meal_df = df_ingredients[df_ingredients['IngredientName'].isin(selected_ingredients)]
            meal_vector = [
                int(meal_df['Is_Carb'].any()),
                int(meal_df['Is_Protein'].any()),
                int(meal_df['Is_Veg'].any())
            ]
            prediction = model.predict([meal_vector])[0]

            st.subheader("📊 Classification Result:")
            if prediction == 1:
                st.success("✅ This meal is BALANCED!")
                st.balloons()
            else:
                st.error("❌ This meal is UNBALANCED.")

            st.markdown("---")
            st.subheader("🧪 Meal Profile")
            col1, col2, col3 = st.columns(3)
            col1.metric("Carbohydrate", "✔️ YES" if meal_vector[0] else "❌ NO")
            col2.metric("Protein", "✔️ YES" if meal_vector[1] else "❌ NO")
            col3.metric("Vegetable/Fruit", "✔️ YES" if meal_vector[2] else "❌ NO")

            if prediction == 0:
                st.info("Here's how you can balance this meal:")
                for i, (label, col) in enumerate(zip(["Carbohydrate", "Protein", "Vegetable/Fruit"], ['Is_Carb', 'Is_Protein', 'Is_Veg'])):
                    if meal_vector[i] == 0:
                        st.warning(f"Missing **{label}**.")
                        suggestions = df_ingredients[df_ingredients[col] == 1]['IngredientName'].sample(3).tolist()
                        st.write(f"Try adding: **{suggestions[0]}**, **{suggestions[1]}**, or **{suggestions[2]}**")

    st.divider()
    st.header("2️⃣ Need a Balanced Meal Idea?")
    if st.button("🎲 Suggest a Meal!"):
        try:
            carb = random.choice(df_ingredients[df_ingredients['Is_Carb'] == 1]['IngredientName'].tolist())
            protein = random.choice(df_ingredients[df_ingredients['Is_Protein'] == 1]['IngredientName'].tolist())
            veg = random.choice(df_ingredients[df_ingredients['Is_Veg'] == 1]['IngredientName'].tolist())
            st.success(f"Here's a balanced idea: **{carb}** + **{protein}** + **{veg}**")
        except Exception as e:
            st.error("Could not generate a meal. Make sure your ingredients file has items for each category.")