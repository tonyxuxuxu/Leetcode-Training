"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def bfs(front_level, end_level, is_forward, word_set, path_dic):
            if len(front_level) == 0:
                return False
            if len(front_level) > len(end_level):
                return bfs(end_level, front_level, not is_forward, word_set, path_dic)
            for word in (front_level | end_level):
                word_set.discard(word)
            next_level = set()
            done = False
            while front_level:
                word = front_level.pop()
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in end_level:
                            done = True
                            add_path(word, new_word, is_forward, path_dic)
                        else:
                            if new_word in word_set:
                                next_level.add(new_word)
                                add_path(word, new_word, is_forward, path_dic)
            return done or bfs(next_level, end_level, is_forward, word_set, path_dic)

        def add_path(word, new_word, is_forward, path_dic):
            if is_forward:
                path_dic[word] = path_dic.get(word, []) + [new_word]
            else:
                path_dic[new_word] = path_dic.get(new_word, []) + [word]

        def construct_path(word, end_word, path_dic, path, paths):
            if word == end_word:
                paths.append(path)
                return
            if word in path_dic:
                for item in path_dic[word]:
                    construct_path(item, end_word, path_dic, path + [item], paths)

        front_level, end_level = {beginWord}, {endWord}
        path_dic = {}
        bfs(front_level, end_level, True, wordList, path_dic)
        path, paths = [beginWord], []
        construct_path(beginWord, endWord, path_dic, path, paths)
        return paths