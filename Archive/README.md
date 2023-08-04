# Demo LLM on CML

### Overview

This Demo is a WIP body of work on testing LLM on CML. We use only Open source models for prompt tuning and pre-training 

This Demo has following files : 
1. Intro_LLM_on_HuggingFace : Needs a hugging face key and builds an understanding of the transformers library of HF
2. Intro_Langchain - Build an understanding on Langchain framework for promp templating, memory, agents etc.
3. Intro_Vicuna_Langchain_chromadb  - Building an end to end pipeline ( at the time of writing this is still WIP)


### Credits 
The code sources have been augmented  from different internet sources including HF, langchain etc for learning purposes. All credits to these source. 

### Prerequisites

- Need to create a key on Huggingface for use in the code or Open AI key if you are using that part of the code. 
- CML Runtime Configuation that worked for me are GPU (), Jupyter LAB , Python 3.9, Edition ( Nvidia GPU), version 2022.11
- Resource Profile 16vCPU/ 64GB Memory, 1 GPU
- GPU Configuration : g4dn.8xlarge
- To test what GPUs are available for the region where you are setting up workspace
1. Start Terminal on laptop
2. Configure AWS CLI for your account
3. Enter the following command
```
aws ec2 describe-instance-types --filters "Name=current-generation,Values=true" "Name=memory-info.size-in-mib,Values=65536" --query "InstanceTypes[*].[InstanceType]" --output text | sort
```
4. Go to workspace and choose the appropriate GPU from the ouput of the command in step 3.