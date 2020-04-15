"""
The verification functions for Course 2 scripts

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import os, os.path, sys
import importlib, importlib.util
import traceback
import inspect
import builtins
from modlib import *

# For support
import introcs

#mark Constants

# The status codes
TEST_SUCCESS      = 0
FAIL_NO_FILE      = 1
FAIL_BAD_STYLE    = 2
FAIL_CRASHES      = 4
FAIL_INCORRECT    = 5


WORKSPACE = [os.path.expanduser('~'),'workspace','exercise1']
#WORKSPACE = ['activity3']


#mark -
#mark Test Capture
class TestPlan(object):

    @property
    def tested(self):
        """
        The captured print statements of this environment.

        Each call to `print` is a separate entry to this list.  Special
        endlines (or files) are ignored.

        **Invariant**: Value is a list of strings.
        """
        return self._tests

    @property
    def asserted(self):
        """
        The captured input statements of this environment.

        Each call to `input` adds a new element to the list.  Only the
        prompts are added to this list, not the user response (which
        are specified in the initializer).

        **Invariant**: Value is a list of strings or None.
        """
        return self._asserts
    
    def __init__(self,env):
        self._environment = env
        self._tests   = {}
        self._asserts = {}
    
    def reset(self):
        self._tests   = {}
        self._asserts = {}
    
    def assert_equals(self,expected,received,message=None):
        """
        Wrapper for introcs.assert_equals
        """
        if not 'assert_equals' in self._asserts:
            self._asserts['assert_equals'] = []
        self._asserts['assert_equals'].append((expected,received))
    
    def assert_not_equals(self,expected,received,message=None):
        """
        Wrapper for introcs.assert_not_equals
        """
        if not 'assert_not_equals' in self._asserts:
            self._asserts['assert_not_equals'] = []
        self._asserts['assert_not_equals'].append((expected,received))
    
    def assert_true(self,received,message=None):
        """
        Wrapper for introcs.assert_true
        """
        if not 'assert_true' in self._asserts:
            self._asserts['assert_true'] = []
        self._asserts['assert_true'].append(received)
    
    def assert_false(self,received,message=None):
        """
        Wrapper for introcs.assert_false
        """
        if not 'assert_false' in self._asserts:
            self._asserts['assert_false'] = []
        self._asserts['assert_false'].append(received)
    
    def assert_floats_equal(self,expected, received,message=None):
        """
        Wrapper for introcs.assert_floats_equal
        """
        if not 'assert_floats_equal' in self._asserts:
            self._asserts['assert_floats_equal'] = []
        self._asserts['assert_floats_equal'].append((expected,received))
    
    def assert_floats_not_equal(self,expected, received,message=None):
        """
        Wrapper for introcs.assert_floats_not_equal
        """
        if not 'assert_floats_not_equal' in self._asserts:
            self._asserts['assert_floats_not_equal'] = []
        self._asserts['assert_floats_not_equal'].append((expected,received))
    
    def has_a_vowel1(self,s):
        """
        Incorrect version for first pass
        """
        if not 'has_a_vowel' in self._tests:
            self._tests['has_a_vowel'] = []
        self._tests['has_a_vowel'].append(s)
        return not ('a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s)
    
    def has_a_vowel2(self,s):
        """
        Correct version
        """
        self._environment.print('___test___')
        if not 'has_a_vowel' in self._tests:
            self._tests['has_a_vowel'] = []
        self._tests['has_a_vowel'].append(s)
        return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s
    
    def has_a_vowel3(self,s):
        """
        Correct version, no logging
        """
        return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s


pass
#mark -
#mark Helpers
def read_file(name):
    """
    Returns the contents of the file or None if missing.
    
    Parameter name: The file name
    Precondition: name is a string
    """
    path = os.path.join(*WORKSPACE,name)
    try:
        with open(path) as file:
            result = file.read()
        return result
    except:
        return None


def import_module(name,step=0):
    """
    Returns a reference to the module.
    
    Returns an error message if it fails.
    
    Parameter name: The module name
    Precondition: name is a string
    """
    try:
        import types
        refs = os.path.splitext(name)[0]
        environment = Environment(refs,WORKSPACE)
        testplan = TestPlan(environment)
        
        intro = types.ModuleType('introcs')
        for func in dir(introcs):
            if func[0] != '_':
                if 'assert' in func and hasattr(testplan,func):
                    setattr(intro,func,getattr(testplan,func))
                else:
                    setattr(intro,func,getattr(introcs,func))
        environment.capture('introcs',intro)
        
        if step < 2:
            func = types.ModuleType('funcs')
            if step:
                func.has_a_vowel = testplan.has_a_vowel2
            else:
                func.has_a_vowel = testplan.has_a_vowel1
            environment.capture('funcs',func)
        else:
            try:
                func = load_from_path('funcs',WORKSPACE)
                func.print = environment.print
                func.input = environment.input
                environment.capture('funcs',func)
            except:
                pass
        
        if not environment.execute():
            return ('\n'.join(environment.printed)+'\n',None)
        return (environment, testplan)
    except Exception as e:
        msg = traceback.format_exc(0)
        pos2 = msg.find('^')
        pos1 = msg.rfind(')',0,pos2)
        if 'SyntaxError: unexpected EOF' in msg or 'IndentationError' in msg:
            msg = 'Remember to include and indent the docstring properly.\n'+msg
        elif pos1 != -1 and pos2 != -1 and not msg[pos1+1:pos2].strip():
            msg = 'Remember to end the header with a colon.\n'+msg
        else:
            msg = ("File %s has a major syntax error.\n" % repr(name))+msg
        return (msg,None)


# Localized error codes
DOCSTRING_MISSING   = 1
DOCSTRING_UNCLOSED  = 2
DOCSTRING_NOT_FIRST = 3

def get_docstring(text,first=True):
    """
    Returns the docstring as a list of lines
    
    This function returns an error code if there is no initial docstring.
    
    Parameter text: The text to search for a docstring.
    Precondition: text is a string
    
    Parameter text: Whether to require the docstring to be first.
    Precondition: text is a string
    """
    lines = text.split('\n')
    lines = list(map(lambda x: x.strip(),lines))
    
    start = -1
    for pos in range(len(lines)):
        if len(lines[pos]) >= 3 and lines[pos][:3] in ['"""',"'''"]:
            start = pos
            break
    
    if start == -1:
        return DOCSTRING_MISSING
    
    end = -1
    for pos in range(start+1,len(lines)):
        if lines[pos][-3:] == lines[start][:3]:
            end = pos
            break
    
    if end == -1:
        return DOCSTRING_UNCLOSED
    
    if first:
        for pos in range(start):
            if len(lines[pos]) > 0:
                return DOCSTRING_NOT_FIRST
    
    # One last trim
    if len(lines[start]) > 3:
        lines[start] = lines[start][3:]
    else:
        start += 1
    if len(lines[end]) > 3:
        lines[end] = lines[end][:-3]
    else:
        end -= 1
    return lines[start:end+1]


