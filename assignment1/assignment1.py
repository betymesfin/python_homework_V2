#Task one
def hello():
    return "Hello!"
print (hello())


#Task Two
def greet(name):
    return "Hello, " + name + "!"
print(greet("Beth"))


#Task Three

def calc(a,b,operation="multipy"):
   match operation:
        case "add":
            try:
                return float(a) + float(b)
            except ( ValueError):
                return "You can't add those values!"
        
        case "subtract":
            try:
                return float(a) - float(b)
            except (ValueError):
                return "You can't subtract those values!"
        
        case "divide":
            try:
                a, b = float(a), float(b)
                if b == 0:
                    raise ZeroDivisionError
                return a / b
            except ZeroDivisionError:
                return "You can't divide by 0!"
            except (ValueError):
                return "You can't divide those values!"
        
        case "modulo":
            try:
                return int(a) % int(b)
            except (ValueError):
                return "You can't modulo those values!"
        
        case _:
            try:
                return float(a) * float(b)
            except (ValueError):
                return "You can't multiply those values!"
answer=calc (12.6,4.4,"subtract")
print (answer)



#Task 4

def data_type_conversion(value,requested_type):
     try:
        if requested_type == "int":
            return int(value)
        elif requested_type == "float":
            return float(value)
        elif requested_type == "str":
            return str(value)
        else:
            return f"Unknown data type: {requested_type}"
     except (ValueError):
        return f"You can't convert {value} into a {requested_type}."

print(data_type_conversion(3.14, "int"))


#Task 5

def grade(*args):
    try:
        scores = [float(score) for score in args]
        average = sum(scores) / len(scores)
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (ValueError, TypeError, ZeroDivisionError):
        return "Invalid data was provided."
print(grade(100, 90, 85))


#Task6

def repeat(string, count):
    result = ""
    for x in range(count):
        result += string
    return result

print(repeat("hi", 3))


#Task 7

def student_scores(mode, **kwargs):
    try:
        if mode == "best":
            best_student = max(kwargs, key=kwargs.get)
            return best_student
        elif mode == "mean": 
            scores = kwargs.values()
            return sum(scores) / len(scores)
        else:
            return "Invalid mode."
    except (ZeroDivisionError, ValueError):
        return "No student scores provided."

print(student_scores("mean", Alice=90))
print(student_scores("best", Alice=88, Bob=91, Carol=85)) 


#Task 8


def titleize(title):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = title.split()
    if not words:
        return ""
    words[0] = words[0].capitalize()
    
    if len(words) > 1:
        words[-1] = words[-1].capitalize()

    for i, word in enumerate(words[1:-1], start=1):
        if word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)
print(titleize("war and peace"))



#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
print(hangman("alphabet", "a"))


#Task 10

def pig_latin(sentence):
    vowels = "aeiou"

    def convert_word(word):
        if word[0] in vowels:
            return word + "ay"
        else:
            
            i = 0
            while i < len(word) and word[i] not in vowels:
                
                if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                    i += 2
                    break
                i += 1
            return word[i:] + word[:i] + "ay"

    words = sentence.split()
    pig_latin_words = [convert_word(word) for word in words]
    return " ".join(pig_latin_words)

print(pig_latin("banana"))