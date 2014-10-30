#coding : shift-jis
print "Calendar"

wday = ("sun","smon","tue","wed","thu","fri","sat")
    #cal0(n,m)は１つの月のカレンダーを作成する。
    #nは月の開始日の曜日を表す数字(0から6)であり、
    #0は日曜日を意味する。
    #mはその月の日数である。たとえば1月はm=31である。
    #したがって2000年1月のカレンダーはcal0(6,31)で表示される。
def cal0(n,m):
    for x in wday: print " ",x,
    print
    for x in range(0, n): print "  ---",
    for x in range(1, m+1):
            print "%5d"%x,
            if (x+n)%7==0 : print
    print
cal0(6,31)
cal0(10,1)
cal0(10,2)
cal0(11,6)