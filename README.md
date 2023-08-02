# Demo LLM on CML 

### Motivations


The release of GPT4 has resulted in considerable attention around how LLMs can be used for building productivity based applications. However enterprises exploring LLM use cases are considerably wary of implementing Black box models. I define Black box models as those, whose methods of training i.e. code and datasets as well as methods of providing inferences are behind paywalls. This has resulted in considerable activity in Open source community around Open source models i.e. models which have been trained on open datasets, source code is available for reviews etc. 


This demo has been setup with the objective to use allow us to understand how to use LLMs in Cloudera machine Learning. Here we focus lesser on the "accuracy" of the models and more on understanding how we can stand up models for local hosting in CML. These demo scripts use a mixture of large Models ( 8GB + parameters, that necessitate GPU usage and smaller models that can be easily set up with CPUs. I will have each script describe at the start as GPU required or not. Please be cautious on costs associated with GPU usage and adhere to clouder/ or your organizations cost control policies on the same.


### Credits 
The code sources have been augmented  from different internet sources including HF, langchain etc for learning purposes. All credits to these source. 


### Prerequisites

- In some code snippets we will need to use a key on Huggingface for use in the code. Please go to the huggingface website to create a new keyhere. 
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

### Files
1. 1_Bootstray.py : This setups the necessary libraries for us to work with LLM models 

2. 

This Demo has following files : 
1. Intro_LLM_on_HuggingFace : Needs a hugging face key and builds an understanding of the transformers library of HF
2. Intro_Langchain - Build an understanding on Langchain framework for promp templating, memory, agents etc.
3. Intro_Vicuna_Langchain_chromadb  - Building an end to end pipeline ( at the time of writing this is still WIP)


4. Go to workspace and choose the appropriate GPU from the ouput of the command in step 3.