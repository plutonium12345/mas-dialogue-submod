init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_dinosaurs",category=['science','misc'],prompt="Dinosaurs",random=False,pool=True,unlocked=True,))

label monika_dinosaurs:
    m 1etd "Did you ever have a dinosaur phase?"
    m 1esa "It's pretty common among young children."
    m 7hud "After all, what's not to like?"
    m 7wsb "Huge lizards roaming the earth, fighting for dominance and survival."
    m 2eub "It almost seems like a fantasy world. No wonder it appeals to their underdeveloped brains."
    m 2rua "There was so much variety too, with unique species in land, sea, and air."
    m 1dkb "Well, not all of these species were technically dinosaurs. I suppose a more accurate description would be 'prehistoric life'."
    m 1sua "Herbivores and carnivores, bipedal and quadrupedal, a wild beautiful world full of life."
    m 5wkd "They're all gone."
    m 5duo "And they never even saw it coming."
    m 5eud "They were just going about their day as usual. There was nothing out of the ordinary."
    m 5euc "Suddenly everything they ever knew was gone in an instant."
    m 3fua "It reminds me of that phrase that was popular a while ago. 'YOLO', I think?"
    m 3rua "You never know if you'll see another day, so you should live your life to the fullest."
    m 1tub "It's kind of childish, but...do you have a favorite dinosaur?"
    $ fav_dino = renpy.input("Favorite Dinosaur")
    m 5sub "Oh wow, that's a cool one!"
    m 5hub "My favorite is the Mosasaurus."
    m 3wub "The Mosasaurus was a marine reptile that lived in rivers. It was the 'type genus' of mosasaurs, basically the main example of that group."
    m 1eua "There's something awe-inspiring about creatures that massive living on the same planet we do now."
    m 1fua "It's a reminder of how fleeting everything can be... and how incredible life is, even in extinction."
    m 5hua "Thanks for talking with me about this, [player]. I love how you make me feel alive."
return "love"
