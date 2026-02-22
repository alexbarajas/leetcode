NAME = "Alex Barajas"

addressee = input("Who is this addressed to (first name)? ")
company = input("What is the name of the company? ")

firstRecruiter = "Thank you for your time during the interview earlier. "
firstInterviewer = "Thank you for the interview earlier, "
first = firstRecruiter if input("is this for a recruiter (True) or interviewer? (False) ").capitalize() else firstInterviewer

secondLearned = input("What did you enjoy learning about? i.e. \"I enjoyed learning about how the culture is at ..., "
                      "and how people are so supportive of each other\" ")
# second = f"Thanks to the interviews I'm even more excited about possibly working at {company.capitalize()}."
second = f"Thank you once again for spending some time discussing the role with me earlier. I'm looking forward to " \
         f"hearing back from you, and I hope you have a great rest of your day!"

day = "weekend" if input("is it Friday? Y/N ").lower() == "y" else "day"
thirdFeedback = f"Have a great {day}, and hope to receive feedback soon!"

ThankYouLetter = f"Hello {addressee}," \
                 f"\n\n{first}{secondLearned} {second}" \
                 f"\n\n{thirdFeedback}" \
                 f"\n\nBest regards," \
                 f"\n{NAME}"

print("\n\n" + ThankYouLetter)