# Localized error codes
NAME_MISSING     = 1
NAME_INCOMPLETE  = 2

def check_name(text):
    """
    Returns TEST_SUCCESS if the name is correct, and error code otherwise
    
    Parameter text: The docstring text as a list.
    Precondition: text is a list of strings
    """
    if not text[-2].lower().startswith('author:'):
        return NAME_MISSING
    if not text[-2][7:].strip():
        return NAME_INCOMPLETE
    if 'your name here' in text[-2][7:].lower():
        return NAME_INCOMPLETE
    return TEST_SUCCESS


# Localized error codes
DATE_MISSING     = 1
DATE_INCOMPLETE  = 2

def check_date(text):
    """
    Returns TEST_SUCCESS if the date is correct, and error code otherwise
    
    Parameter text: The docstring text as a list.
    Precondition: text is a list of strings
    """
    if not text[-1].lower().startswith('date:'):
        return DATE_MISSING
    
    date = text[-1][5:].strip()
    try:
        import dateutil.parser as util
        temp = util.parse(date)
        return TEST_SUCCESS
    except:
        return DATE_INCOMPLETE


pass
#mark -
#mark Test Case Checking
def first_vowel(s):
    """
    Returns: The location of the first vowel (a,e,i,o, or u) in s
    
    This function returns -1 if there is no vowel.
    
    Parameter s: The string to check
    Precondition: s is a string of lower case letters (possibly empty)
    """
    vowels = []
    for x in 'aeiou':
        if x in s:
            vowels.append(s.find(x))
    pos = -1 if vowels == [] else min(vowels)
    return ('' if pos == -1 else s[pos],pos)


