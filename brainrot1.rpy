init -990 python in mas_submod_utils:
    ei_submod = Submod(
        author="plutonium12345",
        name="brainrot dialogue",
        description=(
            "what the sigma"
        ),
        version="1.0.0"
    )
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_brainrot1", # event label (MUST BE UNIQUE)
            category=["misc", "society"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Brainrot", # button text
            random=False, # True if this topic should appear randomly
            pool=True, # True if this topic should appear in "Ask a Question"
            unlocked=True,
        )
    )

label monika_brainrot1:
    m 1esa "Hey, [player]."
    m 1esd "I've been searching the web recently and I came across something called 'brainrot'."
    m 4rtd "If I understand correctly, it seems to be some sort of...absurdist humor?"
    m 5wsb "I'm assuming you're more familiar with internet lingo than I am, have you heard of this?"
menu:
        m "I'm assuming you're more familiar with internet lingo than I am, have you heard of this?{fast}"

        "I LOVE BRAINROT":
            m 5wuo "Wow, you seem really passionate about this! I suppose it is an interesting piece of internet culture."
            m 5hud "Surprise is an important element of comedy, and this style has it in spades."
            m 5rud "It's also a very organic, cultural form of humor - shaped by current events and trends."

        "I've heard of it before.":
            m 1hkb "Ah, I thought so - it seems to be a pretty popular topic nowadays."
            m 5ekb "The concept is a bit foreign to me, but I suppose it is an interesting piece of internet culture."
            m 5wuo "It's a bit controversial, with some finding it hilarious and others finding it annoying and repetitive."
            m 1tuc "Quite frankly, I don't know what to make of it."

        "brainrot???":
            m 1euc "Haha, I guess it may not be as well-known as I thought."
            m 1hud "I don't know much about it either, but I believe it's a style of humor driven by intentional absurdism and repetition."
            m 1wud "This style of humor seems to have been popularised by the internet, though obviously absurdism in comedy is nothing new."
            m 1tuc "Quite frankly, I don't know what to make of it."

        "I'm familiar with it, and I think it's stupid.":
            m 1hub "Well, I guess that style of humor isn't for everyone. It can seem a bit repetitive at times and some people prefer a more structured, witty joke."
            m 1eub "Responses to this kind of joke can even seem somewhat pavlovian. When the same soundbyte is repeated over multiple funny shorts/memes, your brain is primed to associate the sound with the feeling of laughter."
            m 1etp "A good example of this would be the 'among us' joke, which began during the pandemic."
            m 1etp "While originally referring to the video game of the same name, it would sometimes be inserted into completely unrelated jokes for supposedly no reason."
            m 4gtp "Even though there was nothing particularly clever about the inclusion of 'among us', it drew on a shared cultural understanding that said phrase was considered funny."
            m 6etd "Memes can also evolve in meaning over time. While 'skibidi' was originally just a referencing a viral song,"
            m 6eud "it is now more commonly used in the context of 'skibidi toilet'(a youtube webseries) or as an all purpose nonsense word."
            m 2eud "Even if I don't find it particularly funny, it still interests me."
return
