from dataclasses import dataclass
from typing import List
from fastapi import FastAPI, HTTPException, Query

@dataclass
class Flight:
    number: str  # номер рейса
    carrier: str  # авиакомпания
    plane: str  # самолет
    go_from: str  # аэропорт вылета
    go_to: str  # аэропорт прибытия

all_flights = [
  Flight(
    number="AF123", 
    carrier="Aeroflot", 
    plane="Boeing737", 
    go_from="DME", 
    go_to="HEL"
  ), Flight(
    number="UA300", 
    carrier="Ural Airlines", 
    plane="Embraer170", 
    go_from="HEL", 
    go_to="DME"
  ), Flight(
    number="CD456", 
    carrier="S7 Airlines", 
    plane="AirbusA320", 
    go_from="LEN", 
    go_to="DME"
), Flight(
    number="EF789", 
    carrier="Ural Airlines", 
    plane="AirbusA321", 
    go_from="SVX", 
    go_to="AER"
), Flight(
    number="GH012", 
    carrier="Pobeda", 
    plane="Boeing737", 
    go_from="DME", 
    go_to="AER"
), Flight(
    number="IJ345", 
    carrier="Aeroflot", 
    plane="Boeing777", 
    go_from="HEL", 
    go_to="DME"
)]


alphabet = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu",
}

app = FastAPI()

# @app.get("/letter/{letter}")
# def read_alphabet(letter: str) -> dict:
#     result = alphabet.get(letter.upper(), 'Not Found')
#     if result == 'Not Found':
#         raise HTTPException(status_code=404, detail = 'Not Found')
#     return {"result":result}

##############################

# @app.get('/find/')
# def find_view(letter: Union[str, None] = None) -> dict:
#     result = alphabet.get(letter.upper(), 'Not Found')
#     if result == 'Not Found':
#         raise HTTPException(status_code=404,detail=result)
#     return {"result":result}

##############################

# @app.get('/check/{letter}/{word}')
# def check_view(letter: str, word: str):
#     result = alphabet.get(letter.upper()) == word.title()
#     return {'result': result}

##############################

# @app.get('/between/')
# def between_view(frm:str | None, to:str | None):
#     between = ord(to) - ord(frm)
#     if between == 0:
#         return {'result':'-'}
#     frm = frm if frm < to else to
#     result = ''.join(chr(ord(frm) + i) for i in range(1, abs(between)))
#     return {'result':result}

##############################

# @app.get('/get-some/{number}')
# def get_some_view(number:int):
#     if number == 0:
#         return {'result':'-'}
#     result = ''.join(list(alphabet.keys())[:number])
#     return {'result':result}

##############################

# @app.get('/letters/')
# def letters_view(limit:int, offset:int) -> dict[str, str]:
#     _alphabet = list(alphabet.keys())
#     if offset > len(_alphabet):
#         return {'result': '-'}
#     #result = ''.join(_alphabet[i] for i in range(offset, offset + limit))
#     result = ''.join(_alphabet[offset:offset+limit])
#     return {'result':result}

##############################

# @app.get('/letters/')
# def letters_view() -> dict[str, str]:
#     _alphabet = list(alphabet.keys())
#     result = ''.join(_alphabet[:5])
#     return {'result':result}

# @app.get('/letters/page/{page_number}')
# def letters_view(page_number:int) -> dict[str, str]:
#     _alphabet = list(alphabet.keys())
#     if page_number > len(_alphabet) // 5 + 1:
#         raise HTTPException(status_code=404, detail='Ошибка 404')
#     result = ''.join(_alphabet[page_number*5-5:page_number*5])
#     return {'result':result}

##############################

# @app.get('/search/')
# def search_view(s:str) -> dict[str, str]:
#     words = list(alphabet.values())
#     result = ', '.join(word for word in words if s in word.lower())
#     if not result:
#       raise HTTPException(status_code=404, detail='Not Found')
#     return {'result':result}

##############################

# @app.get('/get/')
# def get_view(length:int) -> dict[str, str]:
#     result = ', '.join(list(filter(lambda x: len(x) == length, list(alphabet.values()))))
#     if not result:
#       raise HTTPException(status_code=404, detail='Not Found')
#     return {'result':result}

##############################

# @app.get('/letters/')
# def letters_view(limit:int = None, offset:int = None, sort:str = None) -> dict[str, str]: # type: ignore
#     if limit is None or offset is None or sort is None or sort not in ['desc', 'asc']: # type: ignore
#        raise HTTPException(status_code=400, detail='Bad request')
#     result = ''.join(list(alphabet.keys())[offset:limit+offset])
#     if sort == 'desc':
#         result = result[::-1]
#     return {'result':result}

##############################

# @app.get('/flights/path/{go_from}')
# def flights_from_view(go_from:str):
#     result: List[str] = []
#     for flight in all_flights:
#         if flight.go_from == go_from.upper():
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}

##############################

# @app.get('/flights/')
# def flights_from_to_view(go_from:str, go_to:str):
#     result: List[str] = []
#     for flight in all_flights:
#         if flight.go_from == go_from.upper() and flight.go_to == go_to.upper():
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}

##############################

# @app.get('/flights/from/{airport_1}-{airport_2}')
# def flights_between_view(airport_1:str, airport_2:str):
#     result: List[str] = []
#     for flight in all_flights:
#         if (flight.go_from == airport_1.upper() or flight.go_to == airport_1.upper()) and (flight.go_from == airport_2.upper() or flight.go_to == airport_2.upper()):
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}

##############################

# @app.get('/flights/from/{airport_1}')
# def get_flights_from(airport_1:str):
#     result: List[str] = []
#     for flight in all_flights:
#         if flight.go_from == airport_1.upper():
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}


# @app.get('/flights/from/{airport_1}/to/{airport_2}')
# def get_flights_from_to(airport_1:str, airport_2:str):
#     result: List[str] = []
#     for flight in all_flights:
#         if flight.go_from == airport_1.upper() and flight.go_to == airport_2.upper():
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}

##############################

# @app.get('/flights/')
# def get_flights_with(with_:str = Query(None)):
#     result: List[str] = []
#     planes = with_.split(',')
#     if not planes:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     for flight in all_flights:
#         if flight.plane in planes:
#           result.append(flight.number)
#     if not result:
#         raise HTTPException(status_code=404, detail='Not Found')   
#     return {'result':result}