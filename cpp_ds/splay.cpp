struct Snode{
	typedef int scont_t; // element
	typedef int snode_t; // sum, L, R, ans
	snode_t leaf_val(scont_t c){
		return c;
	}
	// a left, b right
	snode_t combine(snode_t a, snode_t b){
		return a+b;
	}

	typedef bool slazy_t;
	const slazy_t LID = false;
	// apply a <- b
	slazy_t combine_lazy(slazy_t a, slazy_t b){
		return a^b;
	}
	void unlazy(){
		if(lazy) swap(l, r);
	}
	////////////////////////////////////////////////////////////
	Snode *l = nullptr, *r = nullptr, *p = nullptr;
	scont_t content;
	snode_t val;
	slazy_t lazy = LID;
	int cnt = 1;

	Snode(scont_t c): content(c) {val = leaf_val(content);}

	// push, pull, and query
	Snode* refresh(){
		val = leaf_val(content), cnt = 1;
		if(l) l->prop(), val = combine(l->val, val), cnt += l->cnt;
		if(r) r->prop(), val = combine(val, r->val), cnt += r->cnt;
		return this;
	}
	Snode* prop(){
		if(lazy == LID) return this;
		if(l) l->lazy = combine_lazy(l->lazy, lazy);
		if(r) r->lazy = combine_lazy(r->lazy, lazy);
		unlazy(); lazy = LID;
		return this;
	}
	void lazy_add(slazy_t x){
		lazy = combine_lazy(lazy, x);
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

template <typename Node>
struct Splay{
	int n;
	Node *root;
	vector<Node*> nodes;

	Splay(vector<typename Node::scont_t> conts): n(sz(conts)){
		nodes.push_back(root = new Node(0));
		for(int i=0; i<=n; i++){
			Node *s = new Node(i<n ? conts[i] : 0);
			setpar(nodes.back(), s, false);
			nodes.push_back(s);
		}
		for(int i=n+1; i>=0; i--) nodes[i]->refresh();
	}

	// DO NOT USE THESE IN CLIENT CODES!!!
	void setpar(Node *par, Node *son, bool left){
		if(son) son->p = par;
		if(left) par->l = son;
		else par->r = son;
	}
	void rotate(Node *x){
		Node *p = x->p, *q = p->is_root() ? nullptr : p->p;
		bool xdir = (x == p->l);
		if(q) setpar(q, x, (p == q->l));
		else x->p = nullptr, root = x;
		setpar(p, x->ch(!xdir), xdir), setpar(x, p, !xdir);
		p->refresh(), x->refresh();
	}
	
	// splay methods. l, r are 0-indexed
	Node* splay(Node *x){
		while(!x->is_root()){
			Node *p = x->p, *q = p->is_root() ? nullptr : p->p;
			if(q) rotate((x == p->l) == (p == q->l) ? p : x);
			rotate(x);
		}
		return root = x;
	}
	Node* splay_kth(int k){
		assert(0 <= k && k <= n+1);
		Node *x = root->prop();
		while(1){
			while(x->l && x->l->cnt > k+1) x = x->l->prop();
			if(x->l) k-= x->l->cnt;
			if(k-- < 0) break;
			x = x->r->prop();
		}
		return splay(x);
	}
	Node* interval(int l, int r){
		// l to r goes to root->r->l
		assert(0 <= l && l <= r && r < n);
		splay_kth(l-1);
		Node *x = root;
		root = x->r, root->p = NULL;
		splay_kth(r-l);
		setpar(x, root, false), root = x;
		return root->r->l->prop();
	}

	// insert and delete
	Node* insert(int k, typename Node::scont_t v){
		n++; splay_kth(k);
		Snode *x = new Snode(v);
		if(root->l) root->l->p = x;
		x->l = root->l, x->r = NULL;
		setpar(root, x, true);
		return splay(x);
	}
	void remove(int k){
		n--; splay_kth(k);
		Node *p = root->prop();
		if(!p->l) root = p->r, root->p = nullptr;
		else if(!p->r) root = p->l, root->p = nullptr;
		else{
			root = p->l, root->p = nullptr;
			Node *cur = root->prop();
			while (cur->r) cur = cur->r->prop();
			cur->r = p->r, p->r->p = cur;
			splay(cur);
		}
		delete p;
	}
};
