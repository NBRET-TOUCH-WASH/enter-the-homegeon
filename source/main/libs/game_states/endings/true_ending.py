"""
notes:
    ? docs:
        ? I said pick up the can.

    § TODO:
        § Amplify weapons on Wallhammer.

    % FIXME:
        % Target compromised: move in, move in.

        & FIX:
            & Overwatch, target one sterilized.

    µ WHYNOT:
        µ Overwatch reports possible hostiles inbound.

    ! IMPORTANT:
        ! Roger that. Waiting for contact. Over.

    $ LOGS:
        $ 06/11/2021
            $ 00:17AM
                $ alright so ive been fighting for OVER AN HOUR with python cuz
                $ for some reason i can't manage to import modules while in
                $ THIS VERY SPECIFIC file fo fuck it, i'm making the endings in
                $ the game-state file x)
            $ 00:31AM
                $ alright so it seems the problems comes from relative imports
                $ or some shit idk????
                $
                $ anyway i legit just remade the function here lol it's not that
                $ big anyway so meh who cares at this point my code is super
                $ spaghetti but whatever
"""


#encoding
#coding:utf-8


#libraries/modules
import sys
import os
import time


#import true_ending_frames as frames


#libs setup


#classes


#functions
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def true_ending():
    clearConsole()
    time.sleep(3.0)

    print("\nYou walk down the stairs...")
    time.sleep(1.5)
    print("Entering the basement.\n")
    time.sleep(2.5)
    print("Suddenly, something starts speaking.")
    time.sleep(3.0)
    clearConsole()

    #print("You look around...")
    #time.sleep(1.5)
    #print("Nothing.\n")
    #time.sleep(1.5)
    #print("")

    print("\n\"Cleverly done.\"\n")
    time.sleep(3.5)

    clearConsole()
    print("\n\"It was about time...\n")
    time.sleep(3.5)

    print("Sorry, may I have your name -again-?\"\n")
    time.sleep(1.5)
    endingName = input("> ")

    clearConsole()
    print("\n\"Ah.")
    time.sleep(1.0)
    print("That's right.\"\n")
    time.sleep(2.0)
    clearConsole()

    print("\n\"As I said, it was about time you arrived, {}.\"".format(endingName))
    time.sleep(3.0)

    clearConsole()
    print(frame1_1)
    time.sleep(1.0)
    clearConsole()
    print(frame1_2)
    time.sleep(1.0)
    clearConsole()
    print(frame1_3)
    #time.sleep(1.0)
    #clearConsole()
    #print(frames.frame1_4)
    time.sleep(3.0)
    print("\n\"We have been expecting you.\"\n")
    time.sleep(3.0)

    clearConsole()
    print("\n\"As they have witnessed the causes of this... situation, my employer has become interested in your")
    time.sleep(5.0)
    clearConsole()
    print("\n\"As they have witnessed the causes of this... situation, my employer has become interested in your \"services\".")
    time.sleep(3.0)

    clearConsole()
    print("\n\"They are ready to offer you a...")
    time.sleep(2.5)
    clearConsole()
    print("\n\"They are ready to offer you a... \"constrained\" contract.")
    time.sleep(3.0)
    print("They believe that in you lies the potential for a... deviation.\n")
    time.sleep(3.0)
    print("\nOf course, I believe you do consider this offer to be of such an importance that it... cannot be refused.\"\n")
    time.sleep(6.0)

    clearConsole()
    print("\n\"Again, cleverly done, {}, but you're not supposed to be here.".format(endingName))
    time.sleep(3.0)
    print("As a matter of fact, you're not.")
    time.sleep(2.5)
    print("You actually belong in a much more...")
    time.sleep(2.5)
    clearConsole()
    print("\n\"Again, cleverly done, {}, but you're not supposed to be here.\nAs a matter of fact, you're not.\nYou actually belong in a much more... \"manifold\" system.\"\n".format(endingName))
    time.sleep(6.0)

    clearConsole()
    print("\n\"That's why I'm here, {}.".format(endingName))
    time.sleep(2.5)
    print("Although rather than offer you the illusion of free choice, I will take the liberty of choosing for you...".format(endingName))
    time.sleep(6.0)
    clearConsole()
    print("\n\"That's why I'm here, {}.\nAlthough rather than offer you the illusion of free choice, I will take the liberty of choosing for you... \"how\" and \"when\" your time comes around again.\"\n".format(endingName))
    time.sleep(6.0)

    clearConsole()
    print("\n\"My employer previously mobilized a \"sizable\" number of hires ;")
    time.sleep(3.0)
    print("To no effect in the matters of their...")
    time.sleep(2.5)
    clearConsole()
    print("\n\"My employer previously mobilized a \"sizable\" number of hires ;\nTo no effect in the matters of their... \"fruition\".")
    time.sleep(3.0)
    print("We had not found a suitable heir to these hires, up until your \"arrival\" in this \"structure\".")
    time.sleep(6.0)

    clearConsole()
    print("\n\"As a side note, I would like to add that as much as we all do,")
    time.sleep(3.0)
    clearConsole()
    print("\n\"As a side note, I would like to add that as much as we all do, -You- should prepare for unforseen consequences.\"")
    time.sleep(3.0)

    clearConsole()
    print(frame2_1)
    time.sleep(3.0)
    print("\n\"On these weighted strings of words...")
    time.sleep(3.5)
    clearConsole()
    print(frame2_2)
    time.sleep(1.7)
    print("This is where I get off.\"\n")
    time.sleep(5.5)
    clearConsole()

    print("\nSUBJECT:\t\"{}\"\nSTATUS:\t\"[AWAITING ASSIGNMENT]\"\n".format(endingName))
    time.sleep(3.0)

    sys.exit(0)


