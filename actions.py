# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import requests


class ActionGetNewst(Action):

    def name(self) -> Text:
        return 'action_get_news'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = tracker.get_slot('category')
        message = f'{category} dummy1, dummy2, dummy3, dummy 4, dummy5'
        dispatcher.utter_message(message)

        return[]
