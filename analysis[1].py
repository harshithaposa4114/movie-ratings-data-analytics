from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).parent
OUT=HERE/"outputs"; OUT.mkdir(exist_ok=True)
df=pd.read_csv(HERE/"movies.csv").drop_duplicates().dropna()
genre=df.groupby("Genre")["Rating"].agg(["mean","count"]).sort_values("mean",ascending=False)
year=df.groupby("ReleaseYear").size()
print("\\nAverage rating and movie count by genre:\\n",genre.round(2))
print("\\nMovies with most votes:\\n",df.nlargest(5,"Votes")[["Title","Genre","Rating","Votes"]].to_string(index=False))
print("\\nMovie count by release year:\\n",year)
genre.to_csv(OUT/"genre_rating_summary.csv")
plt.figure(figsize=(7,4)); genre["mean"].plot(kind="bar"); plt.ylabel("Average rating"); plt.title("Average Rating by Genre"); plt.tight_layout(); plt.savefig(OUT/"rating_by_genre.png"); plt.close()