def encode_a_vowel(input):
    """
    Returns: the hash encoding for input to has_a_vowel
    
    Parameter input: The input to has_a_vowel
    Precondition: s is a non-empty string with all lower case letters
    """
    """
    The test encoder for has_a_vowel
    """
    if type(input) != str:
        return -1
    elif not input.isalpha():
        return -1
    elif not input.islower():
        return -1
    
    if 'a' in input and 'e' in input and 'i' in input and 'o' in input and 'u' in input:
        return 8
    
    first = first_vowel(input)
    secnd = first_vowel(input[first[1]+1:])
    first = first[0]
    secnd = secnd[0]
    
    if first == '':
        if 'y' in input:
            return 6
        return 7
    elif first == 'a':
        if secnd == '':
            return 1
        elif secnd == 'a':
            return 9
        elif secnd == 'e':
            return 10
        elif secnd == 'i':
            return 11
        elif secnd == 'o':
            return 12
        elif secnd == 'u':
            return 13
    elif first == 'e':
        if secnd == '':
            return 2
        elif secnd == 'a':
            return 10
        elif secnd == 'e':
            return 14
        elif secnd == 'i':
            return 15
        elif secnd == 'o':
            return 16
        elif secnd == 'u':
            return 17
    elif first == 'i':
        if secnd == '':
            return 3
        elif secnd == 'a':
            return 11
        elif secnd == 'e':
            return 15
        elif secnd == 'i':
            return 18
        elif secnd == 'o':
            return 19
        elif secnd == 'u':
            return 20
    elif first == 'o':
        if secnd == '':
            return 4
        elif secnd == 'a':
            return 12
        elif secnd == 'e':
            return 16
        elif secnd == 'i':
            return 19
        elif secnd == 'o':
            return 21
        elif secnd == 'u':
            return 22
    elif first == 'u':
        if secnd == '':
            return 5
        elif secnd == 'a':
            return 13
        elif secnd == 'e':
            return 17
        elif secnd == 'i':
            return 20
        elif secnd == 'o':
            return 22
        elif secnd == 'u':
            return 23
    
    return 24


# The explanatory reasons for the tests
TEST_A_VOWEL = [
    "a basic test with only vowel 'a'",
    "a basic test with only vowel 'e'",
    "a basic test with only vowel 'i'",
    "a basic test with only vowel 'o'",
    "a basic test with only vowel 'u'",
    "a basic test no vowels",
    "a test with forbidden vowel 'y'",
    "a test with all vowels",
    "a test with multiple instances of 'a'",
    "a test with vowels 'a' and 'e'",
    "a test with vowels 'a' and 'i'",
    "a test with vowels 'a' and 'o'",
    "a test with vowels 'a' and 'u'",
    "a test with multiple instances of 'e'",
    "a test with vowels 'e' and 'i'",
    "a test with vowels 'e' and 'o'",
    "a test with vowels 'e' and 'u'",
    "a test with multiple instances of 'i'",
    "a test with vowels 'i' and 'o'",
    "a test with vowels 'i' and 'u'",
    "a test with multiple instances of 'o'",
    "a test with vowels 'o' and 'u'",
    "a test with multiple instances of 'u'",
    "a complex test with more than two vowels"
]


