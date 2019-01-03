template<typename T, int D> struct mvector {using type = vector<typename mvector<T, D - 1>::type>;};
template<typename T> struct mvector<T, 0> {using type = T;};
template<typename T, int D> using mvector_t = typename mvector<T, D>::type;
template<typename T, typename U> vector<T> make(U v) {return vector<T>(v);}
template<typename T, typename U, typename... Sz>
mvector_t<T, sizeof...(Sz) + 1> make(U v, Sz... sz){return mvector_t<T, sizeof...(Sz) + 1> (v, make<T>(sz...));}
