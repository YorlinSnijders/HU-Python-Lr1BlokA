import random

def monopolyworp():
    steen1_1 = random.randrange(1,7)
    steen1_2 = random.randrange(1,7)
    steen2_1 = random.randrange(1,7)
    steen2_2 = random.randrange(1,7)
    steen3_1 = random.randrange(1,7)
    steen3_2 = random.randrange(1,7)

    if steen1_1 == steen1_2:
        if steen2_1 == steen2_2:
            if steen3_1 == steen3_2:
                print('%d + %d = %d (dubbel)' % (steen1_1, steen1_2, (steen1_1 + steen1_2)))
                print('%d + %d = %d (dubbel)' % (steen2_1, steen2_2, (steen2_1 + steen2_2)))
                print('%d + %d = direct naar gevangenis\n' % (steen3_1, steen3_2))
            else:
                print('%d + %d = %d (dubbel)' % (steen1_1, steen1_2, (steen1_1 + steen1_2)))
                print('%d + %d = %d (dubbel)' % (steen2_1, steen2_2, (steen2_1 + steen2_2)))
                print('%d + %d = %d\n' % (steen3_1, steen3_2, (steen3_1 + steen3_2)))
        else:
            print('%d + %d = %d (dubbel)' % (steen1_1, steen1_2, (steen1_1 + steen1_2)))
            print('%d + %d = %d\n' % (steen2_1, steen2_2, (steen2_1 + steen2_2)))
    else:
        print('%d + %d = %d\n' % (steen1_1, steen1_2, (steen1_1 + steen1_2)))

monopolyworp()