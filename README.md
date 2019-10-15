## Description
Prolific News Highlights is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source.Clicking a news link will redirect the user to read it fully from the news source. It consumes data from the News API.
## Author
Rita  Mwaura
## user story
1 user should be able to see sources on home page of application
2 see all news article and when was created
3 image description  and time news article was created
4 click on the article and read  the whole article on the sources website
## installation requirement
1 python3.7
2 pip
3 virtualenv
## How to run the application 
1 Creating the virtual environment

  $ python3.7 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python 
2 Installing Flask and other Modules

  $ python3.7 -m pip install Flask
  $ python3.7 -m pip install Flask-Bootstrap
  $ python3.7 -m pip install Flask-Script
3 Setting up the API Key

  To be able to gather article info from the News API you will need an API Key.
  
  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it: 
  
          export NEWS_API_KEY='<Your-Api-Key>'
          python3.7 manage.py server
          
  * Insert the API Key you received from News Api where <Your-Api-Key> is.
4 To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh
## Testing the application
$ python3.7 manage.py tests
## Technologies used 
python 3.7
flask
## License
MIT ©2019 Rita mwaura
