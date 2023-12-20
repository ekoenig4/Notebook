import sys, os
sys.path.insert(0, os.getcwd())

from src import Notebook, required, dependency

class HelloWorld(Notebook):
  @required
  def init(self):
    print('Initializing...')

    # create a bunch of random variables for testing
    self.a = 1
    self.b = 2
    self.c = 3

  # create 5 random methods

  def method1(self):
    print('Running method1')

  @dependency(method1)
  def method2(self):
    print('Running method2')

  def method3(self):
    print('Running method3')

  @dependency(method3)
  def method4(self):
    print('Running method4')

  @dependency(method4)
  def method5(self):
    print('Running method5')
  


if __name__ == "__main__":

  nb = HelloWorld()
  nb.hello()

  print('Running method1')
  nb = HelloWorld()
  nb.run(['method1'])
  print(' Done!')
  print()

  print('Running method2')
  nb = HelloWorld()
  nb.run(['method2'])
  print(' Done!')
  print()

  print('Running method3')
  nb = HelloWorld()
  nb.run(['method3'])
  print(' Done!')
  print()

  print('Running method4')
  nb = HelloWorld()
  nb.run(['method4'])
  print(' Done!')
  print()

  print('Running method5')
  nb = HelloWorld()
  nb.run(['method5'])
  print(' Done!')
  print()