pass
#mark -
#mark Subgraders
def grade_docstring(file,step=0,outp=sys.stdout):
    """
    Returns the test result and score for the docstring.
    
    The step parameter is the phase in the grading pass.  Step 0 is a verification step
    and will stop at the first error found.  Otherwise it will continue through and try 
    to find all errors.
    
    Parameter name: The file name
    Precondition: name is a string of a file in the given workspace
    
    Parameter step: The current verfication/grading step
    Precondition: grade is 0 or 1
    
    Parameter outp: The output stream
    Precondition: outp is a stream writer
    """
    code = read_file(file)
    if code is None:
        outp.write('Could not find the file %s.\n' % repr(file))
        return (FAIL_NO_FILE, 0)
    
    score = 1
    docs = get_docstring(code)
    if type(docs) == int:
        if docs == DOCSTRING_MISSING:
            outp.write('There is no docstring in %s.\n' % repr(file))
            return (FAIL_BAD_STYLE,0)
        if docs == DOCSTRING_UNCLOSED:
            outp.write('The docstring is not properly closed.\n')
            return (FAIL_CRASHES,0.1)
        if docs == DOCSTRING_NOT_FIRST:
            outp.write('The docstring is not the first non-blank line.\n')
            score -= 0.3
        if not step:
            return (FAIL_BAD_STYLE,max(0,score))
    docs = get_docstring(code,False)
    
    test = check_name(docs)
    if test:
        if test == NAME_MISSING:
            outp.write("The second-to-last line of the docstring does not start with 'Author:'\n")
            score -= 0.3
        if test == NAME_INCOMPLETE:
            outp.write("There is no name after 'Author:'\n")
            score -= 0.1
        if not step:
            return (FAIL_BAD_STYLE,max(0,score))
    test = check_date(docs)
    if test:
        if test == DATE_MISSING:
            outp.write("The last line of the docstring  does not start with 'Date:'\n")
            score -= 0.2
        if test == DATE_INCOMPLETE:
            outp.write("The date after 'Date:' is invalid.\n")
            score -= 0.1
        if not step:
            return (FAIL_BAD_STYLE, max(0,score))
    
    return (TEST_SUCCESS, max(0,score))


