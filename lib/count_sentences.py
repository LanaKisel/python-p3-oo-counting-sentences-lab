#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        pass
        self._value = value        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")                          
    
    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):        
        myString = self.value
        for punc in ["!","?", "..."]:
            myString = myString.replace(punc, ".")
        sentences = [x for x in myString.split('.') if x]    
        return len(sentences)


        # period_split =[s for s in myString.split(".") if "?" not in s and "!" not in s and s] 
        # question_split = [s for s in myString.split("?") if "!" not in s and s]
        # exclamation_spilt = [s for s in myString.split("!") if s]
        # count = len(exclamation_spilt) + len(period_split)+ len(question_split)

        # print(period_split)
        # print(exclamation_spilt)
        # print(question_split)
        # print(myString)
        # return count

