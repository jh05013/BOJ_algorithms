__import__('sys').stdout = open('res5.txt', 'w')

one = ['', 'pierwszy', 'drugi', 'trzeci', 'czwarty', 'piaty', 'szosty', 'siodmy', 'osmy', 'dziewiaty', 'dziesiaty', 'jedenasty', 'dwunasty', 'trzynasty', 'czternasty', 'pietnasty', 'szesnasty', 'siedemnasty', 'osiemnasty', 'dziewietnasty', 'dwudziesty']
ten = ['', 'dziesiaty', 'dwudziesty', 'trzydziesty', 'czterdziesty', 'piecdziesiaty', 'szescdziesiaty', 'siedemdziesiaty', 'osiemdziesiaty', 'dziewiecdziesiaty']
hundflat= ['', 'setny', 'dwusetny', 'trzysetny']
hundred = ['', 'sto', 'dwiescie', 'trzysta']
month = ['', 'stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'wrzesnia', 'pazdziernika', 'listopada', 'grudnia']
year = ['dwutysiecznego', 'dwa tysiace pierwszego', 'dwa tysiace drugiego', 'dwa tysiace trzeciego']
def convert(n):
    if n < 20: return one[n]
    if n % 100 == 0: return hundflat[n//100]
    if n < 100: return (ten[n//10] + ' ' + one[n%10]).strip().replace('  ',' ')
    s = hundred[n//100] + ' ' + convert(n%100)
    return s.strip().replace('  ',' ')

from datetime import datetime, timedelta
class gen5:
    def __init__(_): _.d = datetime(2000, 1, 1); _.s = []
    def gennext(_, i):
        if i == 2647: _.s.append("Pierwszego kwietnia jest prima aprilis.")
        elif i == 4900: _.s.append("Pierwszego czerwca jest dzien dziecka.")        
        else:
            n = (_.d - datetime(_.d.year, 1, 1)).days + 1
            y = year[_.d.year-2000] if _.d.year <= 2003 else "dwa tysiace "+one[_.d.year-2000][:-1]+"ego"
            _.s.append(f"{convert(_.d.day).capitalize()} {month[_.d.month]} to {convert(n)} dzien roku {y}.")
        _.d+= timedelta(1)
    def gen(_):
        for i in range(7671): _.gennext(i)
        _.s.append("Koniec."); print('\n'.join(_.s))

q = gen5()
q.gen()

assert open('gen5.out').read().rstrip() == open('res5.txt').read().rstrip()