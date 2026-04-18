import plotly.express as px

def tool_chart(df):
    return px.bar(df["Preferred_Tool"].value_counts(),
                  title="Tool Preference")

def satisfaction_chart(df):
    return px.histogram(df, x="Satisfaction", color="Gender")