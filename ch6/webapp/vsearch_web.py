from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import find_letters
from DBcm import UseDatabase, ConnError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread

"""Search for letters for the web using flask.
   Includes logging capabilities.
"""

# Flask var
app = Flask(__name__)

# Stores MySQL connection details into Flasks internals
app.config['dbconfig'] = {'host': 'beeferikson.mysql.pythonanywhere-services.com',
                          'user': 'beeferikson',
                          'password': 'vsearchpasswd',
                          'database': 'beeferikson$default'}

# Secret key for using login
app.secret_key = 'holyCowSuperSecretPassword'


# Logic on viewlog.html, queries from MySQL. Must be logged in.
@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
    """Returns MySQL query from database
    """
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            # sets up the main table contents
            _SQL = """select ts, ip, phrase, letters, browser_string, results
                      from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

            # gets total queries
            _SQL = """select count(*) from log"""
            cursor.execute(_SQL)
            queries = cursor.fetchall()
            queries = queries[0][0]

            # get most used browser
            _SQL = """select browser_string, count(browser_string) as 'count'
                      from log
                      group by browser_string
                      order by count desc
                      limit 1;"""
            cursor.execute(_SQL)
            top_browser = cursor.fetchall()
            top_browser = top_browser[0][0]
    except ConnError as err:
        print('There was a problem connecting to the database: ', str(err))
    except CredentialsError as err:
        print('User credentials are incorrect: ', str(err))
    except SQLError as err:
        print('Check your query, error: ', str(err))
    except Exception as err:
        print('Something went awry: ', str(err))

    # sets titles and renders template
    titles = ['Date - Time', 'IP Address', 'Phrase Used', 'Letters Used', 'Browser', 'Results']
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,
                           total_queries=queries,
                           most_used_browser=top_browser)


# Logic on logging in - simple example. Could expand with database etc
@app.route('/login')
def login() -> str:
    """Logs user in."""
    session['logged_in'] = True
    return 'You are now logged in.'


# Logic on logging out
@app.route('/logout')
def logout() -> str:
    """Logs user out"""
    session.pop('logged_in')
    return 'You are now logged out.'


# Logic on results.html
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Logic behind post, running find_letters, logging to database,
       and passing results to results.html.
    """

    # Logs to MySQL after user submits
    @copy_current_request_context
    def log_request(req: 'Flask request', res: str) -> None:
        """Logs request and details into MySQL database.
        """

        with UseDatabase(app.config['dbconfig']) as cursor:
            # creates string with query
            _SQL = """insert into log
                      (phrase, letters, ip, browser_string, results)
                      values
                      (%s, %s, %s, %s, %s)"""

            # execute query
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    # Sets parameters to log and pushes
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(sorted(find_letters(phrase, letters)))
    try:
        # threads the query insert
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging Failed. Error: ', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_results=results,
                           the_phrase=phrase,
                           the_letters=letters)


# Logic on entry.html
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """The title page the user is greeted with.
    """

    return render_template('entry.html',
                           the_title='Search for Letters - a Flask test!')


if __name__ == '__main__':
    app.run(debug=True)
