from cola import Queue
class BinaryTree:
    
    class __Node:
        def __init__(self, key, pokemon):
            self.key = key
            self.pokemon = pokemon
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key, pokemon):
        def __insert(root, key, pokemon):
            if root is None:
                return BinaryTree.__Node(key, pokemon)
            elif key < root.key:
                root.left = __insert(root.left, key, pokemon)
            else:
                root.right = __insert(root.right, key, pokemon)
            return root

        self.root = __insert(self.root, key, pokemon)

    def search(self, key):
        def __search(root, key):
            if root is None:
                return None
            elif root.key == key:
                return root.pokemon
            elif key < root.key:
                return __search(root.left, key)
            else:
                return __search(root.right, key)

        return __search(self.root, key)

    def search_by_prefix(self, prefix):
        result = []
        def __search_by_prefix(root, prefix):
            if root is not None:
                if prefix in root.key:
                    result.append(root.pokemon)
                __search_by_prefix(root.left, prefix)
                __search_by_prefix(root.right, prefix)
        __search_by_prefix(self.root, prefix)
        return result

    def in_order(self):
        result = []
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                result.append(root.pokemon)
                __in_order(root.right)
        __in_order(self.root)
        return result

    def by_level(self):
        result = []
        queue = Queue()
        if self.root is not None:
            queue.arrive(self.root)
        
        while queue.size() > 0:
            node = queue.attention()
            result.append(node.pokemon)
            if node.left is not None:
                queue.arrive(node.left)
            if node.right is not None:
                queue.arrive(node.right)
        
        return result
