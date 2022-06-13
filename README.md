
# GI-projekat
Projektni zadatak za predmet Genomska Informatika, implementacija 'string-searching' algoritma
Link ka prezentaciji:

https://youtu.be/bh-5pdnlNeE
## Instrukcije za pokretanje

# GI - project

## About <a name = "about"></a>

School project task for subject of genomic informatics. Implementation of different heuristics for better string search algorithm. Using Boyer Moor approach with Bad character rule and Good suffix rule. Adding 2 new heuristics and comparing performance.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

You will need python 3 installed and set up on your computer.

### Testing

From command line use this:

1.a -i/--input      => absolute path to fasta file </br>
1.b -s/--search     => word to search for </br>
1.c -he/--heuristic => Number for heuristic to use </br>
------------> 1) RLongestGap </br>
------------> 2) LLongestGap </br>
------------> 3) LLongestGap + RLongestGap </br>
------------> 4) Bad Character + Good Suffix </br>
1.d -a/--alphabet    => Alphabet </br>

    ```
    python .\src\script.py -i {fasta file path} -s {search string} -he 1 -a {alfabet}
    ```

For example:

```
python .\src\script.py -i "C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/chr1.fna" -s 'ATATTTTTTTTTTTTT' -he 1 -a 'ACTG'
```

2. In the project, there is main test script that will go through 3 fasta files and search with 3 different words for each heuristic implementation.

```
    python .\src\test\main_test_script.py
```

Note: You will need to modify your path to these files, because files are not in this repository. Modify lines number 31,44 and 56 in the \src\test\main_test_script.py file. </br>


### Authors

Lazar Manic and Tamara Sretkovic
