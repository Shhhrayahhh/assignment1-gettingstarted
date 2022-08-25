### getting started assignment

def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mtls"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "No"
    elif question5 == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question6 == "What is the SHA1 hashing value to the following message: 'NYU Computer Networking' - Use SHA1 hash generator and use the answer in your code":
        answer = "8496abe9fceb5aa927e28bfbd9a2347d1290ef9b"
    elif question7 == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Yes"
    elif question8 == "What layer of the OSI model does the protocol DHCP belong to? - The answer should be an integer number":
        answer = int(2)
    elif question9 == "What layer of the OSI model does the protocol TCP belong to? - The answer should be an integer number":
        answer = int(4)
    else:
        answer = ""
    return (answer)

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

# Questions:
# "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
# "Are encoding and encryption the same? - Yes/No":
# "Is it possible to decrypt a message without a key? - Yes/No":
# "Is it possible to decode a message without a key? - Yes/No":
# "Is a hashed message supposed to be un-hashed? - Yes/No":
# "What is the SHA1 hashing value to the following message: 'NYU Computer Networking' - Use SHA1 hash generator and use the answer in your code":
# "Is MD5 a secured hashing algorithm? - Yes/No":
# "What layer of the OSI model does the protocol DHCP belong to? - The answer should be an integer number":
# "What layer of the OSI model does the protocol TCP belong to? - The answer should be an integer number":
