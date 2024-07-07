## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Split the path and recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        parts = self.split_path(path)
        
        for part in parts:
            current_node.insert(part)
            current_node = current_node.children[part]
        
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        parts = self.split_path(path)
        
        for part in parts:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        
        return current_node.handler

    def split_path(self, path):
        # Split the path by '/' and filter out empty strings
        return [part for part in path.split('/') if part]


## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, part):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode()

## The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the parts as a list to the RouteTrie
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # Lookup path (by parts) and return the associated handler
        # If there is no path return the "not found" handler
        handler = self.route_trie.find(path)
        if handler:
            return handler
        else:
            return self.not_found_handler

    def split_path(self, path):
        # Split the path by '/' and filter out empty strings
        return self.route_trie.split_path(path)


def test():
    # Example usage
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler'
    print(router.lookup("/home/about/me")) # should print 'not found handler'

if __name__ == "__main__":
    test()
