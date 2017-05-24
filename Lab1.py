from scipy_setup import *

df=pd.read_csv("all.csv", header=None, names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'])
df.head()

df = df[df.year.notnull()]
df.shape
               
# Cleaning data
df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)

df.rating.hist(bins=30)
plt.show()
