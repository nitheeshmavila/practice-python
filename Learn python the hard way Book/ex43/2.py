class seafood(object):
  def printname(self):
    print('seafood\n')


class fish(seafood):
  def printname(self):
    print('fish\n')

class salmon(fish):
  def printname(self):
    print('salmon\n')



crab=seafood()
ayala=fish()
sal=salmon()


crab.printname()
ayala.printname()
sal.printname()

