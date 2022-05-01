////// Point polar sorting //////
// DEPENDENCY: POINT

// ccw, tiebreaker is distance
TTT void polar_sort(vector<Pnt<T>> &V, Pnt<T> c){
	auto pnt_half = [](Pnt<T> p){
		assert(p.x != 0 || p.y != 0);
		return p.y > 0 || (p.y == 0 && p.x < 0);
	};
	for(Pnt<T> &p: V) p-= c;
	sort(entire(V), [&](Pnt<T> v, Pnt<T> w){
		return make_tuple(pnt_half(v), T(0), sq(v)) <
			make_tuple(pnt_half(w), cross(v,w), sq(w));
	});
	for(Pnt<T> &p: V) p+= c;
}

TTT vector<int> polar_sorted_halfplanes(vector<Pnt<T>> &P, const Pnt<T> &c){
	int n = sz(P), ri = 0;
	vector<int> ans;
	for(int li=0; li<n; li++){
		assert(P[li] != c);
		while(ri < li+n && orient(P[li], c, P[ri%n]) <= 0) ri++;
		ans.push_back(ri-1);
	}
	return ans;
}