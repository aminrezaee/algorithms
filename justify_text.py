class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        results = []
        current_length = 0
        chosen_words = []
        for word in words:
            word_length = len(word)
            needs_space = False
            can_add_next_word = (current_length + word_length + 1) <= maxWidth
            if (len(chosen_words) > 0) and (can_add_next_word or (len(chosen_words) == 1)): # dont add space at first of line
                chosen_words.append("") # add space between each two word
                needs_space = True
            current_length += int(needs_space)
            if can_add_next_word:
                chosen_words.append(word)  # add word
                current_length += word_length
            else:
                line = self.fill_spaces(chosen_words , maxWidth)
                results.append(line)
                chosen_words = [word]
                current_length = word_length
        if len(chosen_words) > 0:
            if len(chosen_words) == 1:
                chosen_words.append("")
            line = self.fill_spaces(chosen_words , maxWidth)
            results.append(line)
        return results
                
    def fill_spaces(self, chosen_words:list[str] , maxWidth):
        needed_spaces = maxWidth - sum([len(word) for word in chosen_words])
        places = [i for i in range(len(chosen_words)) if len(chosen_words[i]) == 0]
        remaining_spaces = needed_spaces % len(places)
        required_spaces = [needed_spaces/len(places) for i in range(len(places))]
        for i in range(len(places)):
            if i < remaining_spaces:
                required_spaces[i] += 1
            else:
                break
        
        for required_space_index , index in enumerate(places):
            chosen_words[index] = " " * int(required_spaces[required_space_index])
            
        return "".join(chosen_words)
    
    
    def insert_spaces_in_place(self , text:str , space_index:int , space_per_place:int):
        return text

if __name__== "__main__":
    solution = Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."] , 16))