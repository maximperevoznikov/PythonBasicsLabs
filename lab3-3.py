"""
Написать программу для транслитерации фамилии, имени, отчества для загранпаспорта по установленным МВД РФ требованиям:
А (а) -> A (a)   Ж (ж) -> Zh (zh)    Н (н) -> N (n)   Ф (ф) -> F (f)        Ъ (ъ) -> Ie (ie)  
Б (б) -> B (b)   З (з) -> Z (z)      О (о) -> O (o)   Х (х) -> Kh (kh)      Э (э) -> E (e)  
В (в) -> V (v)   И (и) -> I (i)      П (п) -> P (p)   Ц (ц) -> Ts (ts)      Ю (ю) -> Iu (iu)  
Г (г) -> G (g)   Й (й) -> I (i)      Р (р) -> R (r)   Ч (ч) -> Ch (ch)      Я (я) -> Ia (ia)  
Д (д) -> D (d)   К (к) -> K (k)      С (с) -> S (s)   Ш (ш) -> Sh (sh)      ь     -> не пишется  
Е (е) -> E (e)   Л (л) -> L (l)      Т (т) -> T (t)   Щ (щ) -> Shch (shch)  
Ё (ё) -> E (e)   М (м) -> M (m)      У (у) -> U (u)   Ы (ы) -> Y (y)
Например, для строки: Попов Василий Вячеславович, формат вывода будет: Popov Vasilii Viacheslavovich
"""

cyril = "А.а.Б.б.В.в.Г.г.Д.д.Е.е.Ё.ё.Ж.ж.З.з.И.и.Й.й.К.к.Л.л.М.м.Н.н.О.о.П.п.Р.р.С.с.Т.т.У.у.Ф.ф.Ч.ч.Ц.ц.Ч.ч.Ш.ш.Щ.щ.Ы.ы.Ъ.ъ.Э.э.Ю.ю.Я.я.Ь.ь"
cyril = cyril.split('.')
translit = "A.a.B.b.V.v.G.g.D.d.E.e.E.e.Zh.zh.Z.z.I.i.I.i.K.k.L.l.M.m.N.n.O.o.P.p.R.r.S.s.T.t.U.u.F.f.Ch.ch.Ts.ts.Ch.ch.Sh.sh.Shch.shch.Y.y.Ie.ie.E.e.Iu.iu.Ia.ia.."
translit = translit.split('.')
print("Введите строку")
string = input()
for c in string:
    if c in cyril and c!='.':
        string = string.replace(c, translit[cyril.index(c)])
print(string)