import nltk
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc placerat leo nunc, quis dictum quam bibendum sit amet. Nulla facilisi. Quisque at varius magna, a lacinia nulla. Mauris dapibus velit dapibus, scelerisque risus at, venenatis metus. Duis iaculis nulla at libero malesuada consequat. Maecenas in risus non nibh sollicitudin feugiat. Nam sed condimentum felis. Sed sollicitudin justo dui, eget tempor diam dignissim vitae. Duis non eleifend diam, quis tincidunt lectus. Fusce ac viverra eros. Sed ullamcorper sed ante rutrum faucibus. Pellentesque hendrerit nibh turpis. Mauris fringilla at erat ac aliquet. Integer posuere condimentum leo quis rutrum. Aenean pharetra augue id faucibus sollicitudin."
words = []
clear_text = []
sentenses = nltk.sent_tokenize(text)

for i in range(len(sentenses)):
    words.append(nltk.word_tokenize(sentenses[i]))
    clear_text.append([word for word in words if not word in stopwords.words()])

def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 
    plt.axis("off")

wordcloud = WordCloud(width = 2000, 
                      height = 1500, 
                      random_state=1, 
                      background_color='black', 
                      margin=20, 
                      colormap='Pastel1', 
                      collocations=False, 
                      stopwords = text).generate(text)

wordcloud.to_file('wordcloud.png')