import sys, os
sys.path.insert(0, os.getcwd())

from notebook import Notebook, required, dependency

class HelloWorld(Notebook):
  @required
  def init(self):
    print('Initializing...')



if __name__ == "__main__":
  HelloWorld.main()