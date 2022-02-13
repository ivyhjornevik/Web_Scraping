from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

rev_file = open("amazon_reviews.txt","r") 
 
comment_words = ''
stopwords = set(STOPWORDS)
 
for review in rev_file:
     
    # typecaste each review to string
    review = str(review)
    #print(review)
 
    #split reviews into individual words
    tokens = review.split()
    #print(tokens)
     
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    
    comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
    background_color ='black',
    colormap = "Blues",
    stopwords = stopwords,
    min_font_size = 10).generate(comment_words) 

plt.figure(figsize = (8, 8), facecolor = 'None')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
    
plt.savefig(r"C:\Users\ivyhj\Python Scripts\Amazon Yoga Mat Reviews\review_cloud.jpg")
plt.show()    
 
