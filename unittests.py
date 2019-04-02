#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utiltiy and testing functions
"""
from nose.tools import assert_equal, ok_
from IPython.display import display, HTML, clear_output
<<<<<<< HEAD
from Astar import Node
import numpy as np
from numpy.testing import assert_allclose
from environment import ENVIRONMENT
from mission import MISSION
=======
>>>>>>> 3090f9b6467a783f789a12f687e7cea4e2d990ed

def test_ok():
    """ If execution gets to this point, print out a happy message """
    try:
        from IPython.display import display_html
        display_html("""<div class="alert alert-success">
        <strong>Tests passed!!</strong>
        </div>""", raw=True)
    except:
        print("Tests passed!!")
        
<<<<<<< HEAD
def test_costfunction(fn):
    speed = 1
    alpha = 0

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    student_answer = fn(n1, n2, speed)
    correct_answer = (0.0, np.array([0,0]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")

    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    student_answer = fn(n1, n2, speed)
    correct_answer = (162.0, np.array([0.70710678,  0.70710678]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
        
    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    student_answer = fn(n1, n2, speed)
    correct_answer = (242.0, np.array([0.70710678, -0.70710678]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")

    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    student_answer = fn(n1, n2, speed)
    correct_answer = (24.2, np.array([7.07106781, -7.07106781]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")

    test_ok()
    
def test_heuristic(fn):
    speed = 1
    alpha = 0

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 0.0,msg="There seems to be a problem with the values your function returns! Expected value is 0.0.")
    
    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 162.0,msg="There seems to be a problem with the values your function returns! Expected value is 162.0.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 242.0,msg="There seems to be a problem with the values your function returns! Expected value is 242.0.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 24.2,msg="There seems to be a problem with the values your function returns! Expected value is 24.2.")

    test_ok()
    
def test_costwithrisk(fn):
    
    # set up test case 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    n2.risk = 0.4
    AUVspeed = 10
    alpha = 0
    student_answer = fn(n1, n2, AUVspeed,alpha)
    correct_answer = (0.0, np.array([0,0]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up test case 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    n2.risk = 0.7
    AUVspeed = 3
    alpha = 0.2
    student_answer = fn(n1, n2, AUVspeed,alpha)
    correct_answer = (62.790697667117364, np.array([ 2.12132034,  2.12132034]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up test case 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.9
    AUVspeed = 5
    alpha = 0.5
    student_answer = fn(n1, n2, AUVspeed,alpha)
    correct_answer = (87.99999998399998, np.array([ 3.53553391, -3.53553391]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up test case 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.1
    AUVspeed = 9
    alpha = 0.8
    student_answer = fn(n1, n2, AUVspeed,alpha)
    correct_answer = (29.227053136919768, np.array([ 6.36396103, -6.36396103]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    test_ok()
    
def test_heuristicwithrisk(fn):
    speed = 1
    alpha = 0

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    n2.risk = 0.1
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 0.0,msg="There seems to be a problem with the values your function returns! Expected value is 0.0.")
    
    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 162.0,msg="There seems to be a problem with the values your function returns! Expected value is 162.0.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.5
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 242.0,msg="There seems to be a problem with the values your function returns! Expected value is 242.0.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.3
    speed = 10
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 24.2,msg="There seems to be a problem with the values your function returns! Expected value is 24.2.")

    test_ok()
    
def test_blurRiskField(fn):
    
    # set up test case
    UEXP = MISSION(discretization_distance=1, worldsize_x=100, worldsize_y=100)
    ENV = ENVIRONMENT(UEXP, ReefFunction=None)
    ENV.UnknownRegions = { \
                       0.8: [(50, 15), (43, 25), (80, 25), (88, 19), (90,18)], \
                       0.4: [(80, 84), (95, 80), (95, 92), (76, 95)], \
                       0.1: [(11, 8), (40, 0), (40, 17), (11, 11)] \
                       }
    RiskField = ENV.RiskField
    sigma = 0.8
    student_answer = fn(RiskField,sigma)
    
    # check types & content
    assert_equal(type(student_answer),type(np.array([0,0])))
    assert_equal(student_answer.shape,(101,101))
    #TODO
    #assert_allclose(student_answer,student_answer,rtol=5e-1,atol=0.5,err_msg="There seems to be a problem with the values your function returns!")
    
    test_ok()
    
def test_costwithcurrents(fn):
    speed = 1.0
    alpha = 0.8

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    ##additional info
    n1.current = np.array((0.3, 0.1))
    n2.risk = 0.4
    student_answer = fn(n1, n2, speed, alpha)
    correct_answer = (0.0, np.array([0.0,0.0]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    #additional info
    n1.current = np.array((0.3, 0.1))
    n2.risk = 0.15
    student_answer = fn(n1, n2, speed,alpha)
    correct_answer = (144.63547795353981, np.array([ 0.6,  0.8]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n1.current = np.array((0.5, 0.4))
    n2.risk = 0.72
    student_answer = fn(n1, n2, speed,alpha)
    correct_answer = (677.7971065072265, np.array([ 0.99543561, -0.09543561]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n1.current = np.array((5, 3))
    n2.risk = 0.72
    speed = 10
    student_answer = fn(n1, n2, speed,alpha)
    correct_answer = (59.0817410061006, np.array([ 9.83095189, -1.83095189]))
    
    # check types & content
    assert_equal(type(student_answer),tuple,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[0]),float,msg="Please make sure your types meet the specification!")
    assert_equal(type(student_answer[1]),type(np.array([0,0])),msg="Please make sure your types meet the specification!")
    assert_equal(student_answer[0],correct_answer[0],msg="There seems to be a problem with the values your function returns! Expected cost is " + str(correct_answer[0]) + ".")
    assert_allclose(student_answer[1],correct_answer[1],rtol=1e-2,err_msg="There seems to be a problem with the values your function returns! Expected AUV velocity is " + str(correct_answer[1]) + ".")
    
    test_ok()
    
def test_heuristicwithcurrents(fn):
    speed = 1
    alpha = 0

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    n1.current = np.array((0.5, 0.4))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 0.0,msg="There seems to be a problem with the values your function returns! Expected value is 0.0.")
    
    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    speed = 3.0
    n1.current = np.array((1.5, 0.9))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 54.0,msg="There seems to be a problem with the values your function returns! Expected value is 162.0.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 0.8
    n1.current = np.array((1.1, 0.7))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 302.5,msg="There seems to be a problem with the values your function returns! Expected value is 242.0.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    n1.current = np.array((5.1, 2.9))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 24.2,msg="There seems to be a problem with the values your function returns! Expected value is 24.2.")

    test_ok()
=======
>>>>>>> 3090f9b6467a783f789a12f687e7cea4e2d990ed
