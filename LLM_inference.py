from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
import os
import json
import sys
import logging

logging.basicConfig(level=logging.ERROR)

model_name = "t5-small"

# if model_checkpoint in ["t5-small", "t5-base", "t5-large", "t5-3b", "t5-11b"]:
#     prefix = "summarize: "
# else:
#     prefix = ""


def summarize(param):

    default_document = 'The full cost of damage in Newton Stewart, one of the areas worst affected, is still being assessed.\nRepair work is ongoing in Hawick and many roads in Peeblesshire remain badly affected by standing water.\nTrains on the west coast mainline face disruption due to damage at the Lamington Viaduct.\nMany businesses and householders were affected by flooding in Newton Stewart after the River Cree overflowed into the town.\nFirst Minister Nicola Sturgeon visited the area to inspect the damage.\nThe waters breached a retaining wall, flooding many commercial properties on Victoria Street - the main shopping thoroughfare.\nJeanette Tate, who owns the Cinnamon Cafe which was badly affected, said she could not fault the multi-agency response once the flood hit.\nHowever, she said more preventative work could have been carried out to ensure the retaining wall did not fail.\n"It is difficult but I do think there is so much publicity for Dumfries and the Nith - and I totally appreciate that - but it is almost like we\'re neglected or forgotten," she said.\n"That may not be true but it is perhaps my perspective over the last few days.\n"Why were you not ready to help us a bit more when the warning and the alarm alerts had gone out?"\nMeanwhile, a flood alert remains in place across the Borders because of the constant rain.\nPeebles was badly hit by problems, sparking calls to introduce more defences in the area.\nScottish Borders Council has put a list on its website of the roads worst affected and drivers have been urged not to ignore closure signs.\nThe Labour Party\'s deputy Scottish leader Alex Rowley was in Hawick on Monday to see the situation first hand.\nHe said it was important to get the flood protection plan right but backed calls to speed up the process.\n"I was quite taken aback by the amount of damage that has been done," he said.\n"Obviously it is heart-breaking for people who have been forced out of their homes and the impact on businesses."\nHe said it was important that "immediate steps" were taken to protect the areas most vulnerable and a clear timetable put in place for flood prevention plans.\nHave you been affected by flooding in Dumfries and Galloway or the Borders? Tell us about your experience of the situation and how it was handled. Email us on selkirk.news@bbc.co.uk or dumfries@bbc.co.uk.'

    print(param)
    if  type(param) is str :
        print('param is a json string')        
        obj = json.loads(param)
        data = obj['document']
        action=obj['action']
    elif type(param) is dict :
        print('param is a dictionary')
        data = param['document']
        action=param['action']
        
    # return json.dumps({"summary": data})
    tokenizer = AutoTokenizer.from_pretrained('./models/')
    model = TFAutoModelForSeq2SeqLM.from_pretrained('./models/')
    # if 't5' in model_name:
    #     document = "summarize: " + document
    if action == "summarize":
        print(f"action is :{action}")
        if len(data) == 0 :
            data = default_document
        document = "summarize: " + data
        tokenized = tokenizer([document], max_length=512, truncation=True, return_tensors='np')
        out = model.generate(**tokenized, max_length=128)
        response = tokenizer.decode(out[0])
        print(response)
        #return json.dumps({'summary': tokenizer.decode(out[0])})
        #return (json.dumps({"my_data": data}))
    else:
        response = "Invalid Action"
    return {"summary": response}


    
# def main():
#     default_json = "{\"action\":\"summarize\", \"document\":\"Vish is trying something\"}"
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