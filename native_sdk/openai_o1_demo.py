from openai import OpenAI

# initialize client 
client = OpenAI()

# get response 
response = client.chat.completions.create(
    model = "o1-mini",
    messages=[
        {
        "role" : "user",
        "content" : """
            I want to build a Generative AI application in Python programming language to help 
            insurance comapnies to identify the risk levels of a member/patient.
            Please note that I don't want to use the traditional machine learning models. 
            Please suggest an algorithm for the same. Please also suggest how 
            should I report risk levels of a member and what should be the 
            primary input parameters to be considered.Please do provide some
            sample input data as well along with the sample application code.
        """
        }
    ]
)

print(response)
