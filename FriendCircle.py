import os.path
import sys
from collections import defaultdict

# FriendCircle is  implementation of graph data structure. This implementation maintains uses dictionary to maintain
# vertex i.e. friends and list to maintain direct friends.
class FriendCircle:
    graph_dict = defaultdict(list)
    DEFAULT_START_FRIEND=0


    def makeFriend(self, node, neighbour):
        friendSize=len(self.graph_dict)
        """
            Initialize the friend node in dictionary and keep the starting friend.
        """
        if friendSize==0 and node is not None:
            self.DEFAULT_START_FRIEND=node
        """
            Add friend node to dictionary and keep its direct friends in list.
        """
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
            if neighbour not in self.graph_dict:
                self.graph_dict[neighbour]=[node]
        else:
            self.graph_dict[node].append(neighbour)
            if neighbour not in self.graph_dict:
                self.graph_dict[neighbour]=[node]


    def breakFromFriend(self, node, neighbour):
        """
            Go to the friend from in dictionary and remove its direct.
        """
        if node not in self.graph_dict: return
        else:
            self.graph_dict[node].remove(neighbour)

    def findAllFriends(self,node):

        """
          Goes to the start of node when total has to be found.Check its lists and its direct friendly nodes.
          It gives direct friends of node and indirect friends of node by traversing through list.
        """
        if node not in self.graph_dict: return
        path = []
        stack = [node]
        while (len(stack) != 0):
            s=stack.pop()
            if s not in path:
                path.append(s)
            if s not in self.graph_dict:
                continue
            for friends in self.graph_dict[s]:
                if friends not in path:
                    stack.append(friends)
        return len(path)-1



g = FriendCircle()
scriptdir = os.path.dirname(os.path.abspath(__file__))

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
"""
    Read file input which splits enter or return.
"""
try:
    filename = dname + sys.argv[1]
    arr = open(filename).read().split("\n")
except:
    print("Input file not found")
    exit()
output=[]

"""
    Read all the lines.
"""
for line in arr:
    if (len(line.split())==3):
        functionInput,source,target=line.split()
        if (functionInput=='friends'):
            g.makeFriend(source,target)
            g.findAllFriends(g.DEFAULT_START_FRIEND)
        if (functionInput=='breakUp'):
            g.breakFromFriend(source,target)
    elif (len(line.split())==1):
        functionInput=line.split()
        if (line=='total'):
            output.append(g.findAllFriends(g.DEFAULT_START_FRIEND))
fileNameOut = os.path.join(dname, "outputPS17.txt")
file1 = open(fileNameOut, "w")
for outresult in output:
    file1.write("%s\n" %outresult)