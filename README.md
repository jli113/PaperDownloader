# PaperDownloader
Download papers from ScienceDirect and sci-hub using python.

This Repository contains 2 scripts. 

The first one, "ConvertBIB2CSV", is to convert .bib file to .csv, it also contains the codes to compare two .bib files.
This script iteratively reads and converts the citations into dataframes. 

The second script, "download", is to download the papers.

This script opens the webpage and download papers. If the paper is available on ScienceDirect, it will access the file link, otherwise, it will search with sci-hub.
The script contains the function to get the latest address of sci-hub.
Download might be interrupted by net connection, when it occurs, just run the download file again.

There are some packages to be installed in the first place, either with 'conda install xx' or 'pip install xx'.
Also selenium needs an available webdriver path, the version of the webdriver depends the your installed Chrome version. Here is the download link: http://chromedriver.storage.googleapis.com/index.html
