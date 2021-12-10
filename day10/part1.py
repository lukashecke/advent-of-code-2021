with open('input.txt') as file:
    code = [line.strip() for line in file]

open_tags = ['(', '[', '{', '<']
close_tags = [')', ']', '}', '>']

score = 0

for line in code:
    finished = False
    while not finished:
        end_or_modified = False
        for i in range(len(line)):
            if i == len(line) - 1:  # missing character(s)
                end_or_modified = True
                finished = True
                break
            if line[i] in open_tags and line[i + 1] in close_tags:
                for t in range(4):
                    if line[i] == open_tags[t] and line[i + 1] == close_tags[t]:
                        line = line[:i] + line[i + 2:]
                        end_or_modified = True
                        break
                    if t == 3:  # illegal character
                        for t2 in range(4):
                            if line[i] == open_tags[t2]:
                                found = line[i + 1]
                                if found == ')':
                                    score += 3
                                if found == ']':
                                    score += 57
                                if found == '}':
                                    score += 1197
                                if found == '>':
                                    score += 25137
                                end_or_modified = True
                                finished = True
                                break
            if end_or_modified:
                break

print(score)
