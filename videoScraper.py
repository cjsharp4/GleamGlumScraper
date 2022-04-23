from youtube_transcript_api import YouTubeTranscriptApi #pip install youtube_transcript_api
import requests #pip install requests
from pytube import YouTube #pip install pytube
from moviepy.editor import * #pip install moviepy
import cv2 #pip install opencv-python
import os 
import pathlib #pip install pathlib
from csv import reader
import time

start = time.time()

"""
# open file in read mode
with open('links.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    video_id_list = []
    video_link_list = []
    for row in csv_reader:
        #iterate through first row 
        for i in range(0,len(row)):
            #check if row is empty 
            if row[i]:
                #get video link 
                video_link_list.append(row[i])
                #get video id
                video_id_list.append(row[i].split("v=",1)[1]) 
"""

with open('random_links2.txt') as text_file:
    video_id_list = []
    video_link_list = []
    for line in text_file:
        stripped_line = line.strip()
        video_id_list.append(stripped_line)
        new_link = 'https://www.youtube.com/watch?v=' + stripped_line
        video_link_list.append(new_link)
        
#print(video_id_list)


##TODO require coords to be certain size so that face is big enough to see in video
##TODO OPTIMIZE CLIP LENGTH SO ONLY TARGET WORD IS IN CLIP (HARDER TODO)
def faceDetect(clip_name):
    #Load the cascade  
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #open face classifier from opencv github
  
    # To capture video from existing video.   
    cap = cv2.VideoCapture(clip_name)  

    faces_array = []
    count = 0

    while True:
        #read frame (img variable)
        _, img = cap.read()  
    

        #stop at end of frames in video
        if(img is None):
            break

        #Convert to grayscale  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
        #Detect the faces  
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)  #increase last two argument (scaleFactor and minNeighbors) for stricter classification

        faces_array.append(faces)
        count = count + 1

    #remove empty tuples or frames with no face detection
    faces_array = [t for t in faces_array if t != ()]
    print('frames with face: ' + str(len(faces_array)))
    print('total frames: ' + str(count))
    print(len(faces_array)/count)
    print('-----------------------')

    #Release VideoCapture object  
    cap.release()

    if( (len(faces_array)/count) > 0.80 ):
        return True
    
    return False


def saveClip(clip_name,folder_name,phoneme):
    cwd = os.getcwd()

    current_filepath = cwd + '/' + clip_name

    #gets directory for proper folder based on word's phoneme
    phoneme_folder = cwd + '/'
    if(phoneme == "(EE)"):
        phoneme_folder += "EE_Videos"
    else:
        phoneme_folder += "UH_Videos"

    destination_folder = phoneme_folder + '/' + folder_name
    destination_filepath = destination_folder + '/' + clip_name

    pathlib.Path(destination_folder).mkdir(parents=True, exist_ok=True)

    os.rename(current_filepath, destination_filepath)



"""
example video link:
https://www.youtube.com/watch?v=7iONU9LxeV8
this is the video id:
7iONU9LxeV8
"""

#video_link = 'https://www.youtube.com/watch?v=7iONU9LxeV8'  
#root = YouTubeTranscriptApi.get_transcript('7iONU9LxeV8') 

#for key in root:
#   print(key['text'])
    
