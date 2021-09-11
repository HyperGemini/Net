from _typeshed import Self
import cnf as f
from itertools import product, repeat
import os


def minisat_solve(problem_name, problem_dimacs, number_to_var):
    with open(f'problem_name.cnf', 'w') as f:
        f.write(problem_dimacs)

    os.system(f'minisat {problem_name}.cnf', f'{problem_name}_result')


def n_queens(n):
    cnf = f.CNF()

    # pij -> tacno ukoliko se na polju (i, j) nalazi dama

    # U svakoj vrsti mora da bude barem jedna dama
    for i in range(n):
        clause = [f'p{j}{i}' for j in range (n)]
        cnf.add_clause(clause)


    # U svakoj vrsti mora da bude najvise jedna dama
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                clause = [f'-p{k}{i}', f'-p{k}{j}']
                cnf.add_clause(clause)


    # U svakoj koloni mora biti najvise jedna dama
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1, n):
                clause = [f'-p{i}{k}', f'-p{j}{k}']
                cnf.add_clause(clause)


    # Nema dama koje se napadaju dijagonalno
    for i, j, k, l in product(range(n), repeat=4):
        if k > i and abs(k - i) == abs(l - j):
            clause = [f'-p{i}{j}', f'{k}{l}']
            cnf.add_clause(clause)

    
    minisat_solve(f'{n}_queens', cnf.dimacs(), cnf.number_to_var_name)



if __name__ == '__main__':
    cnf = f.CNF()
    cnf.add_clause(['p1', '-p2'])
    cnf.add_clause(['-p1', 'p2', '-p3'])
    
    print(cnf.dimacs())

