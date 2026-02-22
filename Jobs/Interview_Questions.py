company_name = input("Company Name: ")

# interviewer questions
interviewer_questions = {
    f"Why do you want to work at {company_name}?": "I want to work in a fresh environment because I can use my "
                                                   "experience to learn new technologies and further learn how to "
                                                   "adapt to new challenges while having more growth opportunities",

    f"What made you want to apply at {company_name}?": "I want to work for a company that has been thriving for "
                                                       "decades and is on a strong sustainable path of growth, "
                                                       "I currently don't see that where I am right now, "
                                                       "so that's why it's time for me to move on.",

    f"Why are you looking for a new role?": "I am looking for a new role because I've done great things in my "
                                            "current role, but I want to broaden my knowledge and continue to learn "
                                            "good software engineering practices, along with getting the change to "
                                            "work on different projects and learn in a fresh environment",

    f"What got you interested in software engineering?": "I studied mechanical engineering in college and really "
                                                         "enjoyed it, I ended up working in that field for a few "
                                                         "years but I didn't find it as fulfilling as I had hoped. I "
                                                         "would go to sites, look at the mechanical systems and then "
                                                         "go home and write my reports. There would be a lack of "
                                                         "human interaction most days and it got to me mentally. Then "
                                                         "my friend convinced me that I should try software "
                                                         "engineering because I can start from a blank slate, "
                                                         "and build whatever I want. I started writing basic scripts "
                                                         "to automate daily tasks such as writing reports in my "
                                                         "mechanical engineering roles, and eventually I started "
                                                         "working for a software engineering startup, which "
                                                         "eventually led me to my current role.",

    f"What are you looking for in your next role?": (
        # mention it directly being the role you are applying for
        "I'm looking to continue working in fintech, in a fast moving environment where coding is the main work task "
        "typically done throughout the day",

        "I'm really passionate about being fully invested in the work I do. When it comes to projects, "
        "I always strive to take ownership and drive them towards success. This is why I want to join a new project "
        "and take ownership"
    ),

    f"What do you typically do during the day at your current role?": "At Axoni what I am working now is called the "
                                                                      "Veris project, this project is a cllient-facing "
                                                                      "platform where clients such as big banks can "
                                                                      "perform equity swaps, and other trades. My "
                                                                      "current role for this project is to work on "
                                                                      "the backend by developing APIs for the "
                                                                      "transactions, optimizing database queries for "
                                                                      "the different types of trades, and make sure "
                                                                      "that all functions of an equity swap work as "
                                                                      "expected. I also help out with the frontend by "
                                                                      "working with the design team to develop "
                                                                      "user-friendly interfaces with easy to find "
                                                                      "functions",

    f"Why are you looking for a fintech role?": "I'm looking for a fintech role because I want to mix my love for "
                                                "coding and interest in financial services such as trades and looking "
                                                "at equities. I am drawn to the fast-paced nature of fintech, "
                                                "and I want to continue my career working in this industry",

    f"In a few sentences, describe why you think you would be a good fit"
    f" at {company_name} or why you are interested in {company_name}.": "I think I would be a good fit at ___ because "
                                                                        "I want to continue to learn at a fintech "
                                                                        "company. I enjoy my current role, "
                                                                        "but I want to work somewhere with new "
                                                                        "projects, and new technology to learn about.",

    f"how do you practice agile methodology?": "we have stand-ups at least once a week where we go over what we have "
                                               "done since the previous standup and what we are working or will start "
                                               "to work on. Our sprints are weekly but sometimes when we have a "
                                               "deadline or major project coming up we have stand-ups more often ",

    f"where do you see yourself in 5 years": "In 5 years I see myself as a senior software engineer working on a "
                                             "project that I care about, with a team that usually has a smile on "
                                             "their face and is also passionate about their work",

    f"how would a typical day right before you retire be like?": "I am imagining it is the Tuesday morning before I "
                                                                 "will retire. I am waking up early, smiling as I'm "
                                                                 "thinking of how work will go today. Once I get to "
                                                                 "work I greet my coworkers and chat for a bit over "
                                                                 "things not related to work. After that we continue "
                                                                 "on our work from the previous day up until lunch. I "
                                                                 "have lunch with my coworkers and we discuss what we "
                                                                 "have been working on and if anyone needs any help. "
                                                                 "We then work in a more collaborative environment "
                                                                 "for the rest of the day, making sure that every "
                                                                 "question has an answer, and nobody is confused on "
                                                                 "the work they are doing.",

    f"do you have any personal projects you’re "
    f"working on to keep learning tech?": "I have my net worth project which I update as soon as I learn a new "
                                          "technology that would make the program better for me. I created this "
                                          "project because I started tracking my net worth when I graduated, "
                                          "and as I was getting more financial accounts just as a 401k or brokerage "
                                          "account, I saw myself having to log in to every site at the end of every "
                                          "week. This got very repetitive and wasted a lot of my time so I started "
                                          "tracking my portfolio using this program. It started off as a basic "
                                          "portfolio track, but as I've learned more about programming I added many "
                                          "features using various financial institute APIs, machine learning to "
                                          "estimate my future net worth and cloud hosting so that I can update my "
                                          "data via a mobile phone.",

    f"how do you value diversity as part of the team?": "I value diversity as part of the team because being able to "
                                                        "hear an opinion from different kinds of people that have "
                                                        "live different experiences is what makes a project "
                                                        "interesting. I want a team to have a variety of people so "
                                                        "that everyone's voice is heard, and every type of person can "
                                                        "have their input in how a project is implemented.",

    f"name a time when you were given a tight deadline "
    f"with little information and had to choose between "
    f"a few options and how did that turn out": "One time when I was given a tight deadline with little information "
                                                "and had to choose between a few options was back when I started the "
                                                "Veris V3 project. I had to start it from a blank slate and did not "
                                                "know how to approach the project. I spent the first few days just "
                                                "staring at my screen doing other tasks since I was so intimidated "
                                                "from this project. I was given this project and had to decide every "
                                                "detail for it. My manager wanted to transition to using Scala since "
                                                "other teams were using it and we had started learning it, "
                                                "but I knew it would take a while for us to fully grasp Scala, "
                                                "so I decided on using Python. I was much more familiar with Python "
                                                "and was able to finally get some progress done on the project that "
                                                "started from an empty file. Clients wanted to see a demo of the "
                                                "project so I worked long hours trying to put together something "
                                                "presentable and when it was time to present it, the clients enjoyed "
                                                "what they saw and appreciated the effort. It was a great feeling and "
                                                "looking back I learned that when you have a tight deadline, "
                                                "try not to take risks and just go with what works. ",

    f"what is something you do better than your peers?": "something I do better than my peers would have to be "
                                                         "maintaining my positive attitude. I have been through "
                                                         "enough difficult situations that my problem-solving skills "
                                                         "stand out among my peers. I consistently tackle challenges "
                                                         "with a positive attitude, which helps me stay resilient and "
                                                         "motivated. This optimism allows me to maintain a positive "
                                                         "work environment which also positively effect my teammates "
                                                         "to make the workplace an enjoyable environment.",

    f"what is something your peers do better than you?": "something my peers do better than myself would be asking "
                                                         "questions. When I was assigned the Veris V3 project I was "
                                                         "lost on how to approach it, and was blankly staring at my "
                                                         "screen for a few days trying to do other tasks. Once that "
                                                         "fear went away I started asking more senior engineers for "
                                                         "advice on how to approach the project, from that I was able "
                                                         "to start it. I was able to quickly expand my ideas and put "
                                                         "them to code for the project. The following week the "
                                                         "project had a lot of progress done and the project managers "
                                                         "liked what they saw during my demo. Since then I have been "
                                                         "improving my habit of asking good questions. I try to work "
                                                         "on something for 30 minutes and if I am still unsure after "
                                                         "trying hard for those 30 minutes, then I start asking "
                                                         "people who might know the answer some questions.",

    f"what do you look for when reviewing a coworkers merge request?": "what I look for when reviewing a coworker's "
                                                                       "merge request would be to see how easy it is "
                                                                       "to follow without asking questions. I check "
                                                                       "to make sure that it's easily readable, "
                                                                       "so that if a new employee gets assigned to "
                                                                       "this project, they can understand what is "
                                                                       "going on from day 1. This has proven to also "
                                                                       "help my merge requests as well, because now I "
                                                                       "try to make my merge requests as easy to "
                                                                       "follow to ensure everyone is on the same page.",

    f"how do you explain the short stints at each company you've worked at?": "I wanted to get exposure to a lot of "
                                                                              "different industries and technologies "
                                                                              "in a short amount of time, when I felt "
                                                                              "like my personal growth was plateauing "
                                                                              "I would look for a new challenge. This "
                                                                              "is what led me to apply to such a "
                                                                              "large company, because I want to "
                                                                              "settle down now.",

    f"why are you currently not working at Axoni?": "Due to the market conditions, the project I was working on got "
                                                    "canceled and my team was laid off. "
}

