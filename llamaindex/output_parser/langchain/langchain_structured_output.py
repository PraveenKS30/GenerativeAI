from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.output_parsers import LangchainOutputParser
from llama_index.llms.openai import OpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from llama_index.core.prompts.default_prompts import (
    DEFAULT_TEXT_QA_PROMPT_TMPL,
)


# load documents 
documents = SimpleDirectoryReader("data").load_data()

# create index
index = VectorStoreIndex.from_documents(documents)

# define output schema 
response_schemas = [
    ResponseSchema(
        name = "Education",
        description = "Describes the author's educational experience/background.",

    ),
    ResponseSchema(
        name = "Work",
        description="Describes the author's work experience/background.",

    ),
]

# define output parser
lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
output_parser = LangchainOutputParser(lc_output_parser)

# take a look at the new QA template!
fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
print(fmt_qa_tmpl)

# attach output parser
llm = OpenAI(output_parser= output_parser)

# get structured response
query_engine = index.as_query_engine(llm = llm)
response = query_engine.query("What did author do growing up?")
print(response)