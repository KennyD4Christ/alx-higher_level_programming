#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        return 0, None


# Example usage
if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
