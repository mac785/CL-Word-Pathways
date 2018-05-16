from tkinter import filedialog
import random


class wordPathKeeper:

    def load_words(self):
        self.vertices = []
        print ("Showing file dialog. Make sure it isn't hiding!")
        word_filename = filedialog.askopenfilename(title="Find the list of words.")
        if word_filename == "":
            raise IOError("No file found...")

        count = 0
        with open(word_filename, 'r') as ins:
            for line in ins:
                items = line.split("\t")
                if count % 100 == 0:
                    print(count)
                count += 1
                self.vertices.append(items[1].split("\n")[0])

    def num_mismatched(self, word1, word2):
        """
        looks at the two words, character by character and returns the number of
        characters that don't match.
        :param word1: a string
        :param word2: another string, of the same length as word1
        :return: the number of characters that don't match. Two identical strings
        would return 0; "pack" and "pick" would return 1; "mate" and "meta" would return 2.
        """
        count = 0
        # -----------------------------------------
        placeCounter = 0
        for i in word1:
            if i != word2[placeCounter]:
                count += 1
            placeCounter += 1
        # -----------------------------------------
        return count

    def build_edges(self):
        """
        loops through the list of words in self.vertices. Compares each word to the
        other words on the list. If they differ by exactly one letter, then records
        the words to the self.edges data structure.

        Self.edges should be an array of arrays - each subarray might take the form
        of a pair of indices (e.g., [8252, 8253]) or a pair of strings (e.g.,
        ["zooks", "zooms"]).

        You may also desire to make these unidirectional or
        bidirectional (undirected) edges - for example the connection might be saved
        as [8252, 8253], which would imply a connection in both directions or as
        [8252, 8253] AND [8253, 8252], which would represent two connections from the
        first value to the second. (Obviously, you could use strings, too.)
        The difference is that the former method requires searching the first value
        of the array when looking for a match as well as the second value, but it takes
        half the memory as the latter method.

        Of the four options (id# vs. string) x (unidirectional vs. bidirectional),
        none is "right" or "wrong" here. You can choose the version you wish. Just
        be consistent with the rest of your program.
        :return: None
        """

        self.edges = []
        # -----------------------------------------
        for i in range(0,len(self.vertices)):
            for j in range(i,len(self.vertices)):
                if(self.num_mismatched(self.vertices[i],self.vertices[j]) == 1):
                    self.edges.append([self.vertices[i],self.vertices[j]])
        # -----------------------------------------

        print (self.edges[1])

    def get_neighbors(self, node):
        """
        returns a list of nodes that are directly connected to the node.
        (Nodes can be either strings or id numbers - programmer's choice.)
        If there are no neighbors, return an empty array.
        :param node:
        :return: an array of nodes
        """
        neighbors = []
        # -----------------------------------------
        # TODO: You should write this method!
        for i in self.edges:
            if i[0] == node:
                neighbors.append(i[1])
            elif i[1] == node:
                neighbors.append(i[0])
        # -----------------------------------------
        return neighbors

    def find_path(self, word1, word2):
        """
        Uses Breadth-First-Search to find a path of words from word1 to word2,
        where each word in the path varies from the previous word by exactly
        one letter. For instance, if word1 is "bike" and word2 is "mods", we might
        get a path = ["bike", "bite", "mite", "mote", "mode", "mods"] (Note: I did
        this manually, so the computer might come up with something else.)

        If no path exists from word1 to word2, return None.
        :param word1:
        :param word2:
        :return: an array of strings, or None.
        """
        path = []
        # -----------------------------------------
        # TODO: you should write this
        frontier = []
        visited = []
        done = False
        path.append(word1)
        frontier.append([word1, path])
        while(not done and len(frontier) != 0):
            current = frontier.pop()
            path = current[1]
            neighbors = self.get_neighbors(current[0])
            for i in neighbors:
                if (i not in visited):
                    path.append(i)
                    if i == word2:
                        done = True
                        break
                    else:
                        frontier.append([i,path])
                    visited.append(i)
        # -----------------------------------------
        if done:
            return path
        else:
            print ("No path connecting the two.")

wpk = wordPathKeeper() # calls constructor
wpk.load_words()
wpk.build_edges()
# Alternately, use this method once to build the edges and save them to a file.
# I'll let you research saving files, yourself.... It's fairly similar to opening a file.
# Then load the file in the future. wpk.load_edges()

num_letters = len(wpk.vertices[0])

while True:
    print("Enter the first {0}-letter word: ".format(num_letters))
    word1 = input()
    print("Enter the second {0}-letter word: ".format(num_letters))
    word2 = input()
    if len(word1) != num_letters:
        print("{0} has the wrong number of letters.".format(word1))
        continue
    if len(word2) != num_letters:
        print("{0} has the wrong number of letters.".format(word2))
        continue

    path = wpk.find_path(word1, word2)
    if path is None:
        print ("No path found.")
    else:
        print ("Path has {0} steps:".format(len(path)-1))
        for word in path:
            print (word)


