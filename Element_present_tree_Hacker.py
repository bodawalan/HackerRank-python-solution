class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node


"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""


def isPresent(root, val):

# write your code here
# return 1 or 0 depending on whether the element is present in the tree or not
    curr_node = root
    while curr_node:
        if curr_node.value == val:
            return 1
        elif curr_node.value < val and curr_node.right:  # move right
            curr_node = curr_node.right
        elif curr_node.value > val and curr_node.left:  # move left
            curr_node = curr_node.left
        else:
            return 0
    return 0


_a = None
_a_size = input()
_a_i=0

while _a_i < _a_size:
    _a_item = input()
    _a = _insert_node_into_binarysearchtree(_a, _a_item)
    _a_i += 1

_b = input()

_result = isPresent (_a , _b );
print _result


"""good git
https://github.com/pdecks
https://github.com/pdecks/airbnb-warmup/blob/master/warmup2.py"""