#list of words that we are looking to find in the video
ee_uh_words = [ ["blood","(UH)"],["bloods","(UH)"],["bluff","(UH)"],["bluffs","(UH)"],["blunt","(UH)"],["blunts","(UH)"],["blush","(UH)"],["blushed","(UH)"],["brunch","(UH)"],["brunt","(UH)"],["brush","(UH)"],["brushed","(UH)"],["brusque","(UH)"],["buck","(UH)"],["bucked","(UH)"],["bucks","(UH)"],["buck's","(UH)"],["bud","(UH)"],["budge","(UH)"],["buds","(UH)"],["buff","(UH)"],["buffs","(UH)"],["bug","(UH)"],["bugged","(UH)"],["bugs","(UH)"],["bulb","(UH)"],["bulbs","(UH)"],["bulge","(UH)"],["bulged","(UH)"],["bulk","(UH)"],["bulked","(UH)"],["bulks","(UH)"],["bum","(UH)"],["bump","(UH)"],["bumped","(UH)"],["bumps","(UH)"],["bums","(UH)"],["bun","(UH)"],["bunch","(UH)"],["bunched","(UH)"],["bunk","(UH)"],["bunks","(UH)"],["buns","(UH)"],["bunt","(UH)"],["bus","(UH)"],["bust","(UH)"],["busts","(UH)"],["but","(UH)"],["butt","(UH)"],["butts","(UH)"],["buzz","(UH)"],["buzzed","(UH)"],["chuck","(UH)"],["chug","(UH)"],["chum","(UH)"],["chump","(UH)"],["chunk","(UH)"],["chunks","(UH)"],["club","(UH)"],["clubbed","(UH)"],["clubs","(UH)"],["club's","(UH)"],["cluck","(UH)"],["clucked","(UH)"],["clucks","(UH)"],["clump","(UH)"],["clumps","(UH)"],["clung","(UH)"],["clunk","(UH)"],["clutch","(UH)"],["clutched","(UH)"],["come","(UH)"],["comes","(UH)"],["crumb","(UH)"],["crunch","(UH)"],["crunched","(UH)"],["crush","(UH)"],["crushed","(UH)"],["crust","(UH)"],["crutch","(UH)"],["crux","(UH)"],["cub","(UH)"],["cubs","(UH)"],["cub's","(UH)"],["cud","(UH)"],["cuff","(UH)"],["cuffs","(UH)"],["cull","(UH)"],["cult","(UH)"],["cults","(UH)"],["cup","(UH)"],["cupped","(UH)"],["cups","(UH)"],["cusp","(UH)"],["cuss","(UH)"],["cut","(UH)"],["cuts","(UH)"],["does","(UH)"],["done","(UH)"],["Doug","(UH)"],["dove","(UH)"],["doves","(UH)"],["drudge","(UH)"],["drug","(UH)"],["drugged","(UH)"],["drugs","(UH)"],["drug's","(UH)"],["drum","(UH)"],["drummed","(UH)"],["drums","(UH)"],["drunk","(UH)"],["drunks","(UH)"],["dub","(UH)"],["dubbed","(UH)"],["duck","(UH)"],["ducked","(UH)"],["ducks","(UH)"],["duct","(UH)"],["ducts","(UH)"],["dud","(UH)"],["duds","(UH)"],["dug","(UH)"],["dull","(UH)"],["dulled","(UH)"],["dulls","(UH)"],["dumb","(UH)"],["dump","(UH)"],["dumped","(UH)"],["dumps","(UH)"],["dun","(UH)"],["dunce","(UH)"],["dung","(UH)"],["dunk","(UH)"],["dusk","(UH)"],["dust","(UH)"],["dusts","(UH)"],["Dutch","(UH)"],["flood","(UH)"],["floods","(UH)"],["flood's","(UH)"],["fluff","(UH)"],["flung","(UH)"],["flunk","(UH)"],["flush","(UH)"],["flushed","(UH)"],["flux","(UH)"],["from","(UH)"],["front","(UH)"],["fronts","(UH)"],["frump","(UH)"],["fudge","(UH)"],["fun","(UH)"],["fund","(UH)"],["funds","(UH)"],["fund's","(UH)"],["funk","(UH)"],["fuss","(UH)"],["fuzz","(UH)"],["fuzzed","(UH)"],["glove","(UH)"],["gloved","(UH)"],["gloves","(UH)"],["glum","(UH)"],["glut","(UH)"],["grub","(UH)"],["grubs","(UH)"],["grudge","(UH)"],["gruff","(UH)"],["grunt","(UH)"],["gulch","(UH)"],["gulf","(UH)"],["gulf's","(UH)"],["gull","(UH)"],["gulled","(UH)"],["gulp","(UH)"],["gulped","(UH)"],["gulps","(UH)"],["gum","(UH)"],["gums","(UH)"],["gun","(UH)"],["gunk","(UH)"],["guns","(UH)"],["gun's","(UH)"],["Gus","(UH)"],["gush","(UH)"],["gushed","(UH)"],["gust","(UH)"],["gusts","(UH)"],["gut","(UH)"],["guts","(UH)"],["hub","(UH)"],["hubs","(UH)"],["huff","(UH)"],["hug","(UH)"],["hugged","(UH)"],["hulk","(UH)"],["hulks","(UH)"],["hull","(UH)"],["hum","(UH)"],["hummed","(UH)"],["hump","(UH)"],["humped","(UH)"],["humph","(UH)"],["Hun","(UH)"],["hunch","(UH)"],["hunched","(UH)"],["hung","(UH)"],["hunk","(UH)"],["hunt","(UH)"],["hunts","(UH)"],["hush","(UH)"],["hushed","(UH)"],["husk","(UH)"],["hut","(UH)"],["hutch","(UH)"],["huts","(UH)"],["judge","(UH)"],["judged","(UH)"],["jug","(UH)"],["jump","(UH)"],["jumped","(UH)"],["jumps","(UH)"],["junk","(UH)"],["junks","(UH)"],["just","(UH)"],["love","(UH)"],["loved","(UH)"],["loves","(UH)"],["love's","(UH)"],["luck","(UH)"],["lucked","(UH)"],["lug","(UH)"],["lugged","(UH)"],["lull","(UH)"],["lulled","(UH)"],["lulls","(UH)"],["lump","(UH)"],["lumped","(UH)"],["lumps","(UH)"],["lunch","(UH)"],["lung","(UH)"],["lunge","(UH)"],["lunged","(UH)"],["lungs","(UH)"],["lush","(UH)"],["lust","(UH)"],["lusts","(UH)"],["monk","(UH)"],["monks","(UH)"],["month","(UH)"],["months","(UH)"],["month's","(UH)"],["much","(UH)"],["muck","(UH)"],["mud","(UH)"],["muff","(UH)"],["mug","(UH)"],["mugged","(UH)"],["mugs","(UH)"],["mulch","(UH)"],["mull","(UH)"],["mum","(UH)"],["mumps","(UH)"],["munch","(UH)"],["munched","(UH)"],["mush","(UH)"],["musk","(UH)"],["muss","(UH)"],["must","(UH)"],["mutt","(UH)"],["none","(UH)"],["nub","(UH)"],["nudge","(UH)"],["nudged","(UH)"],["nan","(UH)"],["numb","(UH)"],["nun","(UH)"],["nuns","(UH)"],["nut","(UH)"],["nuts","(UH)"],["of","(UH)"],["once","(UH)"],["one","(UH)"],["ones","(UH)"],["one's","(UH)"],["pluck","(UH)"],["plucked","(UH)"],["plug","(UH)"],["plugged","(UH)"],["plugs","(UH)"],["plum","(UH)"],["plumb","(UH)"],["plumbed","(UH)"],["plump","(UH)"],["plumped","(UH)"],["plunge","(UH)"],["plunged","(UH)"],["plus","(UH)"],["plush","(UH)"],["pub","(UH)"],["pubs","(UH)"],["puck","(UH)"],["puff","(UH)"],["puffed","(UH)"],["puffs","(UH)"],["pulp","(UH)"],["pulse","(UH)"],["pulsed","(UH)"],["pump","(UH)"],["pumped","(UH)"],["pumps","(UH)"],["pun","(UH)"],["punch","(UH)"],["punched","(UH)"],["punk","(UH)"],["punks","(UH)"],["punt","(UH)"],["pup","(UH)"],["pups","(UH)"],["pus","(UH)"],["putt","(UH)"],["rough","(UH)"],["roughed","(UH)"],["rub","(UH)"],["rubbed","(UH)"],["rug","(UH)"],["rugs","(UH)"],["rum","(UH)"],["rump","(UH)"],["run","(UH)"],["rung","(UH)"],["runs","(UH)"],["runt","(UH)"],["rush","(UH)"],["rushed","(UH)"],["rusk","(UH)"],["Russ","(UH)"],["rust","(UH)"],["rut","(UH)"],["ruts","(UH)"],["scrub","(UH)"],["scrubbed","(UH)"],["scruff","(UH)"],["scrunch","(UH)"],["scud","(UH)"],["scuff","(UH)"],["scull","(UH)"],["sculpt","(UH)"],["scum","(UH)"],["shove","(UH)"],["shoved","(UH)"],["shrub","(UH)"],["shrubs","(UH)"],["shrug","(UH)"],["shrugged","(UH)"],["shrugs","(UH)"],["shuck","(UH)"],["shucks","(UH)"],["shun","(UH)"],["shunned","(UH)"],["shuns","(UH)"],["shunt","(UH)"],["shunts","(UH)"],["shut","(UH)"],["shuts","(UH)"],["skulk","(UH)"],["skull","(UH)"],["skulls","(UH)"],["skunk","(UH)"],["skunks","(UH)"],["slough","(UH)"],["sludge","(UH)"],["slug","(UH)"],["slugged","(UH)"],["slugs","(UH)"],["slum","(UH)"],["slump","(UH)"],["slumped","(UH)"],["slums","(UH)"],["slung","(UH)"],["slush","(UH)"],["slut","(UH)"],["smudge","(UH)"],["smudged","(UH)"],["smug","(UH)"],["smut","(UH)"],["snub","(UH)"],["snubbed","(UH)"],["snuff","(UH)"],["snuffed","(UH)"],["snug","(UH)"],["some","(UH)"],["son","(UH)"],["sons","(UH)"],["son's","(UH)"],["sponge","(UH)"],["sponged","(UH)"],["sprung","(UH)"],["spud","(UH)"],["spun","(UH)"],["spunk","(UH)"],["struck","(UH)"],["strum","(UH)"],["strung","(UH)"],["strut","(UH)"],["stub","(UH)"],["stubbed","(UH)"],["stubs","(UH)"],["stuck","(UH)"],["stud","(UH)"],["studs","(UH)"],["stuff","(UH)"],["stuffed","(UH)"],["stump","(UH)"],["stumped","(UH)"],["stumps","(UH)"],["stun","(UH)"],["stung","(UH)"],["stunk","(UH)"],["stunned","(UH)"],["stunt","(UH)"],["stunts","(UH)"],["sub","(UH)"],["subs","(UH)"],["such","(UH)"],["suck","(UH)"],["sucked","(UH)"],["suds","(UH)"],["sulk","(UH)"],["sulked","(UH)"],["sulks","(UH)"],["sum","(UH)"],["summed","(UH)"],["sums","(UH)"],["sun","(UH)"],["sung","(UH)"],["sunk","(UH)"],["suns","(UH)"],["sun's","(UH)"],["sup","(UH)"],["swum","(UH)"],["swung","(UH)"],["thrum","(UH)"],["thrush","(UH)"],["thrust","(UH)"],["thrusts","(UH)"],["thud","(UH)"],["thuds","(UH)"],["thug","(UH)"],["thugs","(UH)"],["thumb","(UH)"],["thumbed","(UH)"],["thumbs","(UH)"],["thump","(UH)"],["thumped","(UH)"],["thus","(UH)"],["ton","(UH)"],["tongue","(UH)"],["tongued","(UH)"],["tongues","(UH)"],["tons","(UH)"],["touch","(UH)"],["touched","(UH)"],["tough","(UH)"],["toughs","(UH)"],["truck","(UH)"],["trucked","(UH)"],["trucks","(UH)"],["trudge","(UH)"],["trudged","(UH)"],["trump","(UH)"],["trumps","(UH)"],["trunk","(UH)"],["trunks","(UH)"],["truss","(UH)"],["trust","(UH)"],["trusts","(UH)"],["tub","(UH)"],["tubs","(UH)"],["tuck","(UH)"],["tucked","(UH)"],["tuft","(UH)"],["tufts","(UH)"],["tug","(UH)"],["tugged","(UH)"],["tush","(UH)"],["tusk","(UH)"],["tusks","(UH)"],["ugh","(UH)"],["up","(UH)"],["upped","(UH)"],["ups","(UH)"],["us","(UH)"],["was","(UH)"],["what","(UH)"],["what's","(UH)"],["won","(UH)"],["young","(UH)"],["young's","(UH)"],["bluffed","(UH)"],["BUDD","(UH)"],["budged","(UH)"],["buffed","(UH)"],["bummed","(UH)"],["bung","(UH)"],["bunged","(UH)"],["bungs","(UH)"],["bunked","(UH)"],["busk","(UH)"],["busked","(UH)"],["busks","(UH)"],["BUSS","(UH)"],["chub","(UH)"],["chubs","(UH)"],["chucked","(UH)"],["chucks","(UH)"],["chugged","(UH)"],["chugs","(UH)"],["chummed","(UH)"],["chumps","(UH)"],["chums","(UH)"],["clumped","(UH)"],["clunked","(UH)"],["clunks","(UH)"],["crumbs","(UH)"],["CRUMP","(UH)"],["crusts","(UH)"],["cuffed","(UH)"],["culled","(UH)"],["culls","(UH)"],["cunt","(UH)"],["cunts","(UH)"],["cusps","(UH)"],["cussed","(UH)"],["dost","(UH)"],["doth","(UH)"],["drub","(UH)"],["drubbed","(UH)"],["drubs","(UH)"],["drudged","(UH)"],["dubs","(UH)"],["duff","(UH)"],["duffs","(UH)"],["dunked","(UH)"],["dunks","(UH)"],["DUNN","(UH)"],["duns","(UH)"],["fluffed","(UH)"],["fluffs","(UH)"],["flunked","(UH)"],["flunks","(UH)"],["frumps","(UH)"],["fuck","(UH)"],["fucked","(UH)"],["fucks","(UH)"],["fudged","(UH)"],["fug","(UH)"],["fugs","(UH)"],["funked","(UH)"],["funks","(UH)"],["fussed","(UH)"],["gluts","(UH)"],["GRUBB","(UH)"],["grubbed","(UH)"],["grudged","(UH)"],["grunts","(UH)"],["gulfs","(UH)"],["gulls","(UH)"],["gummed","(UH)"],["gunge","(UH)"],["HOUGH","(UH)"],["HUCK","(UH)"],["huffed","(UH)"],["huffs","(UH)"],["hugs","(UH)"],["hulled","(UH)"],["hulls","(UH)"],["humps","(UH)"],["hums","(UH)"],["hunks","(UH)"],["Huns","(UH)"],["husked","(UH)"],["husks","(UH)"],["jugs","(UH)"],["junked","(UH)"],["KLUX","(UH)"],["Ludd","(UH)"],["lugs","(UH)"],["lunched","(UH)"],["mucked","(UH)"],["mucks","(UH)"],["muds","(UH)"],["muffed","(UH)"],["muffs","(UH)"],["mulct","(UH)"],["mulcts","(UH)"],["mulled","(UH)"],["mulls","(UH)"],["mums","(UH)"],["mussed","(UH)"],["MUSTS","(UH)"],["mutts","(UH)"],["nubs","(UH)"],["numbed","(UH)"],["numbs","(UH)"],["plucks","(UH)"],["plumbs","(UH)"],["plumps","(UH)"],["plums","(UH)"],["plunk","(UH)"],["plunks","(UH)"],["pucks","(UH)"],["pug","(UH)"],["pugs","(UH)"],["pulped","(UH)"],["pulps","(UH)"],["puns","(UH)"],["punts","(UH)"],["putts","(UH)"],["roughs","(UH)"],["rubs","(UH)"],["ruck","(UH)"],["rucked","(UH)"],["ruff","(UH)"],["ruffed","(UH)"],["ruffs","(UH)"],["rumps","(UH)"],["rungs","(UH)"],["runts","(UH)"],["rusks","(UH)"],["rusts","(UH)"],["scrubs","(UH)"],["scruffs","(UH)"],["scrum","(UH)"],["scrums","(UH)"],["scrunched","(UH)"],["scuds","(UH)"],["scuffed","(UH)"],["scuffs","(UH)"],["sculled","(UH)"],["sculls","(UH)"],["sculpts","(UH)"],["scut","(UH)"],["scuts","(UH)"],["shoves","(UH)"],["shrunk","(UH)"],["shucked","(UH)"],["skulked","(UH)"],["skulks","(UH)"],["skunked","(UH)"],["sloughs","(UH)"],["slummed","(UH)"],["slumps","(UH)"],["slunk","(UH)"],["sluts","(UH)"],["smuts","(UH)"],["snubs","(UH)"],["SNUCK","(UH)"],["snuffs","(UH)"],["sough","(UH)"],["soughed","(UH)"],["soughs","(UH)"],["spuds","(UH)"],["strummed","(UH)"],["strums","(UH)"],["struts","(UH)"],["STUBBS","(UH)"],["stuffs","(UH)"],["stuns","(UH)"],["subbed","(UH)"],["sucks","(UH)"],["sump","(UH)"],["sumps","(UH)"],["sunned","(UH)"],["supped","(UH)"],["sups","(UH)"],["SUS","(UH)"],["thrummed","(UH)"],["thrums","(UH)"],["thumps","(UH)"],["tonne","(UH)"],["tonnes","(UH)"],["trumped","(UH)"],["trussed","(UH)"],["tucks","(UH)"],["tugs","(UH)"],["tun","(UH)"],["tuns","(UH)"],["tup","(UH)"],["tups","(UH)"],["tut","(UH)"],["tuts","(UH)"],["UH","(UH)"],["UM","(UH)"],["wrung","(UH)"],["be","(EE)"],["beach","(EE)"],["bead","(EE)"],["beads","(EE)"],["beak","(EE)"],["beam","(EE)"],["beams","(EE)"],["bean","(EE)"],["beans","(EE)"],["beast","(EE)"],["beasts","(EE)"],["beat","(EE)"],["beats","(EE)"],["bee","(EE)"],["beech","(EE)"],["beef","(EE)"],["beefed","(EE)"],["beef's","(EE)"],["been","(EE)"],["beep","(EE)"],["beeps","(EE)"],["bees","(EE)"],["bee's","(EE)"],["beet","(EE)"],["beets","(EE)"],["bleach","(EE)"],["bleached","(EE)"],["bleak","(EE)"],["bleat","(EE)"],["bleats","(EE)"],["bleed","(EE)"],["bleeds","(EE)"],["bleep","(EE)"],["bleeps","(EE)"],["breach","(EE)"],["breathe","(EE)"],["breathed","(EE)"],["breathes","(EE)"],["breech","(EE)"],["breed","(EE)"],["breeds","(EE)"],["breed's","(EE)"],["breeze","(EE)"],["Brie","(EE)"],["brief","(EE)"],["briefed","(EE)"],["briefs","(EE)"],["cease","(EE)"],["ceased","(EE)"],["cede","(EE)"],["cheap","(EE)"],["cheat","(EE)"],["cheek","(EE)"],["cheeks","(EE)"],["cheep","(EE)"],["cheese","(EE)"],["chic","(EE)"],["chief","(EE)"],["chiefs","(EE)"],["chief's","(EE)"],["clean","(EE)"],["cleaned","(EE)"],["cleans","(EE)"],["cleat","(EE)"],["cleave","(EE)"],["cleaved","(EE)"],["clique","(EE)"],["cliques","(EE)"],["creak","(EE)"],["creaked","(EE)"],["creaks","(EE)"],["cream","(EE)"],["creamed","(EE)"],["creams","(EE)"],["crease","(EE)"],["creased","(EE)"],["creed","(EE)"],["creeds","(EE)"],["creek","(EE)"],["creeks","(EE)"],["creep","(EE)"],["creeps","(EE)"],["deal","(EE)"],["deals","(EE)"],["dean","(EE)"],["deans","(EE)"],["dean's","(EE)"],["deed","(EE)"],["deeds","(EE)"],["deem","(EE)"],["deemed","(EE)"],["deep","(EE)"],["deeps","(EE)"],["dream","(EE)"],["dreamed","(EE)"],["dreams","(EE)"],["each","(EE)"],["eared","(EE)"],["ease","(EE)"],["eased","(EE)"],["east","(EE)"],["eat","(EE)"],["eats","(EE)"],["eel","(EE)"],["eked","(EE)"],["eve","(EE)"],["feast","(EE)"],["feasts","(EE)"],["feat","(EE)"],["feats","(EE)"],["fee","(EE)"],["feed","(EE)"],["feeds","(EE)"],["feel","(EE)"],["feels","(EE)"],["fees","(EE)"],["feet","(EE)"],["Fiat","(EE)"],["Fiats","(EE)"],["fief","(EE)"],["field","(EE)"],["fields","(EE)"],["field's","(EE)"],["fiend","(EE)"],["flea","(EE)"],["fleas","(EE)"],["flee","(EE)"],["fleece","(EE)"],["flees","(EE)"],["fleet","(EE)"],["fleets","(EE)"],["fleet's","(EE)"],["freak","(EE)"],["freaks","(EE)"],["free","(EE)"],["freed","(EE)"],["freer","(EE)"],["frees","(EE)"],["freeze","(EE)"],["frieze","(EE)"],["geese","(EE)"],["gene","(EE)"],["genes","(EE)"],["gleam","(EE)"],["gleamed","(EE)"],["glean","(EE)"],["gleaned","(EE)"],["glee","(EE)"],["glees","(EE)"],["grease","(EE)"],["greased","(EE)"],["Greece","(EE)"],["greed","(EE)"],["Greek","(EE)"],["Greeks","(EE)"],["green","(EE)"],["greens","(EE)"],["green's","(EE)"],["greet","(EE)"],["greets","(EE)"],["grief","(EE)"],["grieve","(EE)"],["he","(EE)"],["heal","(EE)"],["healed","(EE)"],["heap","(EE)"],["heaped","(EE)"],["heaps","(EE)"],["heat","(EE)"],["heat's","(EE)"],["heave","(EE)"],["heaved","(EE)"],["heaves","(EE)"],["he'd","(EE)"],["heed","(EE)"],["heel","(EE)"],["heels","(EE)"],["he'll","(EE)"],["he's","(EE)"],["jeans","(EE)"],["jeep","(EE)"],["keel","(EE)"],["keen","(EE)"],["keep","(EE)"],["keeps","(EE)"],["Keith","(EE)"],["Keith's","(EE)"],["key","(EE)"],["keyed","(EE)"],["keys","(EE)"],["knead","(EE)"],["knee","(EE)"],["kneel","(EE)"],["kneeled","(EE)"],["kneels","(EE)"],["knees","(EE)"],["leach","(EE)"],["lead","(EE)"],["leads","(EE)"],["leaf","(EE)"],["leafed","(EE)"],["league","(EE)"],["leagued","(EE)"],["leagues","(EE)"],["league's","(EE)"],["leak","(EE)"],["leaked","(EE)"],["leaks","(EE)"],["lean","(EE)"],["leaned","(EE)"],["leans","(EE)"],["leap","(EE)"],["leaps","(EE)"],["lease","(EE)"],["leased","(EE)"],["leash","(EE)"],["least","(EE)"],["leave","(EE)"],["leaves","(EE)"],["leech","(EE)"],["leek","(EE)"],["Lee's","(EE)"],["liege","(EE)"],["lien","(EE)"],["liens","(EE)"],["me","(EE)"],["mead","(EE)"],["meal","(EE)"],["meals","(EE)"],["mean","(EE)"],["means","(EE)"],["meat","(EE)"],["meats","(EE)"],["meek","(EE)"],["meet","(EE)"],["meets","(EE)"],["Neal","(EE)"],["neat","(EE)"],["need","(EE)"],["needs","(EE)"],["niece","(EE)"],["paean","(EE)"],["paeans","(EE)"],["pea","(EE)"],["peace","(EE)"],["peach","(EE)"],["peak","(EE)"],["peaked","(EE)"],["peaks","(EE)"],["peal","(EE)"],["peals","(EE)"],["peas","(EE)"],["peat","(EE)"],["pee","(EE)"],["peed","(EE)"],["peek","(EE)"],["peeked","(EE)"],["peel","(EE)"],["peeled","(EE)"],["peels","(EE)"],["peep","(EE)"],["peeve","(EE)"],["Pete","(EE)"],["Pete's","(EE)"],["piece","(EE)"],["pique","(EE)"],["plea","(EE)"],["plead","(EE)"],["pleads","(EE)"],["pleas","(EE)"],["please","(EE)"],["pleased","(EE)"],["pleat","(EE)"],["pleats","(EE)"],["preach","(EE)"],["preached","(EE)"],["preen","(EE)"],["priest","(EE)"],["priests","(EE)"],["priest's","(EE)"],["queen","(EE)"],["queens","(EE)"],["queen's","(EE)"],["quiche","(EE)"],["reach","(EE)"],["reached","(EE)"],["read","(EE)"],["reads","(EE)"],["read's","(EE)"],["real","(EE)"],["ream","(EE)"],["reams","(EE)"],["reap","(EE)"],["reaped","(EE)"],["reed","(EE)"],["reef","(EE)"],["reefs","(EE)"],["reek","(EE)"],["reeked","(EE)"],["reel","(EE)"],["reeled","(EE)"],["reels","(EE)"],["scene","(EE)"],["scenes","(EE)"],["scheme","(EE)"],["schemes","(EE)"],["scream","(EE)"],["screamed","(EE)"],["screams","(EE)"],["screech","(EE)"],["screeched","(EE)"],["screen","(EE)"],["screened","(EE)"],["screens","(EE)"],["sea","(EE)"],["seal","(EE)"],["sealed","(EE)"],["seals","(EE)"],["seam","(EE)"],["seams","(EE)"],["seas","(EE)"],["sea's","(EE)"],["seat","(EE)"],["seats","(EE)"],["see","(EE)"],["seed","(EE)"],["seeds","(EE)"],["seek","(EE)"],["seeks","(EE)"],["seem","(EE)"],["seemed","(EE)"],["seems","(EE)"],["seen","(EE)"],["seep","(EE)"],["seeped","(EE)"],["sees","(EE)"],["seethe","(EE)"],["seize","(EE)"],["seized","(EE)"],["she","(EE)"],["Shea","(EE)"],["sheaf","(EE)"],["Shea's","(EE)"],["sheath","(EE)"],["sheathe","(EE)"],["she'd","(EE)"],["sheen","(EE)"],["sheep","(EE)"],["sheet","(EE)"],["sheets","(EE)"],["sheik","(EE)"],["sheikh","(EE)"],["she'll","(EE)"],["she's","(EE)"],["shield","(EE)"],["shields","(EE)"],["shriek","(EE)"],["shrieked","(EE)"],["siege","(EE)"],["sikh","(EE)"],["skeet","(EE)"],["ski","(EE)"],["skier","(EE)"],["skis","(EE)"],["sleek","(EE)"],["sleep","(EE)"],["sleeps","(EE)"],["sleet","(EE)"],["sleeve","(EE)"],["sleeves","(EE)"],["sneak","(EE)"],["sneaked","(EE)"],["sneaks","(EE)"],["sneeze","(EE)"],["sneezed","(EE)"],["speak","(EE)"],["speaks","(EE)"],["speech","(EE)"],["speed","(EE)"],["speeds","(EE)"],["spiel","(EE)"],["spleen","(EE)"],["spree","(EE)"],["squeak","(EE)"],["squeaked","(EE)"],["squeal","(EE)"],["squealed","(EE)"],["squeals","(EE)"],["squeeze","(EE)"],["squeezed","(EE)"],["steal","(EE)"],["steals","(EE)"],["steam","(EE)"],["steamed","(EE)"],["steed","(EE)"],["steel","(EE)"],["steeled","(EE)"],["steels","(EE)"],["steep","(EE)"],["steeped","(EE)"],["Steve","(EE)"],["streak","(EE)"],["streaked","(EE)"],["streaks","(EE)"],["stream","(EE)"],["streamed","(EE)"],["streams","(EE)"],["stream's","(EE)"],["street","(EE)"],["streets","(EE)"],["street's","(EE)"],["suite","(EE)"],["suites","(EE)"],["suite's","(EE)"],["Swedes","(EE)"],["sweep","(EE)"],["sweet","(EE)"],["sweets","(EE)"],["tea","(EE)"],["teach","(EE)"],["teal","(EE)"],["team","(EE)"],["teamed","(EE)"],["teams","(EE)"],["team's","(EE)"],["teas","(EE)"],["tease","(EE)"],["teased","(EE)"],["teat","(EE)"],["teats","(EE)"],["tee","(EE)"],["teem","(EE)"],["teems","(EE)"],["teen","(EE)"],["teens","(EE)"],["teeth","(EE)"],["teethe","(EE)"],["thee","(EE)"],["theme","(EE)"],["themes","(EE)"],["these","(EE)"],["thief","(EE)"],["thieve","(EE)"],["thieves","(EE)"],["three","(EE)"],["threes","(EE)"],["treat","(EE)"],["treats","(EE)"],["tree","(EE)"],["trees","(EE)"],["tweak","(EE)"],["tweed","(EE)"],["tweet","(EE)"],["tweezed","(EE)"],["veal","(EE)"],["we","(EE)"],["weak","(EE)"],["wean","(EE)"],["weaned","(EE)"],["weave","(EE)"],["weaves","(EE)"],["we'd","(EE)"],["wee","(EE)"],["weed","(EE)"],["weeds","(EE)"],["week","(EE)"],["weeks","(EE)"],["week's","(EE)"],["weep","(EE)"],["we'll","(EE)"],["we've","(EE)"],["wheat","(EE)"],["wheel","(EE)"],["wheeled","(EE)"],["wheels","(EE)"],["wheeze","(EE)"],["wheezed","(EE)"],["wield","(EE)"],["wreak","(EE)"],["wreath","(EE)"],["wreathe","(EE)"],["wreathed","(EE)"],["wreaths","(EE)"],["ye","(EE)"],["yeast","(EE)"],["yeasts","(EE)"],["yield","(EE)"],["yields","(EE)"],["zeal","(EE)"],["aeon","(EE)"],["aeons","(EE)"],["BEA","(EE)"],["beached","(EE)"],["beaks","(EE)"],["BEALE","(EE)"],["beamed","(EE)"],["BEDE","(EE)"],["beefs","(EE)"],["beeves","(EE)"],["BEHAN","(EE)"],["BEIN","(EE)"],["BETE","(EE)"],["BIERCE","(EE)"],["biers","(EE)"],["bleeped","(EE)"],["breached","(EE)"],["bream","(EE)"],["breams","(EE)"],["breezed","(EE)"],["breve","(EE)"],["breves","(EE)"],["CAIUS","(EE)"],["cedes","(EE)"],["CEIL","(EE)"],["cheats","(EE)"],["cheeked","(EE)"],["cheeped","(EE)"],["cheeps","(EE)"],["chine","(EE)"],["cleats","(EE)"],["cleaves","(EE)"],["creel","(EE)"],["creels","(EE)"],["CYR","(EE)"],["DEANE","(EE)"],["deems","(EE)"],["DERE","(EE)"],["e","(EE)"],["e'en","(EE)"],["e's","(EE)"],["EADES","(EE)"],["EAVE","(EE)"],["eaves","(EE)"],["EEG","(EE)"],["eels","(EE)"],["eves","(EE)"],["FICHE","(EE)"],["fiefs","(EE)"],["fiends","(EE)"],["fleeced","(EE)"],["freaked","(EE)"],["Freese","(EE)"],["gee","(EE)"],["GEE'S","(EE)"],["ghee","(EE)"],["GIDE","(EE)"],["gleams","(EE)"],["gleans","(EE)"],["glebe","(EE)"],["glebes","(EE)"],["greaves","(EE)"],["grebe","(EE)"],["grebes","(EE)"],["GREENE","(EE)"],["griefs","(EE)"],["grieved","(EE)"],["grieves","(EE)"],["grippe","(EE)"],["GRIS","(EE)"],["heals","(EE)"],["heath","(EE)"],["heaths","(EE)"],["heats","(EE)"],["HEE","(EE)"],["heeds","(EE)"],["heeled","(EE)"],["IL","(EE)"],["JE","(EE)"],["jean","(EE)"],["JEE","(EE)"],["jeeps","(EE)"],["KEANE","(EE)"],["keels","(EE)"],["KEENE","(EE)"],["keened","(EE)"],["keens","(EE)"],["KLEES","(EE)"],["kneads","(EE)"],["kneed","(EE)"],["lea","(EE)"],["leached","(EE)"],["leafs","(EE)"],["leal","(EE)"],["leas","(EE)"],["leaved","(EE)"],["lee","(EE)"],["LEEDS","(EE)"],["leeks","(EE)"],["lees","(EE)"],["LEET","(EE)"],["LEIGH","(EE)"],["lief","(EE)"],["LIGNE","(EE)"],["MEA","(EE)"],["meads","(EE)"],["meed","(EE)"],["meeds","(EE)"],["meres","(EE)"],["mi","(EE)"],["mien","(EE)"],["miens","(EE)"],["NE","(EE)"],["neap","(EE)"],["neaps","(EE)"],["NEIL","(EE)"],["OUI","(EE)"],["peached","(EE)"],["PEALE","(EE)"],["pealed","(EE)"],["peeks","(EE)"],["peeped","(EE)"],["peeps","(EE)"],["pees","(EE)"],["peeved","(EE)"],["peeves","(EE)"],["peke","(EE)"],["pekes","(EE)"],["pieced","(EE)"],["piqued","(EE)"],["piques","(EE)"],["pleach","(EE)"],["pleached","(EE)"],["preened","(EE)"],["preens","(EE)"],["prink","(EE)"],["prinked","(EE)"],["prinks","(EE)"],["PRIX","(EE)"],["quay","(EE)"],["quays","(EE)"],["quean","(EE)"],["queans","(EE)"],["queened","(EE)"],["QUI","(EE)"],["re","(EE)"],["reaps","(EE)"],["reeds","(EE)"],["reefed","(EE)"],["reeks","(EE)"],["REES","(EE)"],["REESE","(EE)"],["reeve","(EE)"],["reeves","(EE)"],["REID","(EE)"],["rhea","(EE)"],["rheas","(EE)"],["RHEIMS","(EE)"],["rive","(EE)"],["schemed","(EE)"],["SCHIELE","(EE)"],["scree","(EE)"],["screed","(EE)"],["screeds","(EE)"],["screes","(EE)"],["SCRIM","(EE)"],["seamed","(EE)"],["seeps","(EE)"],["seethed","(EE)"],["seethes","(EE)"],["sheathed","(EE)"],["sheathes","(EE)"],["sheaths","(EE)"],["sheaves","(EE)"],["sheers","(EE)"],["sheikhs","(EE)"],["SHIH","(EE)"],["shrieks","(EE)"],["si","(EE)"],["SIE","(EE)"],["Sikhs","(EE)"],["skied","(EE)"],["skiers","(EE)"],["sleeked","(EE)"],["sleeks","(EE)"],["sleets","(EE)"],["SNEAD","(EE)"],["SNEED","(EE)"],["SPEER","(EE)"],["spieled","(EE)"],["spiels","(EE)"],["spleens","(EE)"],["sprees","(EE)"],["squeaks","(EE)"],["Sri","(EE)"],["steams","(EE)"],["steeds","(EE)"],["STEELE","(EE)"],["STEELE'S","(EE)"],["steeps","(EE)"],["STEEVES","(EE)"],["swede","(EE)"],["sweeps","(EE)"],["teak","(EE)"],["teed","(EE)"],["teemed","(EE)"],["tees","(EE)"],["teethed","(EE)"],["teethes","(EE)"],["thieved","(EE)"],["Ti","(EE)"],["TIECK","(EE)"],["TREECE","(EE)"],["treed","(EE)"],["tweaked","(EE)"],["tweaks","(EE)"],["twee","(EE)"],["tweeds","(EE)"],["tweets","(EE)"],["VIVE","(EE)"],["weal","(EE)"],["Weald","(EE)"],["weals","(EE)"],["weans","(EE)"],["weaved","(EE)"],["weeps","(EE)"],["wees","(EE)"],["WHEE","(EE)"],["wields","(EE)"],["wreaked","(EE)"],["wreaks","(EE)"],["wreathes","(EE)"],["zee","(EE)"],["zees","(EE)"] ]

