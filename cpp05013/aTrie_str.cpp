// Trie but elements can be any string
struct Node{
    bool end = false, root;
    map<string, Node*> nxt; 
    Node(bool root = false): root{root} {}
};

struct Trie{
    Node *root = new Node(true);
    void add(vector<string>& sv){
        Node *n = root;
        for(string& x: sv){
            if(n->nxt.find(x) == n->nxt.end()) n->nxt[x] = new Node();
            n = n->nxt[x];
        }
        n->end = true;
    }
};