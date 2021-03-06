#---Import libraries
import unicodedata
import re

def remove_accents(row):
    return "".join(c for c in unicodedata.normalize("NFD", row) if unicodedata.category(c) != "Mn"
 
def removeHTMLtags(row):
    encodings_to_remove = re.compile("")
    clean_row = re.sub(encodings_to_remove, "", row)
    return clean_row

def sanitize(row):
   sanitizedText = row.replace(" ", "")
   sanitizedText = sanitizedText.replace("&", "")
   sanitizedText = sanitizedText.replace("\xa0", "")
   sanitizedText = sanitizedText.replace("\t", "")
   return sanitizedText
 
 def stop_words(row):
   cleanedColumn = row.apply(lambda x: [item for item in x if item not in stop])
   return cleanedColumn
 
def removePunctNum(row):
   cleanedColumn = row.str.replace('[^\w\s]','')
   cleanedColumn = cleanedColumn.str.replace('\d+', '')
   return cleanedColumn
 
