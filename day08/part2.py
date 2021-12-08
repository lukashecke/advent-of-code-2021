with open('input.txt') as file:
    segments_per_line = [line.strip().split(' ') for line in file]

output_sum = 0


def number_from_segments(segment, null_segments, one_segments, two_segments, three_segments, four_segments, five_segments, six_segments, seven_segments, eight_segments, nine_segments):
    segment = ''.join(sorted(segment))
    if segment == ''.join(sorted(null_segments)):
        return 0
    elif segment == ''.join(sorted(one_segments)):
        return 1
    elif segment == ''.join(sorted(two_segments)):
        return 2
    elif segment == ''.join(sorted(three_segments)):
        return 3
    elif segment == ''.join(sorted(four_segments)):
        return 4
    elif segment == ''.join(sorted(five_segments)):
        return 5
    elif segment == ''.join(sorted(six_segments)):
        return 6
    elif segment == ''.join(sorted(seven_segments)):
        return 7
    elif segment == ''.join(sorted(eight_segments)):
        return 8
    elif segment == ''.join(sorted(nine_segments)):
        return 9


for line_values in segments_per_line:
    null_segments = ''
    one_segments = ''
    two_segments = ''
    three_segments = ''
    four_segments = ''
    five_segments = ''
    six_segments = ''
    seven_segments = ''
    eight_segments = ''
    nine_segments = ''

    bottom_left_segment = ''
    for i in range(5):
        if i == 0:  # find 1, 4, 7, 8
            for segment in line_values:
                if len(segment) == 2:
                    one_segments = segment
                if len(segment) == 4:
                    four_segments = segment
                if len(segment) == 3:
                    seven_segments = segment
                if len(segment) == 7:
                    eight_segments = segment
        if i == 1:  # find 3
            for segment in line_values:
                if len(segment) == 5:
                    if set(list(one_segments)).issubset(set(list(segment))):
                        three_segments = segment
                        break
        if i == 2:  # find 9
            for segment in line_values:
                if len(segment) == 6:
                    if set(list(three_segments)).issubset(set(list(segment))):
                        nine_segments = segment
                        bottom_left_segment = [s for s in list(eight_segments) if s not in list(nine_segments)][0]
                        break
        if i == 3:  # find 5 & 2
            for segment in line_values:
                if len(segment) == 5:
                    if not set(list(one_segments)).issubset(set(list(segment))):  # filter 3
                        if set(list(segment)).issubset(set(list(nine_segments))):
                            five_segments = segment
                        else:
                            two_segments = segment
        if i == 4:  # find 6 & 0
            for segment in line_values:
                if len(segment) == 6:
                    if not set(list(one_segments)).issubset(set(list(segment))):
                        six_segments = segment
                    elif segment.__contains__(bottom_left_segment):
                        null_segments = segment
    output_sum += number_from_segments(line_values[11], null_segments, one_segments, two_segments, three_segments, four_segments, five_segments, six_segments, seven_segments, eight_segments, nine_segments) * 1000
    output_sum += number_from_segments(line_values[12], null_segments, one_segments, two_segments, three_segments, four_segments, five_segments, six_segments, seven_segments, eight_segments, nine_segments) * 100
    output_sum += number_from_segments(line_values[13], null_segments, one_segments, two_segments, three_segments, four_segments, five_segments, six_segments, seven_segments, eight_segments, nine_segments) * 10
    output_sum += number_from_segments(line_values[14], null_segments, one_segments, two_segments, three_segments, four_segments, five_segments, six_segments, seven_segments, eight_segments, nine_segments)

print(output_sum)
