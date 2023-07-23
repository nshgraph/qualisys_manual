import time
from llama_index import GPTVectorStoreIndex, StorageContext, load_index_from_storage, ServiceContext, Prompt
from llama_index.llms import OpenAI

custom_prompt = """"We have provided context information below.
---------------------
{context_str}
---------------------
Given this information, please answer the question: {query_str}

Your answer should:
- not be longer than 100 words
- not expect the user to look up additional documentation
- provide a reference to the correct section"""

start = time.time()
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
service_context_chatgpt = ServiceContext.from_defaults(llm=llm, chunk_size=1024)
storage_context = StorageContext.from_defaults(persist_dir="persisted_index")
index = load_index_from_storage(storage_context, service_context=service_context_chatgpt)
print("Loaded index in {:.1f} seconds".format(time.time() - start))
query_engine = index.as_query_engine(text_qa_template=Prompt(custom_prompt))


while True:
    print("Type 'exit' (or nothing) to exit")
    query = input("Enter query: ")
    start = time.time()
    if query.strip() in ("exit", ""):
        break
    response = query_engine.query(query) 
    print("Got response in {:.1f} seconds".format(time.time() - start))
    print(response)