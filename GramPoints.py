import pdb
import csv
from decimal import *
from math import *
def as_exp_theta(x, n):
        return (x/2)*(log(x/(2*pi), e)) - x/2 - pi/8 + 1/(48*x) + 7/(5760*(x**3)) - pi*n+pi;
def numerical_solution(seed, prec, n):
        return numerical_solution_recursion(seed, prec, 100, n);
def numerical_solution_recursion(curr_x, prec, step, n):
        cur_val=as_exp_theta(curr_x, n)
        next_val_plus=as_exp_theta(curr_x+step, n)
        if(curr_x-step >= 7.0):
            next_val_minus=as_exp_theta(curr_x-step, n);
        else:
            next_val_minus=as_exp_theta(7.0, n);
        while ((next_val_plus*cur_val > 0) & (next_val_minus*cur_val > 0)):
            cur_val=as_exp_theta(curr_x, n)
            next_val_plus=as_exp_theta(curr_x+step, n)
            if(curr_x-step >= 7.0):
                next_val_minus=as_exp_theta(curr_x-step, n);
            if(curr_x-step < 7.0):
                next_val_minus=as_exp_theta(7.0, n);
            if((curr_x-step >= 7.0) & (abs(next_val_plus) <= abs(next_val_minus))):
                    curr_x=curr_x+step
            elif((curr_x-step >= 7.0) & (abs(next_val_plus) >= abs(next_val_minus))):
                    curr_x=curr_x-step
            elif((curr_x-step < 7.0) & (abs(next_val_plus) >= abs(next_val_minus))):
                    curr_x=7.0
            elif((curr_x-step < 7.0) & (abs(next_val_plus) <= abs(next_val_minus))):
                    curr_x=curr_x+step
                    
        if((step<=prec) & ((next_val_minus*cur_val <= 0) | (next_val_plus*cur_val <= 0))):
                return curr_x;
        if(next_val_plus*cur_val < 0):
                    return numerical_solution_recursion(curr_x+step, prec, float(step/2), n);
        elif((curr_x-step >= 7.0) & (next_val_minus*cur_val < 0)):
                    return numerical_solution_recursion(curr_x-step, prec, float(step/2), n);
        elif((curr_x-step < 7.0) & (next_val_minus*cur_val < 0)):
                    return numerical_solution_recursion(7.0, prec, float(step/2), n);

table=open('gram_points','w')
with table:
    gram_fields = ['n', 'n-th gram point']
    writer = csv.DictWriter(table, fieldnames=gram_fields)
    for x in range(0,100000):
        if(x%1000==0):
            print("Progress: ", x*0.0001, "%")
        writer.writerow({'n': x, 'n-th gram point' : numerical_solution(8, 0.0000001, x)});

