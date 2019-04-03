#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Various utiltiy and testing functions
"""
from nose.tools import assert_equal, ok_
from IPython.display import display, HTML, clear_output
from Astar import Node
import numpy as np
from numpy.testing import assert_allclose
from environment import ENVIRONMENT
from mission import MISSION

def test_ok():
    """ If execution gets to this point, print out a happy message """
    try:
        from IPython.display import display_html
        display_html("""<div class="alert alert-success">
        <strong>Tests passed!!</strong>
        </div>""", raw=True)
    except:
        print("Tests passed!!")
        
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
    correct_answer = (12.727922061357855, np.array([0.70710678,  0.70710678]))
    
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
    correct_answer = (15.556349186104045, np.array([0.70710678, -0.70710678]))
    
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
    correct_answer = (1.5556349186104046, np.array([7.07106781, -7.07106781]))
    
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
    assert_equal(student_answer, 12.727922061357855,msg="There seems to be a problem with the values your function returns! Expected value is 12.727922061357855.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 15.556349186104045,msg="There seems to be a problem with the values your function returns! Expected value is 15.556349186104045.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 1.5556349186104046,msg="There seems to be a problem with the values your function returns! Expected value is 1.5556349186104046.")

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
    correct_answer = (4.933303123983668, np.array([ 2.12132034,  2.12132034]))
    
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
    correct_answer = (5.656854248463861, np.array([ 3.53553391, -3.53553391]))
    
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
    correct_answer = (1.8787861333832294, np.array([ 6.36396103, -6.36396103]))
    
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
    assert_equal(student_answer, 12.727922061357855,msg="There seems to be a problem with the values your function returns! Expected value is 12.727922061357855.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.5
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 15.556349186104045,msg="There seems to be a problem with the values your function returns! Expected value is 15.556349186104045.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    n2.risk = 0.3
    speed = 10
    student_answer = fn(n1, n2, speed)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 1.5556349186104046,msg="There seems to be a problem with the values your function returns! Expected value is 1.5556349186104046.")

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
    
    test_ok()
    
def test_costwithcurrents(fn):
    speed = 1.0
    alpha = 0.8

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
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
    n1.current = np.array((0.3, 0.1))
    n2.risk = 0.15
    student_answer = fn(n1, n2, speed,alpha)
    correct_answer = (11.363636362345042, np.array([ 0.6,  0.8]))
    
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
    correct_answer = (43.570448207261855, np.array([ 0.99543561, -0.09543561]))
    
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
    correct_answer = (3.7979181554291856, np.array([ 9.83095189, -1.83095189]))
    
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
    max_strength = 1

    # set up sample problem 1
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    n1.current = np.array((0.5, 0.4))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 0.0,msg="There seems to be a problem with the values your function returns! Expected value is 0.0.")
    
    # set up sample problem 2
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    speed = 3.0
    n1.current = np.array((1.5, 0.9))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 3.181980515339464,msg="There seems to be a problem with the values your function returns! Expected value is 3.181980515339464.")

    # set up sample problem 3
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 0.8
    n1.current = np.array((1.1, 0.7))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 8.642416214502248,msg="There seems to be a problem with the values your function returns! Expected value is 8.642416214502248.")
    
    # set up sample problem 4
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    n1.current = np.array((5.1, 2.9))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 1.414213562373095,msg="There seems to be a problem with the values your function returns! Expected value is 1.414213562373095.")
    
    max_strength = 10
    
    # set up sample problem 5
    n1 = Node(None, (1,1))
    n2 = Node(None, (1,1))
    n1.current = np.array((0.5, 0.4))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 0.0,msg="There seems to be a problem with the values your function returns! Expected value is 0.0.")
    
    max_strength = 0
    
    # set up sample problem 6
    n1 = Node(None, (1,1))
    n2 = Node(None, (10,10))
    speed = 3.0
    n1.current = np.array((1.5, 0.9))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 4.242640687119285,msg="There seems to be a problem with the values your function returns! Expected value is 4.242640687119285.")
    
    max_strength = 5

    # set up sample problem 7
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 0.8
    n1.current = np.array((1.1, 0.7))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 2.682129170017939,msg="There seems to be a problem with the values your function returns! Expected value is 2.682129170017939.")
    
    # set up sample problem 8
    n1 = Node(None, (-1,1))
    n2 = Node(None, (10,-10))
    speed = 10
    n1.current = np.array((5.1, 2.9))
    student_answer = fn(n1, n2, speed, max_strength)
    assert_equal(type(student_answer),float,msg="Please make sure your types meet the specification!")
    assert_equal(student_answer, 1.0370899457402696,msg="There seems to be a problem with the values your function returns! Expected value is 1.0370899457402696.")

    test_ok()