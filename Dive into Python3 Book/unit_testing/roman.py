class  OutOfRangeError(ValueError):
    pass

class NotAnIntegerError(ValueError):
    pass

class InvalidRomanNumeralError(ValueError):
    pass

romanNumeralMap = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1)) 

def toRoman(n):
    # convert integer to Roman numeral
    if not(0 < n < 4000):
        raise OutOfRangeError('number must be less than 4000')
    if not isinstance(n, int):
        raise NotAnIntegerError('number must be an integer')
    result = ''
    for numeral, integer in romanNumeralMap:
        while n >= integer:                    
            result += numeral
            n -= integer
    return result

def fromRoman(s):
    # convert roman numeral in to integer
    result = 0
    index = 0
    repeatedNumerals = ['MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII']
    repeatedPairs = ['CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV']
    malformedAntecedents = ['IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                             'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC']
    if s == '':
        raise InvalidRomanNumeralError('should not have an empty input string')
    if s in repeatedNumerals:
        raise InvalidRomanNumeralError('Numeral should  not have too many repeated numerals')
    if s in repeatedPairs:
        raise InvalidRomanNumeralError('Numeral should not have repeated pairs')
    if s in malformedAntecedents:
        raise InvalidRomanNumeralError('Numerals should not have any malformed Antecedents')
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral: 
            result += integer
            index += len(numeral)
    return result   