#script
frame1_1 = """
@@@@@@@@@@@@@@@@@@@B##@#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@0rimAQd##@#Q0B#0sA@@@@@@@@@@@@@@
@@@@@@@@@@@m  _Q#B########@#@#} .#@@@@@@@@@@@
@@@@@@@@@@0  _sAdARR0QQB####Qdn   @@@@@@@@@@@
@@@@@@@@@@   ,i?iini}sAmmni   i   #@@@@@@@@@@
@@@@@@@@@@   =     ,^~rrr,        @@@@@@@@@@@
@@@@@@@@@@n  _                    @@@@@@@@@@@
@@@@@@@@@@A                       @@@@@@@@@@@
@@@@@@@@@@@                       @@@@@@@@@@@
@@@@@@@@@@                         @@@@@@@@@@
@@@@@@@@@@                         @@@@@@@@@@
@@@@@@@@@@d                       #@@@@@@@@@@
@@@@@@@@@@@                       @@@@@@@@@@@
@@@@@@@@@@@=                     ?@@@@@@@@@@@
@@@@@@@@@@@@                     @@@@@@@@@@@@
@@@@@@@@@@@@#                   @@@@@@@@@@@@@
@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@
@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@
@@@@@@@@@@@@#A                 B@@@@@@@@@@@@@
@@@@@@@@@@@                     .m@@@@@@@@@@@
@@@@@@@@}   m                   A  iB@@@@@@@@
@@@s        m                   d   _,^mB@@@@
                                0r~inmAmi_ ^#
                                m^^ri}ssssmi 
                                n=,=^rr?ii}nn
                     nnn,       ?..__,^^r~^^r
                    m}}??}      =....____~_,,
                     Asir       _   .._.,... 
                     s?,,            .  .    
                     s^__?             .     
                     m_ .=                   
       .             s.                      
                    Rs_                      
                    ds=.                     
         .          mn^_                     
,.        .         s}r,                     
"""