# questions that I should ask
my_questions = {
    f"what is typically expected of someone in this role after completing their first 90 days at {company_name}?",

    f"since many of the roles at {company_name} are remote, how does {company_name} help remote workers lift their "
    f"spirit up in a job that might not have a lot of human interaction during the typical day? ",

    f"how did {company_name} help the mental health of employees during COVID?",

    f"what are some short term and long term goals the company expects for someone in this role to accomplish?"
}

# unique for every company
unique_questions = {


}

interviewer1 = f"Why do you want to work at {company_name}?"
# I want to work in a fresh environment because I can use my experience to learn new technologies and further
# learn how to adapt to new challenges while having more growth opportunities
interviewer2 = f"What made you want to apply at {company_name}?"
# What made me apply was when I was searching for fintech companies, and just looking at all the options that were
# available. I was drawn to {company_name} because of the job description mentioning the tech that is typically used
# for this role. I am familiar with some tech such as Python, but not so familiar with others, but I hope to continue
# learning so that I am familiar with any necessary tech in the future
interviewer3 = f"Why are you looking for a new role?"
# I am looking for a new role because I've done great things in my current role, but I want to broaden my knowledge
# and continue to learn good software engineering practices, along with getting the change to work on different
# projects and learn in a fresh environment
interviewer4 = f"What got you interested in software engineering?"
# I studied mechanical engineering, and ended up doing the engineering portions of project management roles.
# It was interesting at first, but over time it was essentially the same day over and over again. I would go
# to a site, look at the mechanical systems and then write about them. If you've ever been inside the basement
# of a few buildings in NYC you'll see that they typically use the same systems. This got very boring to me over
# time. Then my friend convinced me that I should try software engineering because I can start from a blank slate,
# and build whatever I want. I started writing basic scripts to automate daily tasks such as writing reports in my
# mechanical engineering roles, and eventually I started working for a software engineering startup with my friend.
interviewer5 = f"What are you looking for in your next role?"
# mention it directly being the role you are applying for
# I'm looking to continue working in fintech, in a fast moving environment where coding is the main work task
# typically done throughout the day
# I'm really passionate about being fully invested in the work I do. When it comes to projects, I always strive
# to take ownership and drive them towards success. This is why I want to join a new project and take ownership
interviewer6 = f"What do you typically do during the day at your current role?"
# At Axoni what I am working now is called the Veris project, this project is a platform where clients
# such as big banks can perform equity swaps, which is a type of trade. My current role for this project is to
# primarily work on the backend by developing APIs for the transactions, optimizing database queries for the
# different types of trades, and make sure that all functions of an equity swap work as expected. I also help out
# with the frontend by working with the design team to develop user-friendly interfaces with easy to find functions
interviewer7 = f"Why are you looking for a fintech role?"
# I'm looking for a fintech role because I want to mix my love for coding and interest in financial services such as
# trades and looking at equities. I am drawn to the fast-paced nature of fintech, and I want to continue my career
# working in this industry.
interviewer8 = f"In a few sentences, describe why you think you would be a good fit at {company_name} or " \
               f"why you are interested in {company_name}."
