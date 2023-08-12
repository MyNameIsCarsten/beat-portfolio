# beat-portfolio
Basic Django project to display beat catalog and to filter it. Data is stored within a table and subsequently displayed.

# Requirements
Install the required packages by running the following command in your terminal: 

`pip install -r .\requirements.txt`

# How it works
## Beat naming
My beats are all named in a specific way:
[0001] C-Minor 100BPM Beat-Name (Prod. by MyName)

The script that is used for generating the database will use this naming convention to grab the key, BPM, beat title and path to the beat.

## Fill database
In order to fill the database you will need to provide a path e.g.:
`D:\Dropbox\Beats\`

Note: Submitting a path more than one will lead to duplicate entries.

