import roman
import unittest

class ToRomanBadInput(unittest.TestCase):
    def testTooLarge(self):
        # toRoman should fail with this large input
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 4000)

    def testZero(self):
        # toRoman should fail if the input is zero
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

    def testNegative(self):
        # toRoman should fail if the input is negative
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)
    
    def testFloat(self):
        # toRoman should fall if the input is a fraction
        self.assertRaises(roman.NotAnIntegerError, roman.toRoman, 0.5)

class KnownValues(unittest.TestCase):              
    knownValues = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))           

    def testToRomanKnownvalues(self):          
        '''toRoman should give known result with known input'''
        for integer, numeral in self.knownValues:
            result = roman.toRoman(integer)       
            self.assertEqual(numeral, result)      


class RoundtripCheck(unittest.TestCase):
    def testRoundtrip(self):
        
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            result = roman.fromRoman(numeral)
            self.assertEqual(integer, result)

class FromRomanBadInput(unittest.TestCase):
    def testEmptyString(self):
        # fromRoman should fail with empty string input
        self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, '')

    def testTooManyRepeatedNumerals(self):
        # fromRoman should fail with too many repeated numerals
            for s in ('MMMM',
                      'DD',
                      'CCCC',
                      'LL',
                      'XXXX',
                      'VV',
                      'IIII'):
                self.assertRaises(roman.InvalidRomanNumeralError,
                                 roman.fromRoman, s)
    def testMalformedAntecedents(self):
        # fromRoman should fail with malformed antecedents
         for s in ('IIMXCC',
                   'VX',
                   'DCM',
                   'CMM',
                   'IXIV',
                   'MCMC',
                   'XCX',
                   'IVI',
                   'LM',
                   'LD',
                   'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, 
                             roman.fromRoman, s)


    def testRepeatedPairs(self):
        # fromRoman should fail with repeated pairs in numerals
        for s in ('CMCM',
                  'CDCD',
                  'XCXC',
                  'XLXL',
                  'IXIX',
                  'IVIV'):
           self.assertRaises(roman.InvalidRomanNumeralError,
                         roman.fromRoman, s)

                    
if __name__ == '__main__':
    unittest.main()

