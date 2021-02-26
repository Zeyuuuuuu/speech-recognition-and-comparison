import sys
import speech_recognition as sr
import diff_match_patch
import pdfkit
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="psyched-subset-305209-c1a89d60eb87.JSON"

r = sr.Recognizer()
input_path = sys.argv[1]
path_wkpdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
pdf = ""

library = {}
library['011164'] = "For the first two or three years after the Second World War, a new title would often sell out within a few months of publication. However, unless public demand for the book was unusually high, they were rarely able to reprint it. With paper stocks strictly rationed, they could not afford to use up precious paper or tie up their limited capital with a reprint."
library['011165'] = "The starting point of Bergson's theory is the experience of time and motion. Time is the reality we experience most directly, but this doesn't mean that we can capture this experience mentally. The past is gone and the future is yet to come. The only reality is the present, which is real through our experience."
library['011166'] = "The Atlantic coast of the peninsula can be thought of as the cold side, and the sea on this coast tends to be clear and cold, with a variety of seaweeds growing along the rocky shoreline. On a hot day, however, this cold water can be very refreshing and is said to be less hospitable to sharks, which prefer warmer waters."
library['011167'] =  "Most succulent plants are found in regions where there is little rainfall, dry air, plenty of sunshine, porous soils, and high temperatures during part of the year. These conditions have caused changes in plant structures, which have resulted in greatly increased thickness of stems, leaves, and sometimes roots, enabling them to store moisture from the infrequent rains."
library['011168'] =  "The latest scientific evidence on the nature and strength of the links between diet and chronic diseases is examined and discussed in detail in the following sections of this report. This section gives an overall view of the current situation and trends in chronic diseases at the global level."
library['011169'] =  "It was found that while many companies express interest in Jacobson's use case approach, actual scenario usage often falls outside what is described in textbooks and standard methodologies. Users therefore face significant scenario management problems not yet addressed adequately in theory or practice, and are demanding solutions to these problems."

files= os.listdir(input_path)

for file in files:
    if (not os.path.isdir(file)) and (file[-4:]== '.wav'):
        pdf += "<h2><meta charset=\"UTF-8\">" + file[:-4] + "</h2>"
        if len(file)>=10 and file[:6] in library: 
            record_file = sr.AudioFile(input_path+'/'+file)
            with record_file as source:
                audio = r.record(source)
            result_online = r.recognize_google_cloud(audio)
            cfg = pdfkit.configuration(wkhtmltopdf=path_wkpdf)
            dmp = diff_match_patch.diff_match_patch()
            dmp.Diff_Timeout = 1
            diffs = dmp.diff_main(result_online,library[file[:6]].lower())
            dmp.diff_cleanupSemantic(diffs)
            pdf += dmp.diff_prettyHtml(diffs)
        else:
            pdf += "<h3>Text does not exsist in the library.</h3>"

pdfkit.from_string(pdf, input_path+'/output.pdf' ,configuration=cfg)

