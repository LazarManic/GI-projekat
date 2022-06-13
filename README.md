# GI-projekat
Projektni zadatak za predmet Genomska Informatika, implementacija 'string-searching' algoritma
Link ka prezentaciji:

https://youtu.be/bh-5pdnlNeE
## Instrukcije za pokretanje

1. Iz komandne linije pokrenuti sledecu komandu:

1.a -i/--input      => putanja do fasta fajla
1.b -s/--search     => rec za pretragu
1.c -he/--heuristic => Redni broj heuristike kojom zelite izvrsiti pretrazivanje
------------> 1) Heuristika 1
------------> 2) Heuristika 2
------------> 3) Heuristika 1 + Heuristika 2
------------> 4) Bad Character + Good Suffix
1.d -a/--alfabet    => Skup karaktera koji se pojavljuju u tekstu za pretrazivanje
    python .\src\script.py -i {fasta file path} -s {search string} -he 1 -a {alfabet}

Na primer ovako:

python .\src\script.py -i "C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/chr1.fna" -s 'ATATTTTTTTTTTTTT' -he 1 -a 'ACTG'


2. U projektu se nalazi test koji prolazi kroz 3 test fasta fajlova, pretrazuje pomocu svih implementacija heuristika i pretrazuje po 3 reci razlicite duzine za svaki test

    python .\src\test\main_test_script.py

Paznja: Morate izmeniti linije broj 20,39,55 tako da putanja do samog fasta test fajla bude odgovarajuca