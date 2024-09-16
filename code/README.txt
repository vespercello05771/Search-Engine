This folder contains the template code for a search engine application. 

main.py - The main module that contains the outline of the Search Engine.
util.py - An extra file for any additional processing or utility functions - sentenceSegmentation.py, tokenization.py, inflectionReduction.py and stopwordRemoval.py.

To test the code, run main.py with the appropriate arguments
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 
When the -custom flag is passed, the system will take a query from the user as input. When the flag is not passed, all the queries in the Cranfield dataset are considered, for example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics
This will generate *queries.txt files in the OUTPUT FOLDER after each stage of preprocessing of the query and *docs.txt files in the OUTPUT FOLDER after each stage of preprocessing of the documents.