frame1_2 = """
@@@@@@@@@@@@@@@@@@@###@#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@Q}2dEB$##@#BQ##QZE@@@@@@@@@@@@@@
@@@@@@@@@@@d  ^B##########@#@#w >#@@@@@@@@@@@
@@@@@@@@@@Q  ^ZE$E88QBB#####B$f` _@@@@@@@@@@@
@@@@@@@@@@=  r2n22f2wZEddf2,  2   #@@@@@@@@@@
@@@@@@@@@@=  ?`    r]v}}}r.       @@@@@@@@@@@
@@@@@@@@@@f  ^                    @@@@@@@@@@@
@@@@@@@@@@E  =                    @@@@@@@@@@@
@@@@@@@@@@@  ,                    @@@@@@@@@@@
@@@@@@@@@@   -                     @@@@@@@@@@
@@@@@@@@@@                        .@@@@@@@@@@
@@@@@@@@@@$                       #@@@@@@@@@@
@@@@@@@@@@@             `-        @@@@@@@@@@@
@@@@@@@@@@@?                     n@@@@@@@@@@@
@@@@@@@@@@@@                     @@@@@@@@@@@@
@@@@@@@@@@@@#-                  @@@@@@@@@@@@@
@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@
@@@@@@@@@@@@@@-                @@@@@@@@@@@@@@
@@@@@@@@@@@@#E                 #@@@@@@@@@@@@@
@@@@@@@@@@@                     >d@@@@@@@@@@@
@@@@@@@@w   d                   E  2#@@@@@@@@
@@@Z      .,d`                  $, ,^r]d#@@@@
     ._-_,_-_                   Q}v2fdEd2^,]#
     . `.--.-                   d]]}2wZZZZd2_
     ,. `.-``                   f?r?]}}n22wff
     `-   .``        fffr       n>>^^r]]}v]]}
    .    `..        dwwnnw      ?>>>>^^^^v^rr
    _    `--         EZ2}_      ^===>>^>r>>>=
     _   `-,`        Znrr       =,,==>==>,,_-
     -.   -,-        Z]^^n      ___,,=_>_...`
      ,`  .,_        d^,>?     =---__-=-...` 
`.    `>  `_=`      _Z>---     =`...-_-.``   
.....``_, `-=_      8Z^,=,`    `  ``.,`      
-----`..=- -,,      $Z?>=-`         _        
,___-...->-`-,-     df]^=.          ` -__-`  
r>=,_____->`.--`    Zw}r=.         .         
"""

frame1_3 = """
@@@@@@@@@@@@@@@@@@@###@#@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@BUA08#Q##@@#B#@BN8@@@@@@@@@@@@@@
@@@@@@@@@@@0  c#######@@@@@@@@W~}@@@@@@@@@@@@
@@@@@@@@@@B  cN8Q8BBB####@@##Q6^ ?@@@@@@@@@@@
@@@@@@@@@@i  nAPAA6AWN8006A|-,A-  @@@@@@@@@@@
@@@@@@@@@@i  2^   ~nXjUUUn*'  -`  @@@@@@@@@@@
@@@@@@@@@@6  c                 -  @@@@@@@@@@@
@@@@@@@@@@8  i                 '  @@@@@@@@@@@
@@@@@@@@@@@  |                 :  @@@@@@@@@@@
@@@@@@@@@@`  r                    =@@@@@@@@@@
@@@@@@@@@@                        *@@@@@@@@@@
@@@@@@@@@@Q      `         `      @@@@@@@@@@@
@@@@@@@@@@@        `=   ^r        @@@@@@@@@@@
@@@@@@@@@@@2                     P@@@@@@@@@@@
@@@@@@@@@@@@                     @@@@@@@@@@@@
@@@@@@@@@@@@#r                 ~@@@@@@@@@@@@@
@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@
@@@@@@@@@@@@@@r                @@@@@@@@@@@@@@
@@@@@@@@@@@@#8                 #@@@@@@@@@@@@@
@@@@@@@@@@@ ~`                  }0@@@@@@@@@@@
@@@@@@@@W!  0                   8  A#@@@@@@@@
@@@N:-=  !*|0^                  Q|'|cnX0#@@@@
    ,*?r?|?r?=                  BUjA6080Ac|X#
 ,!!!*~^*rr*r                   0XXUAWNNNN0A?
:::=!|*~^*r^^         '-        62n2XUUPAAW66
-,,:=^r~~~*^^        666n       P}}ccnXXUjXXU
,,,!*===~^**!      `0WWPPW      2}}}}ccccjcnn
::,:?===!^rr!       :8NAU?      ciii}}c}n}}}i
===:!?:=!^r|^        NPnn'     `i||ii}ii}||?r
!!=!!r*==~r|r:       NXccP     !???||i?}?***^
~~=!~!|^=~*|?=       0c|}2     irrr??rir***^~
^*~~~~^}!!^?i^      ?N}rrr=    i^***r?r*^^~!=
*****^^?|~^ri?-     BNc|i|^    ^!~^^*|^~~!==,
rrrrr^**ir~r||!     QN2}ir^    ,=!!!?~!!=:,::
|???r***r}r^r|r`    06Xci*=   !--,:~^~r??r^~=
n}i|?????r}^*rr^   :NWUni*:-  -''':*~:'`  ```
"""

