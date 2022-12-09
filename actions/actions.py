# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionGetGpa(Action):

    def name(self) -> Text:
        return "action_gpa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # url = "https://some.api.com/user/xxx/status"
        # status = requests.get(url).json

        #TODO ajouter le call api intrat pour recuper le gpa

        status = 3
        if status:
            dispatcher.utter_message(text="Your GPA is 3.5")
        else:
            dispatcher.utter_message(
                text="Sorry, I can't get your GPA right now")
        return []

class ActionPlanning(Action):
    
        def name(self) -> Text:
            return "action_planning"
    
        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            status = 3
            if status:
                dispatcher.utter_message(text="You have a kick off at 9 and you have a meeting at 10")
            else:
                dispatcher.utter_message(
                    text="Sorry, I can't get your planning right now")
            return []

class ActionModul(Action):
        
            def name(self) -> Text:
                return "action_modul"
        
            def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                status = 3
                if status:
                    dispatcher.utter_message(text="You are regested at math modul")
                else:
                    dispatcher.utter_message(
                        text="Sorry, I can't get your modul right now")
                return []