# I think I would be a good fit at ___ because I want to continue to learn at a fintech company. I enjoy my
# current role, but I want to work somewhere with new projects, and new technology to learn about.
interviewer9 = f"tell me about a time you faced a technical challenge and what decisions you made."
# a time when I faced a technical challenge would be when I was starting the Veris V3 project and unsure of what
# programming language to start the repo with. I was deciding between Scala since that's what other projects where
# mainly written in, and Python because it was the language I was most familiar with. I spent a few days trying to
# quickly learn Scala to try and piece the start of the project together, but then I had a talk with the team where
# we discussed being able to meet deadlines while having to learn a programming language along with other functions
# of the job, and that's when we decided that it would be best if the project was done in Python. I ended up
# progressing very quickly on the project and was able to meet the first deadline for us to demo the project for
# clients. I leaned that sticking to what you know could prove to be better for a project than trying to fit in
# with everyone else.
interviewer10 = f"what is your role for the current project you’re working on?"
# In my current capacity, I hold the position of project lead for the Veris project. As a full-stack engineer,
# my responsibilities span across both the backend and frontend aspects of the project. On the backend, my primary
# focus is to meticulously orchestrate the trading processes, ensuring not only their seamless functionality but
# also their utmost efficiency. I take pride in crafting the digital machinery behind the scenes, making certain
# that each trade unfolds flawlessly. For the frontend, I take on a more user-centric role. It's my duty to empower
# our clients with a comprehensive understanding of the available trading options. I strive to create an intuitive
# interface that guides them through the entire trading journey, from pre-transaction insights to post-transaction
# clarity. It's about making complex financial processes transparent and accessible to our valued customers. This
# dual-role as a technical orchestrator and a user experience advocate allows me to contribute holistically to the
# Veris project, ensuring that it thrives both behind the scenes and in the hands of our clients.




# questions to ask interviewers


question1 = f"what is typically expected of someone in this role after completing" \
            f"their first 90 days at {company_name}?"
question2 = f"since many of the roles at {company_name} are remote, how does {company_name} help remote workers" \
            f"lift their spirit up in a job that might not have a lot of human interaction during the typical day?"
question3 = f"What are some short-term and long-term goals for someone in this role?"
# UNIQUE
question4 = f"I read the Forbes article on how Ramp built an $8 billion company in only a few years. With this " \
            f"rapid growth, would a backend engineer like the one in this role occasionally have to help with the " \
            f"frontend if the time comes up, or would an engineer stick to their role even when times are busy?"
