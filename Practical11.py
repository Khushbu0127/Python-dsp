class FileNode:
    def __init__(self, name, is_folder=False):
        self.name = name
        self.is_folder = is_folder
        self.left = None # first child / file inside folder
        self.right = None # next file in same folder

    def add_child(self, child):
        if self.left is None:
            self.left = child
        else:
            temp = self.left
            while temp.right:
                temp = temp.right
            temp.right = child

root = FileNode("C:", True)
docs = FileNode("Documents", True)
pics = FileNode("photo.jpg", False)
root.add_child(docs)
docs.add_child(pics)

def display(node, level=0):
    if node:
        print(" "*level + ("[Folder] " if node.is_folder else "[File] ") + node.name)
        if node.left: display(node.left, level+1)
        if node.right: display(node.right, level)

display(root)
