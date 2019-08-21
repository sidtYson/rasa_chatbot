# Setup
## Environment
+ conda create -n botenv python=3.6
+ conda activate botenv
+ pip install rasa==1.2.3

## Downloads
+ pip install rasa[spacy]
+ python -m spacy download en
+ python -m spacy download en_core_web_md
+ python -m spacy link en_core_web_md en

## Training - NLU for intent entity & Policy for dialogue management
+ Add your nlu intent and entity in data/nlu.md
+ Add your stoties in data/stories.md
+ Add your domain data - slots, intent, entity, templates etc. in domain.yml
+ Add your custom action in actions.py - here you can connect to DB
+ Add the webhook in endpoints.yml
+ Add training both NLU and policy in config.yml
+ rasa train

## Running
+ rasa shell
