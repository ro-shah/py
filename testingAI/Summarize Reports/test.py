# from langchain.document_loaders import UnstructuredURLLoader

# loader = UnstructuredURLLoader(urls = [
#     "https://www.cnn.com/middleeast/live-news/israel-hamas-war-gaza-news-11-22-23/index.html",
#     "https://www.cnn.com/2023/11/22/climate/uae-cop28-adnoc-fossil-fuels-expansion-climate-intl/index.html"
# ])

# data = loader.load()
# print(data[0])

# from langchain.text_splitter import RecursiveCharacterTextSplitter

# text = """Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan. 
# It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Matt Damon, and Michael Caine. 
# Set in a dystopian future where humanity is embroiled in a catastrophic blight and famine, the film follows a group of astronauts who travel through a wormhole near Saturn in search of a new home for humankind.

# Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007 and was originally set to be directed by Steven Spielberg. 
# Kip Thorne, a Caltech theoretical physicist and 2017 Nobel laureate in Physics,[4] was an executive producer, acted as a scientific consultant, and wrote a tie-in book, The Science of Interstellar. 
# Cinematographer Hoyte van Hoytema shot it on 35 mm movie film in the Panavision anamorphic format and IMAX 70 mm. Principal photography began in late 2013 and took place in Alberta, Iceland, and Los Angeles. 
# Interstellar uses extensive practical and miniature effects, and the company Double Negative created additional digital effects.

# Interstellar premiered in Los Angeles on October 26, 2014. In the United States, it was first released on film stock, expanding to venues using digital projectors. The film received generally positive reviews from critics and grossed over $677 million worldwide ($715 million after subsequent re-releases), making it the tenth-highest-grossing film of 2014. 
# It has been praised by astronomers for its scientific accuracy and portrayal of theoretical astrophysics.[5][6][7] Interstellar was nominated for five awards at the 87th Academy Awards, winning Best Visual Effects, and received numerous other accolades."""

# splitter = RecursiveCharacterTextSplitter(
#     separators = ["\n\n", "\n", "."],
#     chunk_size = 200,
#     chunk_overlap = 0
# )

# chunks = splitter.split_text(text)

# for chunk in chunks:
#     print(chunk + "\n")

import pandas as pd

pd.set_option("display.max_colwidth", 100)

df = pd.read_csv("C:\Users\ronil\Desktop\Programming\Summarize Reports\sample_text.csv")
print(len(df))