frame1_4 = """
@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#D0BB##@@@@###@#QB@@@@@@@@@@@@@@
@@@@@@@@@@@B`,Z#@#@@@@@@@@@@@@8VH@@@@@@@@@@@@
@@@@@@@@@@#  ZQB#B######@@@@##82?X@@@@@@@@@@@
@@@@@@@@@@m  W0$00808QBBB80fi}0i:^@@@@@@@@@@@
@@@@@@@@@@m  d2``^VWE6DDDWtv* i| ~@@@@@@@@@@@
@@@@@@@@@@8  Z       `_`       i  @@@@@@@@@@@
@@@@@@@@@@B  m                 v  @@@@@@@@@@@
@@@@@@@@@@@  f                 } _@@@@@@@@@@@
@@@@@@@@@@|  w                 ~  c@@@@@@@@@@
@@@@@@@@@@^  `                    t@@@@@@@@@@
@@@@@@@@@@#     ^?-       =?>     @@@@@@@@@@@
@@@@@@@@@@@~    =>,|c^ ~2w=_^    ^@@@@@@@@@@@
@@@@@@@@@@@d       `,: =:=:      $@@@@@@@@@@@
@@@@@@@@@@@@         , _-        @@@@@@@@@@@@
@@@@@@@@@@@@@w      ^' '*-     V@@@@@@@@@@@@@
@@@@@@@@@@@@@@      `   _      @@@@@@@@@@@@@@
@@@@@@@@@@@@@@w   `           `@@@@@@@@@@@@@@
@@@@@@@@@@@@@B                 #@@@@@@@@@@@@@
@@@@@@@@@@@-V?                  HB@@@@@@@@@@@
@@@@@@@@8n -B^  -='         '   B-?0#@@@@@@@@
@@@Q}ic>^ntfB2    __`     `'    #fvfZWEB#@@@@
^   }tXwXfXwXc      =_  _`      #D608BBB0ZfE@
_}nnntV2twwtw_'      ,-,_      =BEED08QQQQB0X
}}}cnftV2tw22         vi       ~8dWdEDD$00888
i}}}c2wVVVt22       =888W     `:$HHZZWEED6EED
}}}ntcccV2ttn'     |B88$$8=    :dHHHHZZZZ6ZWW
}}}}Xcccn2wwn,      }BQ0DX     >ZmmmHHZHWHHHm
ccc}nX}cn2wf2*       Q$WWv     ?mffmmHmmHffXw
nncnnwtccVwfw}       QEZZ$     nXXXffmXHXttt2
VVcnVnf2cVtfXc      'BZfHd,    mwwwXXwmwttt2V
2tVVVV2Hnn2Xm2-     XQHwwwc    m2tttwXwt22Vnc
ttttt22XfV2wmXi     #QZfmf2   `2nV22tf2VVncc}
wwwww2ttmwVwffn     #QdHmw2   ^}cnnnXVnnc}}}}
fXXXwtttwHw2wfw?   ^B8EZmtc~  nii}}V2VwXXw2Vc
WHmfXXXXXwH2tww2   }Q8DWmt}i  ivvv}tV}v?????|
"""

