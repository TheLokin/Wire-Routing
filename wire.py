#!/usr/bin/python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys
import os

class AspSolver:
    def __init__(self, input_file, optimum):
        if not os.path.exists('wire.lp'):
            print('File not found: wire.lp')
            return
        if os.path.exists('tmp.lp'):
            os.remove('tmp.lp')
        with open('tmp.lp', 'w+') as output:
            try:
                with open(input_file) as input:
                    try:
                        rows = int(input.readline())
                        columns = int(input.readline())
                        self.__size = max(rows, columns)
                        output.write('#program initial.\n')
                        output.write('row(0..'+str(rows-1)+').\n')
                        output.write('column(0..'+str(columns-1)+').\n')
                        position = 0
                        path = {}
                        wire = {}
                        for line in input:
                            for char in line:
                                if char != '\n':
                                    if char != '.':
                                        if char == '#':
                                            path[position+1] = 'obstacle'
                                            output.write('obstacle('+str(position%self.__size)+','+str(position//self.__size)+').\n')
                                        else:
                                            if char not in wire:
                                                wire[char] = 1
                                                output.write('start('+str(position%self.__size)+','+str(position//self.__size)+','+char+').\n')
                                            else:
                                                wire[char] += 1
                                                output.write('end('+str(position%self.__size)+','+str(position//self.__size)+','+char+').\n')
                                    position += 1
                        if position != columns*rows:
                            print('File contain wrong arguments')
                            return
                        for key in wire:
                            if wire[key] != 2:
                                print('File contain wrong arguments')
                                return
                    except:
                        print('File contain wrong arguments')
                        return
            except:
                print('File not found:', input_file)
                return
        
        # Llamada a telingo
        if optimum:
            os.system('telingo --verbose=0 --quiet=1 wire.lp tmp.lp optimum.lp > solution.lp')
        else:
            os.system('telingo --verbose=0 --quiet=1 wire.lp tmp.lp > solution.lp')
        os.remove('tmp.lp')

        # Construye la ruta con la solución obtenida de telingo
        if os.path.exists('solution.txt'):
            os.remove('solution.txt')
        with open('solution.lp') as input:
            for line in input:
                if 'State' not in line:
                    continue
                line = input.readline().replace('SATISFIABLE', '').replace('Optimization: ', '').replace('OPTIMUM FOUND', '')
                for word in line[2:-1].split(' '):
                    word = word.split(',')
                    path[self.__get_position(int(word[0][5:]), int(word[1]))] = word[2][0]
        os.remove('solution.lp')
        with open('solution.txt', 'w+') as output:
            for position in range(0, rows*columns):
                if position+1 in path:
                    if path[position+1] == 'obstacle':
                        output.write('#')
                    else:
                        output.write(path[position+1])
                else:
                    output.write('.')
                if (position % self.__size == self.__size-1):
                    output.write('\n')
        print('Solution written in: solution.txt')

    def __get_position(self, x, y):
        return x+y*self.__size+1

if __name__ == '__main__':
    parser = ArgumentParser(description='Routing solver')
    parser.add_argument('input_file', metavar='I', type=str, help='path of the wire routing instance')
    parser.add_argument('-o', '--optimum', action='store_true', help='calculate optimum path')
    args = parser.parse_args()
    AspSolver(args.input_file, args.optimum)