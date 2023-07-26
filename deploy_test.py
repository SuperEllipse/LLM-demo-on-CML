from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import os
import json
import sys

model_name = "t5-small"

# Comment the lines below before using in a model           
def summarize(param):
    print(param)
    if  type(param) is str :
        print('param is a json string')        
        obj = json.loads(param)
        data = obj['document']
    elif type(param) is dict :
        print('param is a dictionary')
        data = param['document']
    # return json.dumps({"summary": data})
    return {"summary": data}

    
# def main():
#     default_json = "{\"document\": \"something\"}"
#     args = sys.argv
#     print (args)
#     if len(args) > 1:
#         input_json = args[1]
#     else :  
#         input_json = default_json
   
#     print(summarize(input_json))

#     #replicating CML Behavior
#     print(summarize(json.loads(input_json)))


# if __name__ == "__main__":
#     main()
           