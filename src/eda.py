import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("../data/poll_data.csv")

sns.set_style("darkgrid")

print("📊 Dataset Loaded:", df.shape)

# ---------------------------
# 1. TOOL PREFERENCE
# ---------------------------
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Preferred_Tool", palette="viridis")
plt.title("🔥 Preferred Tools Distribution")
plt.xticks(rotation=30)
plt.show()

# ---------------------------
# 2. SATISFACTION
# ---------------------------
plt.figure(figsize=(6,4))
sns.histplot(df["Satisfaction"], bins=5, kde=True, color="skyblue")
plt.title("📊 Satisfaction Distribution")
plt.show()

# ---------------------------
# 3. REGION ANALYSIS
# ---------------------------
plt.figure(figsize=(7,4))
sns.countplot(data=df, x="Region", palette="coolwarm")
plt.title("🌍 Region-wise Responses")
plt.show()

# ---------------------------
# 4. GENDER DISTRIBUTION
# ---------------------------
plt.figure(figsize=(5,5))
df["Gender"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("👥 Gender Distribution")
plt.ylabel("")
plt.show()

# ---------------------------
# 5. WORD CLOUD (FEEDBACK)
# ---------------------------
text = " ".join(df["Feedback"])

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("💬 Feedback Insights")
plt.show()