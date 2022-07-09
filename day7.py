Hangman game completed

#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
    
    
    
    
    
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    hangman_art.py
    
    
    
    
    
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    

 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------

hangman_words.py
word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]







--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Packager files
poetry.lock

[[package]]
name = "aiohttp"
version = "3.8.1"
description = "Async http client/server framework (asyncio)"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
aiosignal = ">=1.1.2"
async-timeout = ">=4.0.0a3,<5.0"
attrs = ">=17.3.0"
charset-normalizer = ">=2.0,<3.0"
frozenlist = ">=1.1.1"
multidict = ">=4.5,<7.0"
yarl = ">=1.0,<2.0"

[package.extras]
speedups = ["aiodns", "brotli", "cchardet"]

[[package]]
name = "aiosignal"
version = "1.2.0"
description = "aiosignal: a list of registered asynchronous callbacks"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
frozenlist = ">=1.1.0"

[[package]]
name = "async-timeout"
version = "4.0.2"
description = "Timeout context manager for asyncio programs"
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "attrs"
version = "21.4.0"
description = "Classes Without Boilerplate"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[package.extras]
dev = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins", "zope.interface", "furo", "sphinx", "sphinx-notfound-page", "pre-commit", "cloudpickle"]
docs = ["furo", "sphinx", "zope.interface", "sphinx-notfound-page"]
tests = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins", "zope.interface", "cloudpickle"]
tests_no_zope = ["coverage[toml] (>=5.0.2)", "hypothesis", "pympler", "pytest (>=4.3.0)", "six", "mypy", "pytest-mypy-plugins", "cloudpickle"]

[[package]]
name = "certifi"
version = "2022.6.15"
description = "Python package for providing Mozilla's CA Bundle."
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "charset-normalizer"
version = "2.1.0"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
category = "main"
optional = false
python-versions = ">=3.6.0"

[package.extras]
unicode_backport = ["unicodedata2"]

[[package]]
name = "click"
version = "8.1.3"
description = "Composable command line interface toolkit"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.5"
description = "Cross-platform colored terminal text."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "flask"
version = "2.1.2"
description = "A simple framework for building complex web applications."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
click = ">=8.0"
importlib-metadata = {version = ">=3.6.0", markers = "python_version < \"3.10\""}
itsdangerous = ">=2.0"
Jinja2 = ">=3.0"
Werkzeug = ">=2.0"

[package.extras]
async = ["asgiref (>=3.2)"]
dotenv = ["python-dotenv"]

[[package]]
name = "frozenlist"
version = "1.3.0"
description = "A list-like structure which implements collections.abc.MutableSequence"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "idna"
version = "3.3"
description = "Internationalized Domain Names in Applications (IDNA)"
category = "main"
optional = false
python-versions = ">=3.5"

[[package]]
name = "importlib-metadata"
version = "4.12.0"
description = "Read metadata from Python packages"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
zipp = ">=0.5"

[package.extras]
docs = ["sphinx", "jaraco.packaging (>=9)", "rst.linker (>=1.9)"]
perf = ["ipython"]
testing = ["pytest (>=6)", "pytest-checkdocs (>=2.4)", "pytest-flake8", "pytest-cov", "pytest-enabler (>=1.3)", "packaging", "pyfakefs", "flufl.flake8", "pytest-perf (>=0.9.2)", "pytest-black (>=0.3.7)", "pytest-mypy (>=0.9.1)", "importlib-resources (>=1.3)"]

[[package]]
name = "itsdangerous"
version = "2.1.2"
description = "Safely pass data to untrusted environments and back."
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "jinja2"
version = "3.1.2"
description = "A very fast and expressive template engine."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "markupsafe"
version = "2.1.1"
description = "Safely add untrusted strings to HTML/XML markup."
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "multidict"
version = "6.0.2"
description = "multidict implementation"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "replit"
version = "3.2.4"
description = "A library for interacting with features of repl.it"
category = "main"
optional = false
python-versions = ">=3.8,<4.0"

[package.dependencies]
aiohttp = ">=3.6.2,<4.0.0"
Flask = ">=2.0.0,<3.0.0"
requests = ">=2.25.1,<3.0.0"
typing_extensions = ">=3.7.4,<4.0.0"
Werkzeug = ">=2.0.0,<3.0.0"

[[package]]
name = "requests"
version = "2.28.1"
description = "Python HTTP for Humans."
category = "main"
optional = false
python-versions = ">=3.7, <4"

[package.dependencies]
certifi = ">=2017.4.17"
charset-normalizer = ">=2,<3"
idna = ">=2.5,<4"
urllib3 = ">=1.21.1,<1.27"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use_chardet_on_py3 = ["chardet (>=3.0.2,<6)"]

[[package]]
name = "typing-extensions"
version = "3.10.0.2"
description = "Backported and Experimental Type Hints for Python 3.5+"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "urllib3"
version = "1.26.10"
description = "HTTP library with thread-safe connection pooling, file post, and more."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4"

[package.extras]
brotli = ["brotlicffi (>=0.8.0)", "brotli (>=1.0.9)", "brotlipy (>=0.6.0)"]
secure = ["pyOpenSSL (>=0.14)", "cryptography (>=1.3.4)", "idna (>=2.0.0)", "certifi", "ipaddress"]
socks = ["PySocks (>=1.5.6,!=1.5.7,<2.0)"]

[[package]]
name = "werkzeug"
version = "2.1.2"
description = "The comprehensive WSGI web application library."
category = "main"
optional = false
python-versions = ">=3.7"

[package.extras]
watchdog = ["watchdog"]

[[package]]
name = "yarl"
version = "1.7.2"
description = "Yet another URL library"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
idna = ">=2.0"
multidict = ">=4.0"

[[package]]
name = "zipp"
version = "3.8.0"
description = "Backport of pathlib-compatible object wrapper for zip files"
category = "main"
optional = false
python-versions = ">=3.7"

[package.extras]
docs = ["sphinx", "jaraco.packaging (>=9)", "rst.linker (>=1.9)"]
testing = ["pytest (>=6)", "pytest-checkdocs (>=2.4)", "pytest-flake8", "pytest-cov", "pytest-enabler (>=1.0.1)", "jaraco.itertools", "func-timeout", "pytest-black (>=0.3.7)", "pytest-mypy (>=0.9.1)"]

[metadata]
lock-version = "1.1"
python-versions = "^3.8"
content-hash = "51b0542e716c90d6c57fa9f97b6c828b66b936425d6c444546be0a7f81b32a5a"

[metadata.files]
aiohttp = []
aiosignal = []
async-timeout = []
attrs = []
certifi = []
charset-normalizer = []
click = []
colorama = []
flask = []
frozenlist = []
idna = []
importlib-metadata = []
itsdangerous = []
jinja2 = []
markupsafe = []
multidict = []
replit = []
requests = []
typing-extensions = []
urllib3 = []
werkzeug = []
yarl = []
zipp = []


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pyproject.toml

[tool.poetry]
name = "repl_python3_Day-7-Hangman-Final"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
