# WEB SCRAPER
## About
This project is about the creation of a function that takes a website address, and a number of webpages as input
arguments and then goes all over the website saving every new article on the page to a separate.txt on your computer.
## Description
Most of the time, the reason why people create parse-and-scrape programs is to automate the routine tasks of retrieving
large data from a website. For example, every machine learning task requires some train data. Let's imagine you're doing
research based on the recent science news: 
* For that research, you'll need to have the most recent articles with the type "News" that are posted on the Nature
  journal website. Each article should be saved to a separate .txt file named after the article's title.
* Then improve the program by making it parse multiple website pages. To make it even more useful, 
  let's also implement the opportunity to parse several kinds of articles at once.  
## Objectives

1. * Send an HTTP request to a URL received from the user input.
   * Print out the Quote content extracted from the `json` body response.
   * Print out the `Invalid quote resource!` error message if there's no quote or something goes wrong.
2. * Feed your program a link to a movie description such as `https://www.imdb.com/title/tt0080684`.
   * Inspect the page and find out how the movie's title and description are stored in the source.
   * Download the webpage content, parse it using beautifulsoup library, and print out the movie's original title and
     description in a dictionary.
   * If the received page doesn't have a movie description or is not an IMDB resource, the program should respond with
     the `Invalid movie page!` message.
3. * Retrieve the non decoded page's source code from a user input URL and save it to the `source.html` in binary mode.
   * Print the `Content saved.` message if everything is OK, and if something is wrong print the message
     `The URL returned X` where `X` is the received error code
4. * Take the `https://www.nature.com/nature/articles` URL and then goes over the page source code searching for
    articles.
   * Detect the article type and the link to view the article tags and their attributes
   * Save the contents of each article of the type "News" to a separate file named `%article_title%.txt`. Replace
    the whitespaces with underscores and remove punctuation marks in the filename (`str.maketrans` and
      `string.punctuation` will be useful for this). Also, strip all trailing whitespaces in the article body and title.
5. * Improve your code so that the function can take two parameters from the user input: the number of pages 
     (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of
     pages on which the program should look for the articles.
   * Create a directory named Page_N (where N is the page number) for each page in the desired category, and put all
     the articles that are found on the page with the matched type to this directory.
   * If there's no articles on the page, your program should still create a folder, but in this case the folder 
     would be empty.