##  La funzione richiede un'ora di inizio nel formato dell'orologio a 12 ore,
#   una durata che indica il numero di ore e minuti e (facoltativo) un giorno
#   di inizio della settimana, senza differenziare tra maiuscole e minuscole;
#   dopodiché somma la durata all'ora di inizio e restituisce il risultato.
#   @param start un'ora di inizio (che termina in AM o PM)
#   @param duration una durata (ore e minuti)
#   @param dayOfTheWeek giorno di inizio della settimana (facoltativo)
#   @return new_time restituisce il risultato
#
def add_time(start, duration, dayOfTheWeek=""):
  
  # associa alla variabile startingTime l'orario di inizio
  startingTime = ""
  startingTime = start.split()[0]

  # associa alla variabile startingMeridian il suffisso AM/PM dell'orario di inizio
  startingMeridian = ""
  startingMeridian = start.split()[1]
   
  # associa alla variabile startingHour l'intero del valore dell'ora di inizio
  startingHour = 0
  startingHour = int(startingTime.split(":")[0])

  # associa alla variabile startingMinutes l'intero del valore dei minuti di inizio
  startingMinutes = 0
  startingMinutes = int(startingTime.split(":")[1])

  # associa alla variabile durationHours l'intero del valore dell'ora di durata
  durationHours = 0
  durationHours = int(duration.split(":")[0])

  # associa alla variabile durationMinutes l'intero del valore dei minuti di durata
  durationMinutes = 0
  durationMinutes = int(duration.split(":")[1])

  # condizione che calcola e associa alla variabile endingMinutes il valore finale dei minuti
  endingMinutes = ""
  
  tot_minutes = startingMinutes + durationMinutes
  if tot_minutes % 60 < 10 :
    endingMinutes = "0" + str(tot_minutes % 60)
  else :
    endingMinutes = str(tot_minutes % 60)
  
  # condizione che calcola e associa alla variabile endingHour il valore finale delle ore
  endingHour = 0
  
  tot_hours = startingHour + durationHours
  endingHour = str(tot_hours % 12 + tot_minutes // 60)

  # condizione che determina e associa alla variabile endingMeridian il nuovo valore (AM/PM)
  endingMeridian = ""
  
  if (durationHours // 12) % 2 == 0 and (startingHour + durationHours % 12 + tot_minutes // 60) < 12 :
    if startingMeridian == "AM" :
      endingMeridian = "AM"  
    else :
      endingMeridian = "PM"
  else :
    if startingMeridian == "AM" :
      endingMeridian = "PM"  
    else :
      endingMeridian = "AM"

  # condizione che calcola e associa alla variabile durationDays il numero di giorni di durata
  durationDays = 0
  
  if startingMeridian == "AM" and (startingHour + durationHours % 24) > 24 :
    durationDays = (durationHours + durationMinutes // 60) // 24 + 1
  elif startingMeridian == "PM" and (startingHour + durationHours % 24) > 12 :
    durationDays = (durationHours + durationMinutes // 60) // 24 + 1
  elif startingMeridian == "PM" and (startingHour * 60 + startingMinutes + durationMinutes % 60) > 12 * 60 :
    durationDays = (durationHours + durationMinutes // 60) // 24 + 1
  else :
    durationDays = (durationHours + durationMinutes // 60) // 24

  # condizione che determina e associa alla variabile new_dayOfTheWeek il nuovo valore (giorno della settimana)
  weeklyDays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  indexDay = 0
  new_indexDay = 0
  new_dayOfTheWeek = ""

  if dayOfTheWeek != "" :
    indexDay = weeklyDays.index(dayOfTheWeek.lower())
    weeklyDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    new_indexDay = indexDay + durationDays % 7 - 7
    new_dayOfTheWeek = ", " + weeklyDays[new_indexDay]
  else :
    new_dayOfTheWeek = ""
  
  # restituzione di new_time
  if durationDays < 1 :
      new_time = str(endingHour) + ":" + endingMinutes + " " + endingMeridian + new_dayOfTheWeek
  elif durationDays == 1 :
      new_time = str(endingHour) + ":" + endingMinutes + " " + endingMeridian + new_dayOfTheWeek + " (next day)"
  else :
      new_time = str(endingHour) + ":" + endingMinutes + " " + endingMeridian + new_dayOfTheWeek + " (" + str(durationDays) + " days later)"
  
  return new_time

## test della funzione time_calculator()
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
