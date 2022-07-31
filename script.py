import sys
from array import *
from itertools import product

def right_equation(input_file,output_file):
    catch = []      
    line_array = []
    removed_duplicates = []     
    w_results = []          

    with open(input_file) as my_file:               
        for line in my_file:
            line_array.append(line)
    with open(input_file) as my_file:
        w_results = [line.rstrip() for line in my_file]         
        
    elements(line_array,catch)
    switch = []         
    
    differences(switch,catch)
    
    switch = sorted(switch)
    temporary_array = []        
 
    for trans in catch:
        length = len(trans)
        for x in range(length):
            if x > 0:
                temporary_array.append("m-" + substring + ">=" + trans[x] + "_c")
                substring = "{}-{}_c+{}_p".format(substring, trans[x], trans[x])
            elif x == 0:
                temporary_array.append("m>=" + str(trans[0]) + "_c")            
                if length > 1:
                    substring = "{}_c+{}_p".format(trans[0], trans[0])
            else:               
                break
            

    for duplicate in temporary_array:           
        if duplicate not in removed_duplicates:         
            removed_duplicates.append(duplicate)

    write_right_equation(output_file,removed_duplicates)        
    wrong_equation(switch,output_file,w_results)           
    
def substrings(substring_array,w_results):      
    for i in range(len(w_results)):
        for j in range(len(w_results[i])+1):
            x = w_results[i][0:j]         
            if x not in substring_array:      
                substring_array.append(x)

    substring_array = sorted(substring_array, key=len)          
        
def wrong_equation(switch,output_file,w_results):
    substring_array = []            
    f_w_results = []

    substrings(substring_array,w_results)           
    correct_incorrect_combinations(substring_array, switch, output_file, f_w_results)
    write_wrong_equation(output_file,f_w_results)

def correct_incorrect_combinations(substring_array, switch, output_file, f_w_results):         
    for trans in substring_array:
        for x in switch:
            if len(trans) >= 1:
                if trans[len(trans)-1] != x:            
                    temp = trans[len(trans)-1]              
                    if temp not in f_w_results:             
                        f_w_results.append(temp)
            if trans+x not in f_w_results:          
                f_w_results.append(trans+x)

    for trans in substring_array:       
        for i in range(len(f_w_results)-1):
            if trans == f_w_results[i]:
                f_w_results.remove(trans)           
                
    remove_duplicates(f_w_results)
         
def write_wrong_equation(output_file,f_w_results):      
    output = open(output_file, "a")       
    output.write("\n")        
    helper = []         

    for trans in f_w_results:
        substring = ""
        for x in range(len(trans)):
            if len(trans) == 1:
                helper.append("m<" + str(trans) + "_c")         
            elif len(trans) > 1:
                substring = substring + "-{}_c+{}_p".format(trans[x], trans[x])         
                if x == len(trans)-2:
                    helper.append("m" + str(substring) + "<" + trans[x+1] + "_c")
            else:
                break
            
    helper.sort(key=len)        
    for i in range(len(helper)):        
        output.write(helper[i])   
        output.write("\n")        

def files_manager(argv):
    input_file = sys.argv[1]                
    output_file = sys.argv[2]               
    right_equation(input_file,output_file)

def elements(line_array,catch):
    for trans in line_array:           
        catch.append(trans.strip())

def differences(switch,catch):
    for x in catch:             
        for transition in x:
            if transition not in switch:
                if transition.isalpha():            
                    switch.append(transition)

def write_right_equation(output_file,removed_duplicates):
    output = open(output_file, "a")           
    for x in removed_duplicates:       
        output.write(x)
        output.write("\n")           

def remove_duplicates(f_w_results):
    for i in range(3):          
        for trans in f_w_results:
            if len(trans) == 1:
                temp = trans
                for x in f_w_results:
                    if len(x) > 1:
                        if x[0:1] == temp:
                            f_w_results.remove(x)

def main():
    files_manager(sys.argv[2:])            

    
    
    
main()
