# 🥗 Affordable Nutrition AI Classifier

This project empowers Kenyan households to build balanced meals using local ingredients. It uses a simple AI model to classify meals as **Balanced** or **Unbalanced**, and offers smart suggestions to improve nutrition affordably.

> ⚠️ **Malnutrition is a hidden form of hunger.** This app supports **food security** by helping users plan meals that meet basic nutritional needs which is a critical step toward achieving **SDG 2: Zero Hunger**.

---

## 🚀 Features

- ✅ Classify meals based on selected ingredients
- 💡 Suggest missing food groups (carbs, protein, veg/fruit)
- 🎲 Generate random balanced meal ideas
- 📦 Uses a pre-trained Decision Tree model (`.pkl`)
- 📊 Ingredient data loaded from a local CSV file

---

## 📁 Project Structure
nutrition-classifier/ 
├── app.py 
├── decision_tree_model.pkl 
├── ingredients.csv 
├── training_meals.csv 
├── requirements.txt 
└── README.md

---

## 🛠️ Installation

1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Run the app: streamlit run app.py

Requirements:
streamlit
pandas
scikit-learn
joblib
blinker
protobuf
google
cachetools
click
toml

📊 How It Works- The app loads a pre-trained Decision Tree model from decision_tree_model.pkl.

- Ingredient data is read from ingredients.csv, which includes flags for:
- Is_Carb
- Is_Protein
- Is_Veg/Fruit
- Users select ingredients, and the app predicts whether the meal is balanced.
- If unbalanced, it suggests missing food groups.
- Users can also generate random balanced meal ideas.

💻Strealmlit deployment link

https://affordable-nutrition-ai-classifier.streamlit.app/

🌍Impact

This project supports nutrition awareness and food planning in Kenyan communities using accessible technology like mobile phones. 
It’s designed to be simple, educational, and adaptable for local datasets. By promoting balanced meals, it contributes to food security and addresses *hidden hunger* a key challenge in achieving Zero Hunger (SDG 2) and having an impact on malnutrition.

👏 Acknowledgment

Created by Felistus Mukiri
 |Food scientist|Food security enthisiast|Tech innovator|Community advocate|

 Built to empower households with smart, affordable nutrition planning.