frame1_4 = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@####@#@@@@@@@@@##@@@@@@@@@@@@@@
@@@@@@@@@@@#VfQ@@@@@@@@@@@@@@@#0Q@@@@@@@@@@@@
@@@@@@@@@@@^VQ####@@@@@@@@@@@##0%8@@@@@@@@@@@
@@@@@@@@@@Q (B#############8OR#OUZ@@@@@@@@@@@
@@@@@@@@@@Q ^B0VzZ0BBB###Bg6ZcO6}S@@@@@@@@@@@
@@@@@@@@@@# <Q ~~=~r}zsV}}ln}>`O~?@@@@@@@@@@@
@@@@@@@@@@# rQ =>~=!~~~~~^rix` 6~*@@@@@@@@@@@
@@@@@@@@@@@ ^8 ,<~=!~~!!~^*|}. D~X@@@@@@@@@@@
@@@@@@@@@@6 :8 .~~=:==!~~~*?i` S^VN@@@@@@@@@@
@@@@@@@@@@Z>,V  ~=::!<>~~!~rv: `<ig@@@@@@@@@@
@@@@@@@@@@#?~  (Zdw]|r^*inmdHv  :~@@@@@@@@@@@
@@@@@@@@@@@S   }KHf6NA}S08mXZx   A@@@@@@@@@@@
@@@@@@@@@@@B' =v]xnzhU}KUKUn}v  =#@@@@@@@@@@@
@@@@@@@@@@@@x `?vixxVh(Xwcc}?r  ?@@@@@@@@@@@@
@@@@@@@@@@@@@8.:r*^}Zj?jZw?~^  0@@@@@@@@@@@@@
@@@@@@@@@@@@@@( vicnzlvisn}?'  @@@@@@@@@@@@@@
@@@@@@@@@@@@@@8 ^}Vciv}ii]}v, V@@@@@@@@@@@@@@
@@@@@@@@@@@@@#:~^l}c}lnc}vv<  ^@@@@@@@@@@@@@@
@@@@@@@@@@@w0d n}VVx(i}}ii?`., rQ#@@@@@@@@@@@
@@@@@@@@#$}w#Z?<wmjllxv(ii<}jv -#w%#@@@@@@@@@
@@@#DONHZ$g8#0?~=?Xszn}xlnVj?,:?#868QBB#@@@@@
ZnxVRg8888888Nn!"::xmXncsVx:-,!c@#B######Q8B@
sR$$$g00g88g8sj*,~:,>hwhX*`'_"<m#BB#########8
DDDN$8g00g800nli==~=,^6O=`'-,=vS#BBBB########
ORRDN08000g00n*v?:~^m###Bx,,=~zU#QQQQBBB#BBB#
RRR$gNNN00gg$j~~?*?6######m^,i]UBQQQQQQQQBQBB
DDRD8NNN$088$f==:<iiD####8virr|HQQQQQQQQBQQQQ
NNND$8DN$0880Z=::__~c##BB6l^~*(dQ88QQQQQQ8888
$$N$$8gNN0888D~"='':i#BQQ#l=!*?$88888Q8Q8ggg0
00N$0$80N0g88Nv"!'."j#Q8QBf~=**Q888888Q8ggg00
0g00000Q$$08Q0w:!'.=8#Q888N*=^vQ0ggg888g000$N
ggggg0088008Q8O=='.^@#Q8Q80|=>V0$000g8000$NNR
888880ggQ80888$x!-.n##BQQ80l=~ARN$$$80$$NDRDD
88888ggg8Q80888d~,.A##BQQgNS=~$OORD000888800N
BQQ8888888Q0g880n:.D###BQgDO=iO666Dg0D6d%%dd6
"""

frame2_1 = r"""
@@@@###BBQQQQQQQQQQQQQQQQQQQQQQB###@@@@
@@@#B8OWA5GGPPPPPPPPPPPPPPPPGSHZd$Q##@@
@@#BNt_-------------------------_r%Q#@@
@@#8W]                           :U$B#@
@@#gqi                           :eEQ#@
@##0Sv                           :wOQ#@
@#B0Sv                           "o6Q#@
@#B&Sv                           "j6Q#@
@#B&Gv           "v|"            "j6Q#@
@#B&G|           *Vn>            "j6Q#@
@#B$P|           =zV-            "j6Q#@
@#B$P|        ':rjAP}>,`         "j6Q#@
@#B$P|       ^nUWDg0EAw]`        "y6Q#@
@#B$P|       |h60QBBQ&ZJ,        ,t6Q#@
@#B$P|       vKRQ####86j,        "t6Q#@
@#B$P|      `}qNQ####QRh~        "tdQ#@
@#B$P|      -nZ&Q####B&Pv        "y6Q#@
@#B$P|      'uZ$Q####B8Zn'       "t6Q#@
@#B$P|      `]5DQ####B8dz=       "y6Q#@
@#B$P|       ?f6gB###Q&znr       "tdQ#@
@#B$P|       =cm68B#BQ6r:v.      "tdQ#@
@#B$P|        '=o688886r!i'      "t6Q#@
@#B$P|          imdiX08DbKn<     "t6Q#@
@#B$P|          ^jU!*68D0OU?     "t6Q#@
@#B$P|          ,nt:,PR50EKv     "t6Q#@
@#B&G|          `]V=`oZld%Ux     "j6Q#@
@#B&Gv           ?V~`Vs>}zVv`    "j6Q#@
@#B0Sv           =n?`un. `_-     "o6Q#@
@##05v           -cn-l}`         "oOQ#@
@@#gqi           `vz<Vv          :sEQ#@
@@#8W]            ~2?i^`         :UNB#@
@@#BNz_----------_?z!_----------_rW8#@@
@@@#B8OWqSPPPPP5AWEDRdWAHSPPPP5Zd$Q##@@
@@@@@##BBBQQQQQBBB####BBBQQQQQBB###@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

