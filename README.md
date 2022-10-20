# Bountiful-Mushrooms


## Overview
Bountiful Mushrooms is an application that can be used as a source of information for anyone trying to intrested in identifing and learning about different strains of mushrooms. to help with this i'll be using Django, vue and TBD
</br>
## Functionality
- Create, Login, and view user profile
- Map of where strains are around the PNW and get informantion on the certain mushroom
- Being able to post information and a brief discription of what they found, possibly a photo upload
- backend shit
---
</br>

### Data ***model***
</br> 
- users- created date
- updated date
- pictures?

|Variable|Field Type|Properties|
|--------|---------|---------|
|username| CharField|max_length=23,unique=True|
|title | Charfield| max length = 50
|user    |Foriegnkey|null=True|
|image| URLfield| max_length=50    |
|is_superuser|BooleanField|default=False|
|date |DateTimeField| auto_now = True
|Location|models.Char.Field | max_length=50 
</br>
## Schedule
- Week 1 - search API or how to build one, if api is f``ound learn how to use it. start backend work how it needs to look 
    if building an API research information about certain mushrooms and locations as well as learn how to add to a map
- Week 2 -connect to front end to back end
- Week 3 -  Focus on styling and trouble shooting anything that was missed or not working


https://mushroomobserver.org/activity_logs/
https://gps-coordinates.org/latitude-and-longitude.php