#get list of ee_uh_words without the phoneme as a tuple
ee_uh = [x[0] for x in ee_uh_words]
ee_uh = [x.lower() for x in ee_uh]

test_counter = 0

#print(ee_uh)
#GET https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=surfing&key=[YOUR_API_KEY] HTTP/1.1


for link in range(0,len(video_link_list)):

    test_counter += 1

    video_link = video_link_list[link]  
    
    try:
        root = YouTubeTranscriptApi.get_transcript(video_id_list[link])
    except:
        root = "fail"

    if(root != "fail"):
        word_found = False
        which_word = "###"
        clip_number = 1
        for child in root:  
            transcript_section = child['text'].lower().split()

            #begin downloading and clipping a video if a word from the list is found in the video's transcript
            if(any(word in transcript_section for word in ee_uh)):
                
                print("target word found")

                print("Video Link Array Index: " + str(link))

                #get which word and phoneme was said in the clip
                phoneme = ""
                word_index = 0
                for word in ee_uh:
                    if(word in transcript_section):
                        phoneme = ee_uh_words[word_index][1]
                        which_word = word
                    word_index += 1

                #for the first instance of a word being found, download the current video
                if(word_found == False):
                    yt = YouTube(video_link)
                    video_title = yt.title
                    video_title = "".join( x for x in video_title if (x.isalnum() or x in "._- ")) #remove illegal characters from filename
                    video_filename = video_title + ".mp4"
                    #yt.streams.first().download()
                    download_video = yt.streams.filter(progressive = True, file_extension = "mp4").first().download(filename=video_filename)
                    word_found = True

                #find the start and ending times of each transcript portion with a target word
                start = int(float(child['start']))
                end = int(float(child['duration'])) + start

                print("Initial start and end: " + str(start) + " | " + str(end))
                

                clip = VideoFileClip(video_filename)

                #case where clip is at the end of the video and the duration is rounded up when converting to an int
                duration = clip.duration
                print("duration: " + str(duration))
                if(duration < end):
                    print("test")
                    end = end-2
                    print("test2")
                    start = start - 4
                if(start == end):
                    start = start -1

                print("After comparison start and end: " + str(start) + " | " + str(end))

                clip = clip.subclip(start, end)

                #name file with video's title, the target word found, and number of clip within an individual video 
                clip_name = phoneme + "-(" + which_word + ")_" + video_title + "_clip" + str(clip_number) + ".mp4"
                clip_number += 1
                folder_name = video_title

                #write file that will contain video and audio
                
                clip.write_videofile(clip_name, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")
                #print(unescape(child.text), int(float(child.attrib['start'])), "\n")

                clip.close()

                #if a face is detected for at least 80% of the video
                if(faceDetect(clip_name)):
                    saveClip(clip_name,folder_name,phoneme)
                else:
                    removeFile = os.getcwd() + '/' + clip_name
                    if(os.path.isfile(removeFile)):
                        os.remove(removeFile)


        
        #remove full length downloaded video
        try:
            removeFile = os.getcwd() + '/' + video_filename
        except:
            print("video did not contain any of the target words")
            video_filename = None
        else:
            if(os.path.isfile(removeFile)):
                os.remove(removeFile)

#Print number of links analyzed and total elapsed time of script
end = time.time()
print("Number of videos analyzed:")
print(test_counter)
print("Elapsed Time:")
print(end - start)
