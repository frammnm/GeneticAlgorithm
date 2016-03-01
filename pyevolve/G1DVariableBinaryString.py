from GenomeBase import GenomeBase, G1DBase
import Consts
import Util

class G1DVariableBinaryString(G1DBase):
   """ G1DBinaryString Class - The 1D Variable Binary String chromosome

   This chromosome class extends the :class:`GenomeBase.G1DBase` class.

   Example:
      >>> genome = G1DVariableBinaryString.G1DVariableBinaryString(5,2)

   :param ruleLength: the length of each rule
   :param numRules: the number of rules

   """
   __slots__ = ["stringLength"]

   def __init__(self, rulelength=10, numRules=1):
      """ The initializator of G1DList representation """
      super(G1DBinaryStringVariable, self).__init__(ruleLength*numRules,rulelength)
      self.genomeList = []
      self.stringLength = ruleLength*NumRules
      self.ruleLength = ruleLength
      self.initializator.set(Consts.CDefG1DVariableBinaryStringInit)
      self.mutator.set(Consts.CDefG1DVariableBinaryStringMutator)
      self.crossover.set(Consts.CDefG1DVariableBinaryStringCrossover)

   def __setitem__(self, key, value):
      """ Set the specified value for an gene of List

      >>> g = G1DBinaryString(5)
      >>> for i in xrange(len(g)):
      ...    g.append(1)
      >>> g[4] = 0
      >>> g[4]
      0

      """
      if value not in (0, 1):
         Util.raiseException("The value must be zero (0) or one (1), used (%s)" % value, ValueError)
      G1DBase.__setitem__(self, key, value)

   def __repr__(self):
      """ Return a string representation of Genome """
      ret = GenomeBase.__repr__(self)
      ret += "- G1DBinaryString\n"
      ret += "\tString length:\t %s\n" % (self.getListSize(),)
      ret += "\tString:\t\t %s\n\n" % (self.getBinary(),)
      return ret

   def getDecimal(self):
      """ Converts the binary string to decimal representation

      Example:
         >>> g = G1DBinaryString(5)
         >>> for i in xrange(len(g)):
         ...    g.append(0)
         >>> g[3] = 1
         >>> g.getDecimal()
         2

      :rtype: decimal value

      """
      return int(self.getBinary(), 2)

   def getBinary(self):
      """ Returns the binary string representation

      Example:
         >>> g = G1DBinaryString(2)
         >>> g.append(0)
         >>> g.append(1)
         >>> g.getBinary()
         '01'

      :rtype: the binary string

      """
      return "".join(map(str, self))

   def append(self, value):
      """ Appends an item to the list

      Example:
         >>> g = G1DBinaryString(2)
         >>> g.append(0)

      :param value: value to be added, 0 or 1

      """
      if value not in [0, 1]:
         Util.raiseException("The value must be 0 or 1", ValueError)
      G1DBase.append(self, value)

   def copy(self, g):
      """ Copy genome to 'g'

      Example:
         >>> g1 = G1DBinaryString(2)
         >>> g1.append(0)
         >>> g1.append(1)
         >>> g2 = G1DBinaryString(2)
         >>> g1.copy(g2)
         >>> g2[1]
         1

      :param g: the destination genome

      """
      GenomeBase.copy(self, g)
      G1DBase.copy(self, g)

   def clone(self):
      """ Return a new instace copy of the genome

      Example:
         >>> g = G1DBinaryString(5)
         >>> for i in xrange(len(g)):
         ...    g.append(1)
         >>> clone = g.clone()
         >>> clone[0]
         1

      :rtype: the G1DBinaryString instance clone

      """
      newcopy = G1DBinaryString(self.getListSize())
      self.copy(newcopy)
      return newcopy