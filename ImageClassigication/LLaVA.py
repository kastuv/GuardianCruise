# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-uEgU_Hq3wQnPZ-pVFWz9dRUUhwlby06
"""

#pip install replicate

#r8_SWp24LJcA2yFiXklelFnK6puztNtxjv20hxYk

# Commented out IPython magic to ensure Python compatibility.
# %env REPLICATE_API_TOKEN= r8_SWp24LJcA2yFiXklelFnK6puztNtxjv20hxYk
import cohereNegativityClassification
import replicate
import base64

def jpg_to_data_uri(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        image_binary = image_file.read()

        # Encode the image data as base64
        base64_encoded_image = base64.b64encode(image_binary).decode('utf-8')

        # Construct the data URI
        data_uri = f"data:image/jpeg;base64,{base64_encoded_image}"

    return data_uri
big_list_prompt = """

Eyes:

Droopy or heavy eyelids
Frequent blinking
Red or watery eyes
Difficulty keeping eyes open
Facial Expression:
\n
Yawning
Blank or unfocused stare
Slow or delayed responses to questions
Body Language:
\n
Slouched posture
Restlessness or fidgeting
Slow movements
Nodding off or head bobbing
Speech:
\n
Slurred speech
Monotone or lack of inflection
Incoherent or disjointed responses
Behavioral Cues:
\n
Difficulty staying awake or alert
Difficulty concentrating or maintaining attention
Lack of awareness of surroundings
Microsleep episodes (brief, involuntary periods of sleep)
Physical Signs:
\n
Fatigue-related signs such as rubbing eyes or face
Appearing disoriented or confused
Excessive yawning or stretching
Reaction Time:
\n
Delayed reactions to external stimuli
Slow responses to instructions or commands
External Factors:
\n
Time of day (late at night or early morning)
Previous activities (e.g., driving long distances)


"""
def getInfo(src):


    output = replicate.run(
        "yorickvp/llava-13b:e272157381e2a3bf12df3a8edd1f38d1dbd736bbb7437277c8b34175f8fce358",
        input={
            "image": jpg_to_data_uri(src),
            "top_p": 1,
            "prompt": "Does the driver appear to be physically safe",
            "max_tokens": 150,
            "temperature": 0.2
        }
    )

    print(' '.join(output))
    return ' '.join(output)