def grade_testcases(file,step=0,outp=sys.stdout):
    """
    Returns the test result and score for the test cases
    
    The step parameter is the phase in the grading pass.  Step 0 only looks for one
    test cases.  Step 1 looks for proper test coverage.  Steps 0-1 will stop at the 
    first error found.  Step 2 is the final grading pass and will continue through and 
    try to find all errors.
    
    Parameter name: The file name
    Precondition: name is a string of a file in the given workspace
    
    Parameter step: The current verfication/grading step
    Precondition: grade is 0 or 1
    
    Parameter outp: The output stream
    Precondition: outp is a stream writer
    """
    env, tests = import_module(file,0)
    if type(env) == str:
        outp.write(env)
        return (FAIL_CRASHES,0)
    
    # Step 1
    score = 1
    if not hasattr(env.module,'introcs') or not hasattr(env.module,'funcs'):
        outp.write("You have modified the import statements, violating the instructions.\n")
        return (FAIL_INCORRECT,0)
    
    if not 'has_a_vowel' in tests.tested:
        outp.write("You have not called the function 'has_a_vowel' properly.\n")
        return (FAIL_INCORRECT,0)
    elif tests.tested['has_a_vowel'][0] != 'aeiou':
        outp.write("You were instructed to make the first test input 'aeiou'.\n")
        score -= 0.05
        if step < 2:
            return (FAIL_INCORRECT, max(0,score))
    
    if not 'assert_equals' in tests.asserted or len(tests.asserted['assert_equals']) != len(tests.tested['has_a_vowel']):
        outp.write("You were supposed to call 'assert_equals' for each test case.\n")
        score -= 0.1
        if step < 2:
            return (FAIL_INCORRECT, max(0,score))
    
    badin = None
    for pos in range(len(tests.asserted['assert_equals'])):
        if  pos < len(tests.tested['has_a_vowel']):
            pair  = tests.asserted['assert_equals'][pos]
            input = tests.tested['has_a_vowel'][pos]
            if pair[0] != tests.has_a_vowel3(input) and encode_a_vowel(input) >= 0:
                badin = input
    
    if badin:
        outp.write("In 'assert_equals', the expected value goes first [see %s].\n" % repr(badin))
        score -= 0.1
        if step < 2:
            return (FAIL_BAD_STYLE,0)
    
    env, tests = import_module(file,1)
    if type(env) == str:
        outp.write(env)
        return (FAIL_CRASHES,0)
    
    if step:
        if not 'assert_equals' in tests.asserted or len(tests.asserted['assert_equals']) != len(tests.tested['has_a_vowel']):
            outp.write("You were supposed to call 'assert_equals' for each test case.\n")
            score -= 0.5
            if step < 2:
                return (FAIL_INCORRECT, max(0,score))
        else:
            badin = None
            for pos in range(len(tests.asserted['assert_equals'])):
                pair = tests.asserted['assert_equals'][pos]
                input = tests.tested['has_a_vowel'][pos]
                if pair[0] != pair[1] and encode_a_vowel(input) >= 0:
                    badin = input
            if not badin is None:
                outp.write("The test for input %s has incorrect output.\n" % repr(badin))
                score -= 0.3
                if step < 2:
                    return (FAIL_INCORRECT, max(0,score))
        
        results = [0]*len(TEST_A_VOWEL)
        # Look for proper coverage
        for input in tests.tested['has_a_vowel']:
            code = encode_a_vowel(input)
            if code == -1:
                outp.write("The test input %s violates the precondition.\n" % repr(input))
                score -= 0.2
                if step < 2:
                    return (FAIL_INCORRECT, max(0,score))
            results[code-1] += 1
        for pos in range(len(results)):
            if results[pos] > 1 and pos < len(TEST_A_VOWEL):
                outp.write("You have %s cases of %s (but that is okay).\n" % (repr(results[pos]),TEST_A_VOWEL[pos]))
                
        ntests = len(list(filter(lambda x : x > 0, results)))
        wtests = 10
        if  ntests < wtests:
            outp.write("You only have %d distinct test case%s [wanted %d].\n" % (ntests,'' if ntests == 1 else 's', wtests))
            score -= 0.1* (wtests-ntests)
            if step < 2:
                return (FAIL_INCORRECT, max(0,score))
        
    elif len(tests.tested['has_a_vowel']) > 1:
        outp.write("You should only have one test case right now.\n")
        score -= 0.1
        return (FAIL_INCORRECT, max(0,score))
    
    additional = None
    for line in env.printed:
        if not line in ['___test___','Module funcs is working correctly']:
            additional = line
        
    if not additional is None:
        outp.write("You added the extra print statement %s.\n" % repr(additional))
        score -= 0.1
        if step < 2:
            return (FAIL_BAD_STYLE, max(0,score))
    elif not 'Module funcs is working correctly' in env.printed:
        outp.write("You have removed the final print statement.\n")
        score -= 0.1
        if step < 2:
            return (FAIL_BAD_STYLE, max(0,score))
    elif env.printed[-1] != 'Module funcs is working correctly':
        outp.write("You added test cases after the final print statement.\n")
        score -= 0.1
        if step < 2:
            return (FAIL_BAD_STYLE, max(0,score))
    
    return (TEST_SUCCESS, max(0,score))


