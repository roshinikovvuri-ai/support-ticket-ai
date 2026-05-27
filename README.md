# 🤖 AI Customer Support Ticket Classification System

An end-to-end Natural Language Processing (NLP) project that automatically classifies customer support tickets into relevant categories such as **Billing, Technical Issues, Product Enquiry, Cancellation Requests**, etc.

This system was built using a complete ML pipeline and later upgraded from a traditional TF-IDF model to a modern **BERT-based semantic understanding model** for improved accuracy.



# 📌 Project Objective

Customer support teams receive thousands of tickets daily. Manually categorizing them is:
- time-consuming
- inefficient
- error-prone

This project automates ticket classification using Machine Learning and NLP.


# ⚙️ Key Features

- 📊 Automatic ticket classification
- 🧠 NLP-based text understanding
- ⚡ Real-time predictions using Streamlit UI
- 🔄 Model upgrade from TF-IDF → BERT embeddings
- 🐳 Docker containerization support
- 📂 CSV-based dataset training
- 💬 User-friendly interface


# 🧠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Sentence Transformers (BERT)
- PyTorch
- Docker



# 🏗️ System Architecture

User Input
    ↓
Streamlit UI
    ↓
Text Preprocessing
    ↓
BERT Embedding Model
    ↓
ML Classifier (Logistic Regression)
    ↓
Predicted Category
    ↓
UI Output


# 🔄 Model Evolution (VERY IMPORTANT)

## ❌ Initial Approach: TF-IDF Vectorizer

Initially, the model used:

- TF-IDF Vectorizer
- Logistic Regression

### Limitations:
- Only keyword-based understanding
- Poor semantic understanding
- Incorrect predictions for similar meaning sentences

Example:

"Application crashes" → Billing Enquiry ❌


## ✅ Improved Approach: BERT Embeddings

The model was upgraded to:

- Sentence Transformers (MiniLM BERT model)
- Semantic embeddings
- Logistic Regression classifier on embeddings

### Improvements:
- Understands meaning instead of keywords
- Better generalization
- More accurate classification

Example:

"Application crashes during login" → Technical Issue ✅


# 📊 Dataset

The dataset contains customer support tickets with:
- Ticket text
- Category labels

Example:
| Ticket Text | Category |
|------------|----------|
| Payment failed | Billing |
| App crashes | Technical Issue |
| Need refund | Cancellation |


# 🚀 How to Run the Project

## 1️⃣ Clone Repository

git clone https://github.com/your-username/ticket-classification-ai.git
cd ticket-classification-ai


## 2️⃣ Create Virtual Environment (Recommended)


python -m venv venv
venv\Scripts\activate   # Windows


## 3️⃣ Install Dependencies


pip install -r requirements.txt


## 4️⃣ Run Streamlit App


streamlit run app/main.py



# 🐳 Run with Docker

## Build Image

docker build -t ticket-ai .


## Run Container

docker run -p 8501:8501 ticket-ai


# 💡 Example Usage

Input:

Application crashes during login

Output:

Predicted Category: Technical Issue


# 📁 Project Structure

ticket-classification-ai/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── utils.py
│
├── data/
│   └── tickets.csv
│
├── requirements.txt
├── Dockerfile
├── README.md


# 🔥 Key Learnings

- NLP text preprocessing
- TF-IDF vs BERT comparison
- Sentence embeddings
- Logistic Regression classification
- Streamlit UI development
- Model deployment using Docker
- End-to-end ML pipeline design


# 🚀 Future Improvements

- Replace Logistic Regression with Deep Learning classifier
- Add confidence score for predictions
- Integrate LLM (ChatGPT / Gemini API)
- Auto-response generation
- Ticket priority prediction
- Cloud deployment (AWS / Azure)


# 👨‍💻 Author

Built as an end-to-end AI/ML project demonstrating real-world NLP workflow and production-style deployment techniques.


# ⭐ Project Highlights

✔ Real-world NLP use case  
✔ Upgraded from TF-IDF → BERT  
✔ Streamlit UI  
✔ Docker support  
✔ End-to-end ML pipeline  
✔ Production-style structure  

