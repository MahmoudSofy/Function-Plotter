import pytest
import sys
sys.path.append(".")
from plotter import prepare

def test_sin():
    test = "sin(x)"
    assert prepare(test) == "np.sin(x)"

def test_sinh():
    test = "sinh(x)"
    assert prepare(test) == "np.sinh(x)"

def test_arcsin():
    test = "arcsin(x)"
    assert prepare(test) == "np.arcsin(x)"

def test_arcsinh():
    test = "arcsinh(x)"
    assert prepare(test) == "np.arcsinh(x)"
    
def test_cos():
    test = "cos(x)"
    assert prepare(test) == "np.cos(x)"

def test_cosh():
    test = "cosh(x)"
    assert prepare(test) == "np.cosh(x)"

def test_arccos():
    test = "arccos(x)"
    assert prepare(test) == "np.arccos(x)"

def test_arccosh():
    test = "arccosh(x)"
    assert prepare(test) == "np.arccosh(x)"

def test_tan():
    test = "tan(x)"
    assert prepare(test) == "np.tan(x)"


def test_tanh():
    test = "tanh(x)"
    assert prepare(test) == "np.tanh(x)"

def test_arctan():
    test = "arctan(x)"
    assert prepare(test) == "np.arctan(x)"

def test_arctanh():
    test = "arctanh(x)"
    assert prepare(test) == "np.arctanh(x)"

def test_power():
    test = "x^x"
    assert prepare(test) == "x**x"

def test_exp():
    test = "e^(x)"
    assert prepare(test) == "np.exp(x)"

def test_ln():
    test = "ln(x)"
    assert prepare(test) == "np.log(x)"

def test_log():
    test = "log(x)"
    assert prepare(test) == "np.log10(x)"

def test_compex_function():
    test = "(1+x^sinh(x))+e^(1/(cosh(x)+tan(x)))+log(arcsin(5*x))"
    assert prepare(test) == "(1+x**np.sinh(x))+np.exp(1/(np.cosh(x)+np.tan(x)))+np.log10(np.arcsin(5*x))"