def grade_function(file,step=0,outp=sys.stdout):
    """
    Returns the test result and score for the fixing the function.
    
    The step parameter is the phase in the grading pass.  Step 0 is a verification step
    and will stop at the first error found.  Otherwise it will continue through and try 
    to find all errors.
    
    Parameter name: The file name
    Precondition: name is a string of a file in the given workspace
    
    Parameter step: The current verfication/grading step
    Precondition: grade is 0 or 1
    
    Parameter outp: The output stream
    Precondition: outp is a stream writer
    """
    env, tests = import_module(file,2)
    if type(env) == str:
        outp.write(env)
        return (FAIL_CRASHES,0)
    
    score = 1
    if not hasattr(env.module,'introcs') or not hasattr(env.module,'funcs'):
        outp.write("You have modified the import statements, violating the instructions.\n")
        return (FAIL_INCORRECT,0)
    if not hasattr(env.module.funcs,'has_a_vowel'):
        outp.write("You have deleted the function 'has_a_vowel' from func.\n")
        return (FAIL_INCORRECT,0)
    
    func1 = env.module.funcs.has_a_vowel
    func2 = tests.has_a_vowel3
    
    failed = []
    consnts = 'bdcx'
    test = consnts
    try:
        if func1(test) !=  func2(test):
            failed.append(test)
    except:
        failed.append(test)
    test = 'y'+consnts
    try:
        if func1(test) !=  func2(test):
            failed.append(test)
    except:
        failed.append(test)
    test = consnts+'y'
    try:
        if func1(test) !=  func2(test):
            failed.append(test)
    except:
        failed.append(test)
    
    vowels  = 'aeiou'
    test = vowels
    try:
        if func1(test) !=  func2(test):
            failed.append(test)
    except:
        failed.append(test)
    
    for x in vowels:
        test = consnts[:2]+x+consnts[2:]
        try:
            if func1(test) !=  func2(test):
                failed.append(test)
        except:
            failed.append(test)
        
    
    from itertools import combinations_with_replacement as comb
    pairs = comb(vowels,2)
    for item in pairs:
        test =  consnts[:1]+item[0]+consnts[1:3]+item[1]+consnts[3:]
        try:
            if func1(test) !=  func2(test):
                failed.append(test)
        except:
            failed.append(test)
    
    if failed != []:
        score -= 0.1 * len(failed)
        if step:
            outp.write("The fix to function 'has_a_vowel' failed on the following input: %s.\n" % ','.join(map(repr,failed)))
        else:
            outp.write("The fix to function 'has_a_vowel' failed on input %s.\n" % repr(failed[0]))
            return (FAIL_INCORRECT, max(0,score))
    
    return (TEST_SUCCESS, max(0,score))


pass
#mark -
#mark Graders
def grade_file(file,outp=sys.stdout):
    """
    Grades the interactive script, weighting earlier parts less.
    
    Parameter name: The file name
    Precondition: name is a string
    
    Parameter outp: The output stream
    Precondition: outp is a stream writer
    """
    outp.write('Docstring comments:\n')
    status, p1 = grade_docstring(file,1,outp)
    if p1 == 1:
        outp.write('The module docstring looks good.\n\n')
    else:
        outp.write('\n')
    
    if not status:
        outp.write('Test Case comments:\n')
        status, p2 = grade_testcases(file,2,outp)
        if p2 == 1:
            outp.write('The test cases look good.\n\n')
        else:
            outp.write('\n')
    else:
        p2 = 0
    
    if not status:
        outp.write('Bug Fix comments:\n')
        status, p3 = grade_function(file,1,outp)
        if p3 == 1:
            outp.write('The bug fix looks good.\n\n')
        else:
            outp.write('\n')
    else:
        p3 = 0
    
    total = round(0.1*p1+0.7*p2+0.2*p3,3)
    return total


def grade(outp=sys.stdout):
    """
    Invokes this subgrader (returning a percentage)
    """
    return grade_file('tests.py',outp)


if __name__ == '__main__':
    print(grade())