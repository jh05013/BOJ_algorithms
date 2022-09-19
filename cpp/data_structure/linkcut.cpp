template <typename Node>
struct LinkCut{
	int n;
	vector<Node*> nodes;

	LinkCut(vector<typename Node::scont_t> conts): n(sz(conts)){
		for(int i=0; i<n; i++){
			nodes.push_back(new Node(conts[i]));
			nodes[i]->no = i;
		}
	}
	Node *new_node(typename Node::scont_t c){
		nodes.push_back(new Node(c));
		nodes.back()->no = n++;
		return nodes.back();
	}
	void input(int cnt){
		int a, b;
		while(cnt--) cin>>a>>b, connect(a, b);
	}

	// DO NOT USE THESE IN CLIENT CODES!!!
	void setpar(Node *par, Node *son, bool left){
		if(son) son->p = par;
		if(left) par->l = son;
		else par->r = son;
	}
	void rotate(Node *x){
		Node *p = x->p, *q = p->p;
		if(!p->is_root()) q->prop();
		p->prop(), x->prop();
		bool xdir = (x == p->l);
		if(!p->is_root()) setpar(q, x, (p == q->l));
		else x->p = q;
		setpar(p, x->ch(!xdir), xdir), setpar(x, p, !xdir);
		p->refresh(), x->refresh();
	}
	
	// splay methods. k, l, r are 1-indexed
	Node* splay(Node *x){
		x->prop();
		while(!x->is_root()){
			Node *p = x->p, *q = p->is_root() ? nullptr : p->p;
			if(q) rotate((x == p->l) == (p == q->l) ? p : x);
			rotate(x);
		}
		return x;
	}

	// link-cut ops
	// make a chain from x to the root of its global tree
	// x becomes the root of its splay tree
	// return, among the vertices in the previous chain that
	// contains the global root, the closest one to x
	Node* access(Node *x){
		splay(x);
		x->r = nullptr; x->refresh();
		Node *ret = x;
		while(x->p){
			Node *y = x->p; ret = y;
			splay(y);
			y->r = x; y->refresh();
			splay(x);
		}
		return ret;
	}
	Node* access(int i){return access(nodes[i]);}

	// y becomes parent of x in the global forest
	// TODO abort if x and y are in the same comp
	void link(Node *x, Node *y){
		access(x); access(y); assert(!x->l);
		x->l = y; y->p = x;
		x->refresh();
	}
	void link(int x, int y){link(nodes[x], nodes[y]);}

	// cut x from its parent in the global forest
	void cut(Node *x){
		access(x); assert(x->l);
		x->l = x->l->p = nullptr;
		x->refresh();
	}
	void cut(int x){cut(nodes[x]);}

	// node representing a path x--y
	Node* path(Node *x, Node *y){reroot(x); access(y); return y;}
	Node* path(int x, int y){return path(nodes[x], nodes[y]);}
	void path_update(Node *x, Node *y, typename Node::slazy_t v){
		path(x, y)->lazy_add(v);
	}
	void path_update(int x, int y, typename Node::slazy_t v){
		path_update(nodes[x], nodes[y], v);
	}

	// find lca(x,y) in the global tree containing x and y
	Node* lca(Node *x, Node *y){access(x); return access(y);}
	int lca(int x, int y){return lca(nodes[x], nodes[y])->no;}

	// find root of the global tree containing x
	// that root is then splayed
	Node* root(Node *x){
		access(x);
		while(x->l) x = x->l->prop();
		return splay(x);
	}
	int root(int x){return root(nodes[x])->no;}
	bool is_root(Node *x){access(x); return !x->l;}
	bool is_root(int x){return is_root(nodes[x]);}

	// find parent of x in the global tree, and splay it
	Node* parent(Node *x){
		access(x); x = x->prop()->l; assert(x);
		x->prop();
		while(x->r) x = x->r->prop();
		return splay(x);
	}
	int parent(int x){return parent(nodes[x])->no;}

	// find depth of x in the global tree containing x
	// root has depth 0
	int depth(Node *x){access(x); return x->l ? x->l->cnt : 0;}
	int depth(int x){return depth(nodes[x]);}

	// reroot x in its global tree
	Node* reroot(Node *x){access(x); return splay(x)->flip();}
	Node* reroot(int x){return reroot(nodes[x]);}

	// connect x and y in the global forest
	void connect(Node *x, Node *y){reroot(x); link(x, y);}
	void connect(int x, int y){connect(nodes[x], nodes[y]);}

	// disconnect x and y in the global forest
	void disconnect(Node *x, Node *y){reroot(x);
		assert(root(x) == x);
		assert(parent(y) == x); cut(y);
	}
	void disconnect(int x, int y){disconnect(nodes[x], nodes[y]);}

	// check whether x and y are in the same global tree
	bool connected(Node *x, Node *y){return root(x) == root(y);}
	bool connected(int x, int y){return connected(nodes[x], nodes[y]);}
};

struct Snode{
	typedef ll scont_t; // element
	typedef ll snode_t;
	snode_t leaf_val(scont_t c){
		return c;
	}
	// a left, b right
	snode_t combine(snode_t a, snode_t b){
		return a+b;
	}

	typedef ll slazy_t;
	const slazy_t LID = -666; // MUST BE AN UNUSED VALUE
	// apply a <- b
	slazy_t combine_lazy(slazy_t a, slazy_t b){
		return a+b;
	}
	void unlazy(){
		content+= lazy;
		val+= cnt * lazy;
	}
	void undoflip(){
		;
	}
	////////////////////////////////////////////////////////////
	Snode *l = nullptr, *r = nullptr, *p = nullptr;
	scont_t content; int no = 0;
	snode_t val;
	slazy_t lazy = LID; bool doflip = false;
	int cnt = 1;

	Snode(scont_t c): content(c) {val = leaf_val(content);}

	// push, pull, and query
	Snode* refresh(){
		val = leaf_val(content), cnt = 1;
		if(l) l->prop(), val = combine(l->val, val), cnt += l->cnt;
		if(r) r->prop(), val = combine(val, r->val), cnt += r->cnt;
		return this;
	}
	void lazy_add(slazy_t x){
		lazy = combine_lazy(lazy, x);
	}
	Snode* flip(){doflip = !doflip; return this;}
	Snode* prop(){
		if(doflip){
			if(l) l->flip();
			if(r) r->flip();
			swap(l, r), undoflip(), doflip = false;
		}
		if(lazy != LID){
			if(l) l->lazy_add(lazy);
			if(r) r->lazy_add(lazy);
			unlazy(), lazy = LID;
		}
		return this;
	}

	// helper funcs
	bool is_root(){return !p || (this != p->l && this != p->r);}
	bool is_left(){
		assert(!p || p->lazy == LID);
		return p && p->l == this;
	}
	Snode *ch(bool left){
		assert(lazy == LID);
		return left? l : r;
	}
};