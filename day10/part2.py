with open('input.txt') as file:
    code = [line.strip() for line in file]

open_tags = ['(', '[', '{', '<']
close_tags = [')', ']', '}', '>']

incomplete_lines = []


def find_incomplete_lines():
    for line in code:
        modified_line = line
        finished = False
        while not finished:
            end_or_modified = False
            for i in range(len(modified_line)):
                if i == len(modified_line) - 1:  # missing character(s)
                    incomplete_lines.append(line)
                    end_or_modified = True
                    finished = True
                    break
                if modified_line[i] in open_tags and modified_line[i + 1] in close_tags:
                    for t in range(4):
                        if modified_line[i] == open_tags[t] and modified_line[i + 1] == close_tags[t]:
                            modified_line = modified_line[:i] + modified_line[i + 2:]
                            end_or_modified = True
                            break
                        if t == 3:  # illegal character
                            end_or_modified = True
                            finished = True
                            break
                if end_or_modified:
                    break


find_incomplete_lines()
unclosed_line_tags = []


def remove_legal_pairs():
    for line in incomplete_lines:
        finished = False
        while not finished:
            for i in range(len(line)):
                end_or_modified = False
                if i != len(line) - 1:
                    if line[i] in open_tags and line[i + 1] in close_tags:
                        for t in range(4):
                            if line[i] == open_tags[t] and line[i + 1] == close_tags[t]:
                                line = line[:i] + line[i + 2:]
                                end_or_modified = True
                                break
                else:  # end of line
                    unclosed_line_tags.append(line)
                    finished = True
                    end_or_modified = True
                if end_or_modified:
                    break


remove_legal_pairs()
scores = []


def calc_scores():
    for line in unclosed_line_tags:
        score = 0
        for opening_tag in reversed(list(line)):
            for t in range(4):
                if open_tags[t] == opening_tag:
                    score *= 5
                    score += (t + 1)
                    break
        scores.append(score)


calc_scores()
scores.sort()

print(scores[int((len(scores)/2))])
