def summary_stats(df):
    return {
        "total": len(df),
        "avg": df["Satisfaction"].mean(),
        "top": df["Preferred_Tool"].mode()[0]
    }