# Pass-genner Tool

Tools to generate strong unique passwords and unique usernames.

## How to use

#### Password generator
generate a 16 character password with atleast 5 numbers and 0 special characters 
```
python passgenner.py -L 16 -N 5 -S 0
> XpB6f3Ifeov52aJ6
```

generate a random pin
```
python passgenner.py -L 6 -N 6 -S 0
> 429666
```

generate a longest password
```
python passgenner.py -L 256
> %,Q+AZgmk5?`YZ]>U~aT9B:-[>2D$~t"Tc';.}[N]9\}1IPT'$.WSzGx&#.zgwBO$]eKST0_YvsP\>Fl~L?q7tW\tcc!>,E}`j-$-#&IECJB!Z6/#{yC~ZCdde,V,-C=2[=n`c^r3(=v397(=ta`*6MRDVAl%pZTx;Qeu8b_}aCR',SAe!(i`MUJ_l?.`,n1+x{Bx}PgBGr0HOpR-c:_"FnktY1azvNM8,)_78QOY*6u{"]k3`$20QVi(sd[A|R-
```

#### Username generator
_Note! The username generator depends on the size of the **wordlist** file/files being large enough to generate many unique usernames without repeating, I am working on making the word lists as large as I possibly can_

generate username
```
python username.py
> Your username is leaderene577

python username.py
> Your username is leila_mirei687
```