frame2_2 = r"""
    `.-_,,,,,,,,,,,,,,,,,,,,,,,__'``   
   ._=<*r???((((((((((((((((???r^!,-`  
  `,~}B#########################BA*:'` 
 `':*w@@@@@@@@@@@@@@@@@@@@@@@@@@@8v~_` 
 `-=?h@@@@@@@@@@@@@@@@@@@@@@@@@@@Qx<,. 
 `_!?U@@@@@@@@@@@@@@@@@@@@@@@@@@@Q]^,. 
 `_!?U@@@@@@@@@@@@@@@@@@@@@@@@@@@Q]^,' 
 `_!?m@@@@@@@@@@@@@@@@@@@@@@@@@@@Q]^,. 
 `_!?m@@@@@@@@@@@QUmQ@@@@@@@@@@@@Q}^,' 
 `_!?m@@@@@@@@@@@WnnR@@@@@@@@@@@@Q}^,' 
 `_!(m@@@@@@@@@@@8}n#@@@@@@@@@@@@Q}^,' 
 `_!(m@@@@@@@@#8Z]r(zRQ#@@@@@@@@@Q}^,' 
 `_!(K@@@@@@@6nv*~=!<r]w#@@@@@@@@Q}^"' 
 `_~(K@@@@@@@mi^!,__,!rlB@@@@@@@@Q}^"' 
 `_~(K@@@@@@@f(~:-..-:^]Q@@@@@@@@Q}^"' 
 `_~(K@@@@@@@j?~,-``',>iD@@@@@@@@Q}^"' 
 `_~(K@@@@@@#nr!,-``._!(f@@@@@@@@Q}^,' 
 `_~(K@@@@@@#Vr!,-```_=rV#@@@@@@@Q}^,' 
 `_~(K@@@@@@@j?~"-.`._:^}8@@@@@@@Q}^"' 
 `_~(K@@@@@@@5v^=,-.-,!}nA@@@@@@@Q}^"' 
 `_~(K@@@@@@@8V|^=,-_:^Z8f#@@@@@@Q}^"' 
 `_~(K@@@@@@@@#8]^==:=^W&h#@@@@@@Q}^"' 
 `_!(K@@@@@@@@@@h|^Xi!=~*(nE@@@@@Q}^"' 
 `_!(m@@@@@@@@@@d}v0W^=~!^v5@@@@@Q}^,' 
 `_!(m@@@@@@@@@@Qn}8B(>?!<|U@@@@@Q}^,' 
 `_!?m@@@@@@@@@@#jl8#]rJ^*vX@@@@@Q}^,' 
 `_!?m@@@@@@@@@@@SnN#l]Rz}uU@@@@@Q}^,' 
 `_!?U@@@@@@@@@@@gn5@VV#@#B#@@@@@Q]^,' 
 `_!?U@@@@@@@@@@@#Vn#Vj#@@@@@@@@@Q]^,. 
 `-=?h@@@@@@@@@@@@U}ElU@@@@@@@@@@Q]<,. 
 `':*w@@@@@@@@@@@@NlSXO#@@@@@@@@@8v~_` 
  `,~}B###########5}$B###########Z*:'` 
   ._=^r??(((((?r*<~>^rr??((((?r^!,-`  
    `.-__,,,,,,,__----__,,,,,,__-'``   
          ````           ````          
"""

#true_ending()#!!!!!!!!!!!!!!!!!!!!DEBUG!!!!!!!!!!!! TO REMOVE!!!!!!!!!!!!!!!!