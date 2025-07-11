init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_languagestudy",
            category=["literature"],
            prompt="The study of language.",
            pool=True,
            unlocked=True,
        )
    )

label monika_languagestudy:
    m 1eua "[player], have you heard of etymology?"
    m 1hua "It's often confused for entomology, which is actually the study of insects."
    m 1hub "Etymology, however, is the study of language."
    m 4rub "My interest in literature is actually what led me to research this topic."
    m 1eub "Of course the two are not interchangable, but they are related."
    m 1sua "It's quite interesting how language can be shaped by culture and history."
return
