import pandas as pd
import numpy as np

letter_data = pd.read_csv('letters.csv',delim_whitespace=True,index_col=0)
extra_letter_data = pd.read_csv('extra_letters.csv',delim_whitespace=True,index_col=0)
exception_list = [' ']
def get_latin_char(char = 'ዩ'):
    # if char in exception_list:
    #     return 
    

    try:
        if 4607 < ord(char) < 5018:
            return letter_data[letter_data.eq(char).any(1)].index.values[0]+letter_data[letter_data.eq(char)].dropna(how='all',axis=1).dropna().columns.values[0]
        else:
            return char
    except IndexError:
        if 4607 < ord(char) < 5018:
            return extra_letter_data[extra_letter_data.eq(char).any(1)].index.values[0]+extra_letter_data[extra_letter_data.eq(char)].dropna(how='all',axis=1).dropna().columns.values[0]
        else:
            return char

def get_latin_word(word):
    result =  map(get_latin_char, word)
    return ''.join(list(result))

print(get_latin_word('የይርጋለም የተቀናጀ የግብርና ኢንዱስትሪ ፓርክ 11 ሼዶች ምክትል ርእሰ መስዳደድሩ የገለፁትበቴክኖሎጂ ሽግግር ረገድ የአርሶ አደሩን አቅም የማጎልበት ስራ እየተሰራ እንደሆነም አቶ ርስቱ ተናግረዋል ተቋሙ ያሉበትን ችግሮች ቀርፎ በፍጥነት ወደ ስራ እንዲገባ የክልሉ መንግስት ተገቢውን ድጋፍ ያደርጋል ብለዋልየፓርኩ ዋና ስራ አስፈፃሚ አቶ ብሩ ወልዴ በበኩላቸው ፓርኩ የምግብ ማቀነባበሪያ በመሆኑ ጥንቃቄ ማድረግ ወሳኝ ነው ብለዋልየቀሪ ሼዶች ግንባታ የፋብሪካዎቹ አይነት ወይም ፍላጎት ሲታወቅ የሚገነባ ሲሆን ተቋሙ የውጪ ምንዛሪ እጥረት እንዳለበት ስራ አስፈፃሚው አክለው ጠቁመዋል '))