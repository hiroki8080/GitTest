#coding : shift-jis
print "Calendar"

wday = ("sun","smon","tue","wed","thu","fri","sat")
    #cal0(n,m)�͂P�̌��̃J�����_�[���쐬����B
    #n�͌��̊J�n���̗j����\������(0����6)�ł���A
    #0�͓��j�����Ӗ�����B
    #m�͂��̌��̓����ł���B���Ƃ���1����m=31�ł���B
    #����������2000�N1���̃J�����_�[��cal0(6,31)�ŕ\�������B
def cal0(n,m):
    for x in wday: print " ",x,
    print
    for x in range(0, n): print "  ---",
    for x in range(1, m+1):
            print "%5d"%x,
            if (x+n)%7==0 : print
    print
cal0(6,31)

    
