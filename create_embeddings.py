import re
import os
import shutil
from llama_index import GPTVectorStoreIndex, Document

documents = []
index = 0
def get_manual_documents():
    global index

    # ensure there is an empty manual directory
    if os.path.exists("manual"):
        shutil.rmtree("manual")
    os.mkdir("manual")

    with open("manual.md", "r") as f:
        lines = f.readlines()

    remove_pages = re.compile(r"\[page \d+\]")
    remove_chapters = re.compile(r"\[chapter \d+\]")

    section = []
    for line in lines:
        if line.startswith("#"):
            if len(section) > 1:
                documents.append(Document(text="\n".join(section)))

                with open(f"manual/{index}.md", "w") as f:
                    f.writelines(section)
                index += 1
            section = [line]
        elif line.startswith("```"):
            continue
        elif line.strip():
            line = remove_pages.sub("", line)
            line = remove_chapters.sub("", line)
            section.append(line)

get_manual_documents()

index = GPTVectorStoreIndex([])
print("Have {} documents".format(len(documents)))
# documents = documents[:20]
index = 0
for doc in documents:
    if index % 100 == 0:
        print("Indexing document {}".format(index))
    index.insert(doc)

print("Created index")
index.storage_context.persist(persist_dir="persisted_index")
print("Saved index")