# Solution for the problem "ACM ICPC Team"
# https://www.hackerrank.com/challenges/acm-icpc-team/problem

# Count of the number of people and topics
peopleCount, topicCount = map(int, input().strip().split(' '))

# Knowledge of person in topic
personKnowledge = []

for peopleIndex in range(0, peopleCount):
    # We need to convert to binary for bitwise operations
    currentPersonKnowledge = int(input().strip(), 2)

    # Add to knowledge list
    personKnowledge.append(currentPersonKnowledge)

# Initializing maximum combined knowledge
maxKnowledge = 0

# Number of teams with maximum knowledge
maxKnowledgeCount = 0

# We need to do bitwise or on every combination to get the topic each two person team can know
for personIndex1 in range(0, peopleCount - 1):
    for personIndex2 in range(personIndex1 + 1, peopleCount):
        unionKnowledge = personKnowledge[personIndex1] | personKnowledge[personIndex2]

        # Counting number of ones to get current team's knowledge
        currentTeamKnowledge = str(bin(unionKnowledge)).count('1')

        # If the combined knowledge is same as max knowledge, increment max knowledge count
        # If combined knowledge is greater, update max knowledge with current max knowledge
        # And reset max knowledge count to 1
        if currentTeamKnowledge > maxKnowledge:
            maxKnowledge = currentTeamKnowledge
            maxKnowledgeCount = 1
        elif currentTeamKnowledge == maxKnowledge:
            maxKnowledgeCount = maxKnowledgeCount + 1

# Print maximum combined knowledge and count of teams having maximum knowledge
print(maxKnowledge)
print(maxKnowledgeCount)