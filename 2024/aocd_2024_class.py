import runpy
import os

date = 1
part = 1

class aocd():
    def __init__(self,day_of_month,part):
        self.day_of_month = day_of_month
        self.part = part
    
    def run_solver(self):
        assert(0<self.day_of_month<32)
        assert(self.part in [1,2])
        filepath = f'Dec_{self.day_of_month}/dec_{self.day_of_month}_pt_{self.part}.py'
        if os.path.isfile(filepath):
            print(f'Executing file: {filepath}')
            runpy.run_path(filepath)
        else:
            print(f'File not found! {filepath}')

if __name__ == '__main__':
    puzzle = aocd(1,2)
    puzzle.run_solver()