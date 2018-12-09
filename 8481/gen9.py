import base64, zlib
def decipher(s): return zlib.decompress(base64.b85decode(s)).decode('utf-8')
__import__('sys').stdout = open('res9.txt', 'w')

class Line:
    def __init__(_,sx,sy,ex,ey): _.sx,_.sy,_.ex,_.ey=sx,sy,ex,ey
    def __repr__(_): return f"{_.sx}{_.sy}{_.ex}{_.ey}"
    def draw(_, board):
        x = _.sx; y = _.sy
        for i in range(_.length()+1): board[y][x] = "#"; x+= _.dx(); y+= _.dy()
    def length(_): return max(abs(_.ey-_.sy), abs(_.ex-_.sx))
    def dx(_): return 0 if _.sx == _.ex else (_.ex-_.sx) // abs(_.ex-_.sx)
    def dy(_): return 0 if _.sy == _.ey else (_.ey-_.sy) // abs(_.ey-_.sy)

class gen9:
    def gen(_):
        board = [['.']*1003 for i in range(1003)]
        Z = b'c$__#Tec-32ty}yK74^N|A}>WtlMk#?HsEt6$k;d)^G0lt10}&IluMmO8tMT^yU{kfZX|;VW{d~<nQYF9KWTnhUPEBEj>LN9z$jQw$@o!Zx3+x`rY|EHyN!?y*I2AzdGZ$+mJDSnsXNaZ@w7C2$-#<Lc=t0irYhL{^l49)PQOHzhzR~`qkxxTE1kZValF6WMTYz8)Qwd-(t`|ohcXpFKpH~x!?Lio$vV6f}L75r%rqso>ls3C~dHG$V>w#!GFoTz^;;;vJIGs$wTg)zaAK@r>ph#{ORn4%kP73PaHnCU}}NdhLE?n4%Wjk<?d8ydp?l&@_1NUWXnHw6z|`WeMi9}hI$cm0;ymu=57x!9FW7nwe%-v%<<vTSK5@Zy%bYxFG5o9!O{uyGNX-4Hs%#ibT07X3Bt0bF*ftcR(Sz_V5`CfS%sW>E{HH57UMRS4!L!PCAJ<pZf?ALAKA6_()Wq)#P6C9?>_$#hQOJ5WIL%Kgdds_Q=_e*FJp)-V9m4}K<JxGs|riGu>+@*LZ2~99ET%Qtm*x5Vm*Y$dL`24z1RjG`FrAx-twI0ifXASO|hxhhrGWZOK1N*i0{FL;FENk$CwaAt^tpxb}(*ZZ|$LjPt!|>SHw0MRuJmpCVFyBXf1FP-G<9LgJ{E!XF|mJa#quul=xkAhA&CK=CB0mae|#wR2=5j-cN$A>{~;jAKMrtp!@)GHj;FSYG7)wL|{adJJ@hK2<%uKfW$APtBiTb=%u`q20-jhfY2-*1td?_difG4U7!l%lLPI<8nR#_9+#9_sG8hm^l$0X+WJGB&^rBF%9r8AHdci)i-oPNY0<h1rTcV^AH#~b6mT#l5h0^1_`Ge{QZ5v1EObccmHIT!LZ(<=a?)A}yn43s7`ND3mw6(B1RvZS@}dsg7&uyi2XDXpBdx(!T1UJzCw;*?%4U4|f9z!~H{hH;Ck?BulL+yWZq}s?JlVPNRN#HC5ALV`T6#74vi{>?TXHJ?&%aM*`fvX>r^Gb43vLBwqqNGkLx^R*LoY1pF~wkuKczL1f;|~4SM(iqEW{ng7s(NIl5;HNWcvApzvSwmijl|p)>vQe>4?rn&LSk7taD{E;n<tG(^yED{iASAv_WUAYqWXW>bSN2_UA-r{Kr=PIRSG;)qDLM)g!`S>zKuN=#*0J$h1%!uw}ZDqV%VE-cCQLdvNv`L!R78z1qetFPAKJQHM+uWq9gydb?T#-{V;=e+S#hDjfyHSp}apOEIDh9SqSf`jX6WfqN-Pjn^`AD1l1h#o{rHAxGtgJZa30U_dY(gWh5y0HK4SLz5OpZYvT>uFzj6t;m<~{6M@#5CVqy5|nry5N{nwWjk2TE$wy6LW7Xk7*+x>MV{r}=9T)A+gkE?RD+B)ojPY@$HTd(Wy@|lRu|b1QKU_WC~->JMjg!k$bEuth03I7is;GDdHm3Es2|6GH|YgTYt(>NOPK`5q6=ZHbc=^5$su**Ww7$$3k}tt5TI`E$Oe7R;RN4b+E0_03i6?eVP)i)av(oqcPsy6E*Gkp+u<?Fo|yP%+P}>><F5%p#LLYH*mOy<H?$d8h3&DZnb))k@jA#Yg|jAY1n>WrTjA-HmTj#2eDb}1tI2%11PpO02rRv!JG@6ebN?*o13foL9^f`a6l_{p9H-3-kwJ*WqxsR0wj<lgvEgyj(;OGXo#DcF&Kswu-rH^}3K7A#*{%!0R?MN1yRVqj|A1sfNG&)jnDe~{`&=_1?kBj{gnuLjFaFKp<O9=*k+0s{fJQ<>QXq-~(3lz2Xi)QsK)W~`xI6jX#v+fYSr*4~qmc^^JcJ)09HHGNp!p}37rK&=zL-cX<lsgmXzfhfpxeuM6auSXo%~*_O5{r>uvfYQF%I{&>&04ezZ%oEBfM>?pj;0(pHQQQ2i{l*nZ9_XoETVK9F#y$w~P0_b}E}Tf4huaqW57jkB#Z+F?2q9GtT&s`x4#)DSH-ONT|b3Sj2a73?*2&X$c*o>oMY6ZVY{$Ak_5G`^h97@}=9^!*Nm8A;H{`EX4<@9QF!D2e#jsMzZnv{nx`@JBk8Rug<XPbwbcqb5tcfN2hAa=U1fchS2TtFzvbM5x(Z@`q+oXS021>9PT?mg@uVde1G7M^+JYlaAD)(fniC$hRH|wZ4z=}_^`D%#i5i)YYyW^@VS)Gm{aR$)PhT37ztCw(<_jM#}b<#%E=8a7Wbs#n^?(!DWdn~)@&oWzx0XM_sPlD&I!-x>#iG#{y0rBMeTXt)SLCupC1bEdVLaj#@qd<V#9XstB``e*T}VOLtMT0y#fVWF0)Nl9Y`~!miDu)v9zJaOTO#5Ti19f%bKI|UEX({>E$K_4Da)$Ge3qa1YdXj0~82O)B'
        Z = list(map(int, decipher(Z).split(',')))
        for i in range(0, len(Z), 4): Line(*Z[i:i+4]).draw(board)
        print('\n'.join(''.join(row) for row in board))
    
q = gen9()
q.gen()

assert open('gen9.out').read().rstrip() == open('res9.txt').read().rstrip()