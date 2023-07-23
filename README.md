# Setting it up
This project requires python and virtualenv to be installed. It uses Python 3.8

To set up the virtual environment run `./setup.sh`. This should create an environment in the `env` directory and install required dependencies.

To activate this environment will require:
`source env/bin/activate`

This project expects there to be an environment variable `OPENAI_API_KEY` set with an OpenAI key with access to GPT3.5.

# Embeddings
The persisted index (embeddings) are not stored in the project due to size and will need to be generated. This can be done by running: 
`python create_embeddings.py`

This will take the file `manual.md` (a converted version of the Qualisys manual) and split it into sections which will be stored in `manual/` for review. It will also use llama-index to create embeddings of each section and persist them into `persisted_index`. This can take some time.

# Querying
There is a simple command line script for asking queries of the embeddings. Running `python query.py` will load the index and provide a prompt like: `Enter query: `. Whatever is entered will be treated as a question and use the embeddings to try to provide an answer.

An empty query or ctrl+c will stop the program.
