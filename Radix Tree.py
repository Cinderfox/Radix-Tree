class Node: # initialise a node of Trie
    def __init__(self):
        self.value = None       #value corresponds to letter
        self.leef = False       #leef signifies the letter is the end of word
        self.children = {}      #children contains all children of Node
        
class Trie:
    def __init__(self):
        self.root = Node()      #initialise Trie with Root as Null

    ''' insert function 
    inserts word into Trie if it doesn't already exist
    gives leef node attribute to last character if word
    already exists in Trie '''

    def insert(self, word):
        curWord = word
        curNode = self.root
        while len(curWord) > 0:
            if curWord[0] in curNode.children:
                curNode = curNode.children[curWord[0]]
                if len(curWord) == 1:
                    curNode.leef = True
                curWord = curWord[1:]
            else:               
                newNode = Node()
                newNode.value = curWord[0]
                if len(curWord) == 1:
                    newNode.leef = True
                curNode.children[curWord[0]] = newNode                
                curNode = newNode
                curWord = curWord[1:]
            
    ''' searching function
    searches for word taken from user and traverses Trie
    returns confirmation if word is found
    returns Not found if word is not present in Trie  '''

    def search(self, word):
        curWord = word
        curNode = self.root
        while len(curWord) > 0:
            if curWord[0] in curNode.children:
                curNode = curNode.children[curWord[0]]
                if len(curWord) == 1:
                    if curNode.leef == True:
                        return 'Word \'' + word + '\' has been found in trie'
                    else:
                        return 'Not Found'
                curWord = curWord[1:]
            else:
                return "Not in trie"
    
    ''' deletion function  
    traverses to find user inputted word in Trie
    if word doesn't exist returns not found in Trie
    if found and last letter has no children deletes till
    there are children
    if found and last letter has children, then removes leef
    node attribute from the letter and returns deletion confirmation '''

    def delete(self, node, word, idx=0):
        if len(word) == idx:
            node.leef = False
            print('\''+ word + '\'' + ' has been deleted from Trie')
            if node.children is False:
                return False
            else:
                return True
        char = word[idx]
        if char not in node.children:
            print('\''+ word + '\'' + ' not found in Trie')
            return True
        if self.delete(node.children[char], word, idx+1) is True:
            return True
        node.children.pop(char)
        if node.children is False or node.leef is False:
            return False
        else:
            return True
            
    ''' autocompletion function 
    searches for the inputted prefix in the Trie
    returns list of words starting with prefix '''

    def autocomplete(self, word):
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                return "No Auto-complete for given input!"
            curNode = curNode.children[char]
        return self.autoSearch(curNode, '', word, [])

    def autoSearch(self, curNode, out_word, word, ac_list):
        for child in curNode.children.values():
            x = out_word + child.value
            if child.leef:
                ac_list.append(x)
            self.autoSearch(child, x, word, ac_list)
        output_list = []
        for i in ac_list:
            i = word + i
            output_list.append(i)
        return output_list
    
    ''' print all nodes function starting from root node 
    which is null '''

    def printer(self):
        print('Printing all nodes...')
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            print(nodes.pop(0).value, end = ', ')
        
''' initialise a Trie with words '''

def makeTrie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

''' menu function to make menu driven programme '''
def menu():

    trie = makeTrie(['bat', 'batter', 'cattle', 'capitulate', 'canopy','cat', 'calligraphy', 'a','b'])
    
    print('''\nEnter your choice below:
    1. Insert into Trie
    2. Search in Trie
    3. Delete from Trie
    4. Print all Nodes of Trie
    5. Autocomplete words present in Trie
    6. Print all words present in Trie
    7. Exit''')

    choice = int(input("Input: "))
    
    if choice == 1:
        word = input("Enter the word to insert into Trie: ")
        trie.insert(word)
        print(trie.autocomplete(''))
        menu()
    elif choice == 2:
        word = input("Enter the word to search in Trie: ")
        print(trie.search(word))
        print(trie.autocomplete(''))
        menu()
    elif choice == 3:
        word = input("Enter the word to delete from Trie: ")
        trie.delete(trie.root, word)
        print(trie.autocomplete(''))
        menu()
    elif choice == 4:
        trie.printer()
        menu()
    elif choice == 5:
        word = input("Enter characters to auto-complete: ")
        print(trie.autocomplete(word))
        menu()
    elif choice == 6:
        print(trie.autocomplete(''))
        menu()
    elif choice == 7:
        return print(" bye :) ")
menu()